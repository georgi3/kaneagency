from django.shortcuts import render, get_list_or_404
from .models import PortfolioItem, Services, Inquiry, Content
from django.db.models import Q
from django.contrib import messages
from django.core.mail import send_mail
import smtplib
from emb.settings import EMAIL_HOST_USER, REGULAR_EMAIL
import datetime
import pytz


def index(request):
    services = Services.objects.filter(hide=False)
    portfolio_items = PortfolioItem.objects.filter(hide=False).order_by('-date')[:4]
    content = Content.objects.filter(hide_info=False).first()
    year = datetime.datetime.now().year
    context = {
        'services': services,
        'portfolio_items': portfolio_items,
        'content': content,
        'active_page': 'index',
        'year': year
    }
    return render(request, 'home/index.html', context)


def about_us(request):
    content = Content.objects.filter(hide_info=False).first()
    context = {
        'content': content,
        'active_page': 'about'
    }
    print(content.about_par_1)
    return render(request, 'home/about_us.html', context)


def portfolio(request):
    portfolio_items = PortfolioItem.objects.filter(hide=False).order_by('-date')
    services = {item.service_category for item in portfolio_items}
    content = Content.objects.filter(hide_info=False).first()
    context = {
        'portfolio_items': portfolio_items,
        'unique_services': services,
        'content': content,
        'active_page': 'portfolio'
    }
    return render(request, 'home/portfolio.html', context)


def portfolio_item(request, pk):
    portfolio_item = get_list_or_404(PortfolioItem, id=pk, hide=False)
    related_projects = PortfolioItem.objects.filter(~Q(id=pk), service_category=portfolio_item[0].service_category)
    content = Content.objects.filter(hide_info=False).first()
    context = {
        'portfolio_item': portfolio_item,
        'related_projects': related_projects,
        'content': content,
        'active_page': 'portfolio'
    }
    return render(request, 'home/portfolio-item.html', context)


def services(request):
    if request.method == 'POST':
        if int(request.session.get('filed_inquiry', 0)) >= 3:
            messages.error(request, 'You have already submitted an inquiry! For more, please, reach out via e-mail.')
        else:
            inquiry_date = datetime.datetime.now(pytz.timezone('US/Eastern'))
            name = request.POST.get('name')
            email = request.POST.get('email')
            subject = request.POST.get('email_subject')
            service = request.POST.get('service_type')
            budget = request.POST.get('budget')
            message = request.POST.get('inquiry')
            inquiry = Inquiry(inquiry_date=inquiry_date, name=name, email=email, subject=subject,
                              service=service, budget=budget, message=message)
            inquiry.save()
            # with smtplib.SMTP_SSL('mail.privateemail.com', 465) as connection:
            #     print('Logging in...')
            #     connection.login('embaston@embaston.com', 'Embaston3434!emg')
            #     print('Logged in')
            #     connection.sendmail(
            #         from_addr='embaston@embaston.com',
            #         to_addrs=email,
            #         msg=message
            #     )
            #
            mail_message = f"FROM: {name} <{email}>\nSUBJECT: {subject}\nSERVICE: {service}\nBUDGET: " \
                           f"{budget if budget else 'N/A'}\nMESSAGE: {message}"
            send_mail(
                subject='Please DO NOT Reply, Automated Email',
                message='Thank you for submitting the form, our team will get back to you shortly. \nSincerely,'
                        '\nKTAgency',
                from_email=EMAIL_HOST_USER,
                recipient_list=[email],
                fail_silently=False)
            send_mail(subject=subject,
                      message=mail_message,
                      from_email=EMAIL_HOST_USER,
                      recipient_list=[EMAIL_HOST_USER, REGULAR_EMAIL],
                      fail_silently=False)

            messages.success(request, 'Your form has been submitted successfully!')
            prev_value = int(request.session.get('filed_inquiry', 0))
            request.session['filed_inquiry'] = prev_value + 1

    services = Services.objects.filter(hide=False)[::-1]
    content = Content.objects.filter(hide_info=False).first()
    context = {
        'services': services,
        'content': content,
        'active_page': 'services'
    }
    return render(request, 'home/services.html', context)


handler404 = 'home.'

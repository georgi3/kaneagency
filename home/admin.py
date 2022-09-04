from django.contrib import admin
from .models import PortfolioItem, Services, Inquiry, Content


class ContentAdmin(admin.ModelAdmin):
    list_display = ['name', 'hide_info']
    list_editable = ['hide_info']


class InquiryAdmin(admin.ModelAdmin):
    list_display = ['name', 'subject', 'email', 'inquiry_date']
    list_per_page = 25


class ServicesAdmin(admin.ModelAdmin):
    list_display = ['service_name', 'hide']
    list_editable = ['hide']


class PortfolioItemAdmin(admin.ModelAdmin):
    list_display = ['title', 'service_category', 'hide']
    list_editable = ['hide']


admin.site.register(Content, ContentAdmin)
admin.site.register(Inquiry, InquiryAdmin)
admin.site.register(Services, ServicesAdmin)
admin.site.register(PortfolioItem, PortfolioItemAdmin)

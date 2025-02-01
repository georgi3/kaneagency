from django.db import models
from django.core.exceptions import ValidationError
from tinymce.models import HTMLField


class Content(models.Model):
    name = models.CharField('Name', max_length=7, default='Content', help_text='Leave it as it is.',
                            blank=True, null=True)
    about_par_1 = HTMLField('About Info Paragraph 1', help_text='About page first paragraph',
                                         blank=True, null=True)
    city_country = models.CharField('City, Country', max_length=50, help_text='City, Country (Address)',
                                    blank=True, null=True)
    address = models.CharField('Street Number, Name, other', max_length=75, blank=True, null=True)
    email = models.EmailField('Your Email', help_text='Your email for contact info', blank=True, null=True)
    phone_1 = models.CharField('Telephone', max_length=20, help_text='Your phone for contact info. Do the '
                                                                     'formatting here (e.g. +1 (438) 777 7777',
                               blank=True, null=True)
    phone_2 = models.CharField('Telephone', max_length=20, help_text='Your Second phone for contact info. Do the '
                                                                     'formatting here (e.g. +1 (438) 777 7777)',
                               blank=True, null=True)
    intro_text = models.TextField('Intro Text', help_text="Text underneath 'Kane'",
                                  blank=True, null=True)
    services_text = models.TextField('Text for services', help_text="Text underneath 'Services' (home page)",
                                     blank=True, null=True)
    latest_projects_text = models.TextField('Text for latest projects', help_text="Text underneath 'Latest Projects'"
                                                                                  " (home page)", blank=True, null=True)
    twitter_link = models.URLField('Twitter Link', help_text='Contact info', null=True, blank=True)
    spotify_link = models.URLField('Spotify Link', help_text='Contact info', null=True, blank=True)
    fb_link = models.URLField('Facebook Link', help_text='Contact Info', blank=True, null=True)
    ig_link = models.URLField('Instagram Link', help_text='Contact Info', blank=True, null=True)
    linkedin_link = models.URLField('LinkedIn Link', help_text='Contact Info', blank=True, null=True)
    footer_desc_par_1 = models.TextField('Footer Short Description 1', help_text='Paragraph 1, Max one sentence',
                                         max_length=500, blank=True, null=True)
    hide_info = models.BooleanField('Hide all info', help_text='Hide all information', default=False)

    def __str__(self):
        return "Content"

    def clean(self):
        if self.pk is None and len(Content.objects.all()) >= 1:
            raise ValidationError('You are NOT allowed to create more than one content!')

    class Meta:
        verbose_name = 'Content'
        verbose_name_plural = 'Content'


class Inquiry(models.Model):
    inquiry_date = models.DateTimeField(null=True)
    name = models.CharField('Name', max_length=40)
    email = models.EmailField()
    subject = models.CharField('Subject', max_length=30)
    service = models.CharField('Service Type', max_length=30)
    budget = models.CharField('Budget', max_length=20, blank=True, null=True)
    message = models.TextField('Message')
    notes = models.TextField('Personal Notes', blank=True, null=True)

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = 'Inquiry'
        verbose_name_plural = 'Inquiries'
        ordering = ['-inquiry_date']


class Services(models.Model):
    service_name = models.CharField('Service Name', primary_key=True, max_length=30,
                                    help_text='Name of the service you provide')
    short_description = HTMLField('Short Description', help_text='Short Description')
    description = HTMLField('Description', help_text='Detailed Description')
    icon = models.FileField('Icon', upload_to='photos/services/', help_text='MUST BE .SVG EXTENSIONS',
                            blank=False, null=False)
    main_img = models.ImageField('Main Img', upload_to='photos/services/')
    hide = models.BooleanField('Hide Service', help_text='Check to hide service', default=False)

    def __str__(self):
        return self.service_name

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'


class PortfolioItem(models.Model):
    title = models.CharField('Project Name', max_length=30, help_text='Name of the project')
    date = models.DateField('Date of the Event', help_text='Date when the event took place', blank=True, null=True)
    service_category = models.ForeignKey(Services, max_length=30, help_text='Type of the service',
                                         on_delete=models.CASCADE)
    description_1 = HTMLField('Description, Paragraph 1', help_text='Event Description')
    description_2 = HTMLField('Description, Paragraph 2', help_text='Event Description', blank=True, null=True)
    description_3 = HTMLField('Description, Paragraph 3', help_text='Event Description', blank=True, null=True)
    press_link = models.URLField('Press Link', help_text='Link for Press Article', blank=True, null=True)
    fb_link = models.URLField('Facebook Link', help_text='Facebook Link for More', blank=True, null=True)
    ig_link = models.URLField('Instagram Link', help_text='Instagram Link for More', blank=True, null=True)
    twitter_link = models.URLField('Twitter Link', help_text='Twitter Link for More', blank=True, null=True)
    linkedin_link = models.URLField('LinkedIn Link', help_text='LinkedInLink for More', blank=True, null=True)
    hide = models.BooleanField('Hide Item', help_text='Check to hide item', default=False)
    front_image = models.ImageField('Front Image', help_text="Square Image", upload_to='photos/portfolio/', blank=False, null=True)
    img_1 = models.ImageField(upload_to='photos/portfolio/', blank=True, null=True)
    img_2 = models.ImageField(upload_to='photos/portfolio/', blank=True, null=True)
    img_3 = models.ImageField(upload_to='photos/portfolio/', blank=True, null=True)
    img_4 = models.ImageField(upload_to='photos/portfolio/', blank=True, null=True)
    img_5 = models.ImageField(upload_to='photos/portfolio/', blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Portfolio Item'
        verbose_name_plural = 'Portfolio Items'

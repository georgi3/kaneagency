# Generated by Django 4.1 on 2022-09-04 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='content',
            name='fb_link',
            field=models.URLField(blank=True, help_text='Contact Info', null=True, verbose_name='Facebook Link'),
        ),
    ]

# Generated by Django 4.0 on 2024-03-19 17:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_remove_content_about_par_2_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='content',
            name='footer_desc_par_1',
            field=models.TextField(blank=True, help_text='Paragraph 1, Max one sentence', max_length=500, null=True, verbose_name='Footer Short Description 1'),
        ),
    ]

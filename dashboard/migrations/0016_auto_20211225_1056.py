# Generated by Django 3.2.7 on 2021-12-25 05:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0015_auto_20211221_1559'),
    ]

    operations = [
        migrations.AddField(
            model_name='gallery',
            name='year',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='index',
            name='gallery_heading',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='index',
            name='testimonial_heading',
            field=models.TextField(blank=True, null=True),
        ),
    ]

# Generated by Django 3.2.7 on 2021-12-25 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0017_gallery_event'),
    ]

    operations = [
        migrations.AddField(
            model_name='index',
            name='event_heading',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='index',
            name='team_heading',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='index',
            name='vertical_heading',
            field=models.TextField(blank=True, null=True),
        ),
    ]

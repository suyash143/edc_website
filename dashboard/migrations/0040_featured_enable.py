# Generated by Django 3.2.7 on 2022-03-05 05:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0039_rename_url_featured_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='featured',
            name='enable',
            field=models.BooleanField(default=False),
        ),
    ]

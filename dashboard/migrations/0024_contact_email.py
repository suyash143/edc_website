# Generated by Django 3.2.7 on 2022-01-10 04:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0023_event_vertical'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
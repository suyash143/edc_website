# Generated by Django 3.2.5 on 2022-01-13 09:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0029_auto_20220113_1510'),
    ]

    operations = [
        migrations.AddField(
            model_name='index',
            name='startup_heading',
            field=models.TextField(blank=True, null=True),
        ),
    ]

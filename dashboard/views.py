from . import models
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
import os
import pytz
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail

from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.contrib.sessions.models import Session
from django.core import mail
from datetime import date
from django.utils import timezone
from django.db import connection
import datetime
import random
import json

from django.db import transaction


def index(request):
    future_events = models.Event.objects.filter(completed=False,ongoing=False)
    past_events = models.Event.objects.filter(completed=True,ongoing=False)
    ongoing_events = models.Event.objects.filter(completed=False,ongoing=True)
    index = models.Index.objects.all().latest('pk')
    skill = models.Skill.objects.all()
    verticals = models.Vertical.objects.all()
    testimonials = models.Testimonial.objects.all()
    startups = models.Startup.objects.all()
    gallery = models.Gallery.objects.all()
    team = models.Team.objects.all()
    company = models.Company.objects.all()
    try:
        featured = models.Featured.objects.get(enable=True)
    except:
        featured=None
    if request.method == "POST":
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        number = request.POST.get('number')
        email = request.POST.get('email')
        sc, created = models.Contact.objects.get_or_create(name=name, subject=subject, message=message, number=number,
                                                           email=email,
                                                           created=datetime.datetime.now())
        sc.save()


        try:
            email_subject = 'Greetings from Entrepreneurship Development Cell'
            add = models.Index.objects.latest('pk').address
            print(add)
            html_message = render_to_string('email_requester.html',
                                            {'name': name,'address':add})
            plain_message = strip_tags(html_message)
            from_email = settings.EMAIL_HOST_USER
            to = str(email)

            mail.send_mail(email_subject, plain_message, from_email, [to], html_message=html_message)

            print('requester email sent')
        except:
            pass

        try:
            email_subject = '----New Response received on EDC----'
            html_message = render_to_string('email_details.html',
                                            {'name': name, 'subject': subject, 'email': email, 'number': number,
                                             'message': message,'submitted':datetime.datetime.now()})
            plain_message = strip_tags(html_message)
            from_email = settings.EMAIL_HOST_USER
            user_list = User.objects.filter(is_superuser=1)
            to = [x.email for x in user_list]
            print(to)
            mail.send_mail(email_subject, plain_message, from_email, to, html_message=html_message)
        except:
            pass

        return redirect('index')

    return render(request, 'index.html', {'future_events': future_events,'past_events': past_events, 'index': index, 'skill': skill, 'verticals': verticals,
                                          'testimonials': testimonials,'startups': startups, 'gallery': gallery,
                                          'team': team,'company':company,'ongoing_events':ongoing_events, 'featured':featured})


def events(request, **kwargs):
    print(kwargs)
    event = models.Event.objects.get(pk=kwargs.get('pk'))
    index = models.Index.objects.all().latest('pk')

    return render(request, 'event_detail.html', {'event': event, 'index': index})

def team(request, **kwargs):
    print(kwargs)
    team = models.Team.objects.all()
    index = models.Index.objects.all().latest('pk')

    return render(request, 'team.html', {'team': team,'index': index})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            if request.user.is_staff is True:
                return redirect('/dashboard')
            else:
                return redirect('/index')
        else:
            messages.info(request, "invalid Credentials")
            return redirect('login')
    else:
        return render(request, 'login.html')


def logout(request):
    auth.logout(request)
    return redirect('login')


def dashboard(request):
    if request.user.is_staff:
        return render(request, 'dashboard.html')
    else:
        return render(request, '403.html')


def add_link(request):
    if request.user.is_staff:
        if request.method == 'POST' and 'checker' in request.POST:
            key = request.POST.get('test_char')
            try:
                object = models.LinkStorage.objects.get(key=key)
                return render(request, 'add_link.html', {'char_status': False, 'char': key})
            except:
                return render(request, 'add_link.html', {'char_status': True, 'char': key, 'char_true': key})

        if request.method == "POST" and 'link_submit' in request.POST:
            if 'key' in request.POST:
                original_link = request.POST.get('original_link', None)
                link_name = request.POST.get('link_name', None)
                key = request.POST.get('key', None)
                domain = request.build_absolute_uri('/')
                converted_link = domain + f'l/{key}'
                sc, created = models.LinkStorage.objects.get_or_create(name=link_name, link=original_link, key=key,
                                                                       converted_link=converted_link,
                                                                       date_time=datetime.datetime.now())
                sc.save()
                return redirect('link_table')
            else:
                return redirect('add_link')

        return render(request, 'add_link.html')
    else:
        return render(request, '403.html')


def link_table(request):
    objects = models.LinkStorage.objects.all()

    return render(request, 'link_tables.html', {'objects': objects})


def l(request, **kwargs):
    key = kwargs.get('key', None)
    try:
        object = models.LinkStorage.objects.get(key=key)
        object.count += 1
        object.save()
    except:
        return HttpResponse('sorry Bad request')

    return redirect(f'{object.link}')

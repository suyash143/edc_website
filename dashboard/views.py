from . import models
from django.contrib.auth.models import User
from django.http import HttpResponse, JsonResponse
import os
import pytz
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
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
    return render(request,'index.html')


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
        if request.method=='POST' and 'checker' in request.POST:
            key=request.POST.get('test_char')
            try:
                object=models.Storage.objects.get(key=key)
                return render(request,'add_link.html',{'char_status':False,'char':key})
            except:
                return render(request, 'add_link.html', {'char_status': True,'char':key,'char_true':key})

        if request.method=="POST" and 'link_submit' in request.POST:
            if 'key' in request.POST:
                original_link=request.POST.get('original_link',None)
                link_name = request.POST.get('link_name',None)
                key = request.POST.get('key',None)
                domain = request.build_absolute_uri('/')
                converted_link = domain + f'l/{key}'
                sc, created = models.Storage.objects.get_or_create(name=link_name,link=original_link, key=key,
                                                                   converted_link=converted_link,
                                                                   entry=datetime.datetime.now())
                sc.save()
                return redirect('link_table')
            else:
                return redirect('add_link')

        return render(request,'add_link.html')
    else:
        return render(request, '403.html')


def link_table(request):
    objects = models.Storage.objects.all()

    return render(request,'link_tables.html',{'objects':objects})


def l(request,**kwargs):

    key=kwargs.get('key',None)
    try:
        object=models.Storage.objects.get(key=key)
        object.count += 1
        object.save()
    except:
        return HttpResponse('sorry Bad request')
    
    return redirect(f'{object.link}')

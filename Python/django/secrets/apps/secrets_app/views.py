# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Secret

# Create your views here.
def index(request):
    print "SECRET INDEX ROUTE"
    print "*****************"
    print "first name from session:",request.session['first_name']
    print "user id from session:",request.session['user_id']
    # print recent_secret()
    # if 'id' in request.session:

    #pass context once in the index route
    context = {
        'recent_secret': Secret.objects.recent_secret_5(request),
        'secrets': Secret.objects.all(),
        # 'current_user_id': Secret.objects.current_user(request.session.user_id),
        # 'secrets': "THIS IS A HARDCODED SECRET"
    }
    print "context dictionary:", context

    return render(request,'secrets_app/index.html', context)

def new(request):
    print "Secrets Home Route"
    print "*****************"
    if request.method == 'POST':
        print "request.POST:",request.POST
        valid, data = Secret.objects.create_new_secret(request.POST)

        if valid == True:
            print "Added secret to database!"
            print "*********************"
        else:
            for err in data:
                messages.error(request,err)
                return redirect('secret:index')
    else:
        return redirect('auth:index')

    return redirect('secret:index')

def popular(request):
    print "Popular Secrets Route"
    print "*****************"
    context = {
        'secrets': Secret.objects.all(),
    }
    return render(request,'secrets_app/popular.html', context)

def like(request):
    print "Like Secrets Route"
    print "*****************"
    # Secret.objects.like_secret(request)
    if True:
        valid, data = Secret.objects.like_secret(request.POST)

    return redirect('secret:index')

def delete(request):
    print "delete Secrets Route"
    print "*****************"

    return redirect('secret:index')

def logout(request):
    print "logout route"
    print "***********"
    request.session.clear()
    return redirect('auth:index')

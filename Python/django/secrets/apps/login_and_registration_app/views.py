# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
import bcrypt

# Create your views here.
def index(request):
    print "Index route"
    print "***********"

    context = {
        'users': User.objects.all()
    }

    return render(request, 'login_and_registration_app/index.html',context)

def register(request):
    print "Register route"
    print "***********"
    if request.method == 'POST':
        print "request.POST:", request.POST
        #use valid and data to unpack 2 values from tuple
        valid, data = User.objects.validate_and_create(request.POST)

        if valid == True:
            print "Successful registration!"
            print "***********"
        else:
            for err in data:
                messages.error(request,err)
            return redirect('auth:index')

    #save info in session for success page.
    user_info = User.objects.validate_and_login(request.POST)
    request.session['first_name'] = user_info[1].first_name
    request.session['user_id'] = user_info[1].id


    return redirect('secret:index')

def login(request):
    print "Login route"
    print "***********"
    if request.method == 'POST':
        print "request.POST:", request.POST
        print "***********"

        valid, data = User.objects.validate_and_login(request.POST)

        if valid == True:
            print "Successful Login"
            print "***********"
        else:
            for err in data:
                messages.error(request,err)
            return redirect('auth:index')


    #save info in session for success page.
    user_info = User.objects.validate_and_login(request.POST)
    request.session['first_name'] = user_info[1].first_name
    request.session['user_id'] = user_info[1].id
    # print request.user.id
    print "first_name in session:", request.session['first_name']
    print "id in session:",request.session['user_id']

    user_id = request.session['user_id']
    print "THIS IS THE USER ID-------->", user_id


    # print "THIS IS THE NEW SESSION", request.session['user_id']
    return redirect('secret:index')

def logout(request):
    print "logout route"
    print "***********"
    request.session.clear()
    return redirect('auth:index')

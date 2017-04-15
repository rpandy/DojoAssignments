# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from django.contrib import messages
from .models import User
import bcrypt

# Create your views here.
def index(request):
    print "this is the index method"

    context = {
        'users': User.objects.all()
    }
    # User.objects.validate_and_create("rspandy@gmail.com")

    pw = "lost 92 bricks"
    hashed = bcrypt.hashpw(pw.encode(), bcrypt.gensalt())
    print pw, hashed


    return render(request, "validation_app/index.html", context)
    # return HttpResponse(User.userManager.login("rspandy@gmail.com"))

def submit(request):
    print "This is the submit route"
    if request.method == 'POST':
        print "request.POST:",request.POST
        #use valid and data to unpack 2 values from tuple
        valid,data = User.objects.validate_and_create(request.POST)
        # print "response back from our function call:", response_back

        if valid == True:
            print "we're successful"
        else:
            for err in data:
                messages.error(request,err)
            return redirect('/')
    context = {
        'users': User.objects.all()
    }
    #passing data into session in order to display on success page
    request.session['email'] = data.email
    return render(request,"validation_app/success.html", context)
    # return HttpResponse(User.userManager.login("rspandy@gmail.com"))

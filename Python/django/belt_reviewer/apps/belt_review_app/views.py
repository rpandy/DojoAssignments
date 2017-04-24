# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Review

# Create your views here.
def index(request):
    print "INDEX METHOD"
    print "************"

    return render(request, 'belt_review_app/index.html')

def add(request):
    print "ADD METHOD"
    print "************"
    context = {
        'all_reviews': Review.objects.all()
    }
    print context, "<------- CONTEXT"
    return render(request, 'belt_review_app/add.html', context)

def new_review(request):
    print "NEW REVIEW METHOD"
    print "************"
    if request.method == 'POST':
        print "request.POST:",request.POST

        valid, data = Review.objects.create_review(request.POST)

        if valid == True:
            print "Added review to database"
            print "***********************"
        else:
            for err in data:
                messages.error(request,err)
                return redirect('review:add')
    else:
        return redirect('auth:index')

    return redirect('review:index') #send user to page of book review

# # -*- coding: utf-8 -*-
# from __future__ import unicode_literals

from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, 'survey_form_app/index.html')

def survey_process(request):
    #lets figure out what we're getting below
    print ('*'*25)
    print(request.method)
    print(request.POST)
    print ('*'*25)
    print "survey process route"
    #logic here
    #info from form
    request.session['name'] = request.POST['name']
    request.session['location'] = request.POST['location']
    request.session['fav_language'] = request.POST['fav_language']
    request.session['comment'] = request.POST['comment']
    #counter
    request.session['counter'] += 1
    return redirect('/results')

def results(request):
    print ('*'*50)
    print(request.method)
    print ('*'*50)

    return render(request, 'survey_form_app/results.html')

def home(request):
    print ('*'*25)
    print "Go back home"
    print ('*'*25)
    return redirect('/')

def clear(request):
    request.session['counter'] = 0
    return redirect('/')

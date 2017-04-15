# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
import string
import random
# Create your views here.
def index(request):
    if 'count' not in request.session:
        request.session['count'] = 0
    return render(request, 'randomWordApp/index.html')

def generate(request):
    print(request.method)
    if request.method == "POST":
        print('*'*50)
        print(request.POST)
        print('*'*50)
        # request.session['name'] = request.POST['name']
        rando = ''.join(random.choice(string.ascii_uppercase+string.digits) for x in range(16))
        request.session['count'] += 1
        request.session['randomNum'] = rando
        print "random number is:",request.session['randomNum']
        return redirect('/')
    else:
        return redirect('/')

def clear(request):
    print(request.method)
    request.session['count'] = 0
    request.session['randomNum'] = "-"
    return redirect('/')

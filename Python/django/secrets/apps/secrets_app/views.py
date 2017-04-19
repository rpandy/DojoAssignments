# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,'secrets_app/index.html')

def home(request):
    print "Secrets Home Route"
    print "*****************"
    if request.method == 'POST':
        print "request.POST:",request.POST

    pass

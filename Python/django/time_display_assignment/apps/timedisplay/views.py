# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse
import datetime
print "This is the date and time function:"
# Create your views here.
def index(request):
    now = datetime.datetime.now()
    print "This is the date and time function:",now
    context = {
    "somekey": now
    }
    return render(request,'timedisplay/index.html',context)

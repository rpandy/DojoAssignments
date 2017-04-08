# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse
import datetime
now = datetime.datetime.now()
print "This is the date and time function:", now
# Create your views here.
def index(request):
    context = {
    "somekey": now
    }
    return render(request,'timedisplay/index.html',context)

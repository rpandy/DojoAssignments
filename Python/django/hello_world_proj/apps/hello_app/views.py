# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.

#traffic cop or main hub
def index(request):
    print "made it to the index method"
    return render(request, 'hello_app/index.html')

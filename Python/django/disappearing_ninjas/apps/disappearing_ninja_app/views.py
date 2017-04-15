# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
def index(request):
    print ("*"*20)
    print "INDEX ROUTE HIT"
    return render(request, "disappearing_ninja_app/index.html")

def ninjas(request):
    print ("*"*20)
    print "NINJA ROUTE"
    context = {
        'blue':'static/images/leonardo.jpg',
        'purple':'static/images/donatello.jpg',
        'red':'static/images/raphael.jpg',
        'orange':'static/images/michelangelo.jpg'
    }
    return render(request, "disappearing_ninja_app/ninjas.html", context)

def one_ninja(request, color):
    print ("*"*20)
    print "ONE NINJA ROUTE"
    context = {
        'blue':['static/images/leonardo.jpg','Leonardo'],
        'purple':['static/images/donatello.jpg','Donatello'],
        'red':['static/images/raphael.jpg','Raphael'],
        'orange':['static/images/michelangelo.jpg','Michelangelo']
    }

    #psuedo code: if color is not blue, purple, red or orange then redirect to April Sinclair



    return render(request, "disappearing_ninja_app/ninjas.html", context)

# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
import random, time
from datetime import datetime
# time_stamp = time.time()
# time_stamp = datetime.datetime.fromtimestamp(time_stamp).strftime('%Y-%m-%d %H:%M')
print datetime.now()

# Create your views here.
def index(request):
    if 'gold_total' not in request.session:
        request.session['gold_total'] = 0
        # request.session['time'] = 0
        request.session['activities_list'] = []
    return render(request, 'ninja_gold_app/index.html')

def process_farm(request):
    #if no farm gold in session then we create it
    if 'farm_gold' not in request.session:
        request.session['farm_gold'] = 0
        request.session['location'] = 'farm'

    random_gold_farm = random.randrange(10,20+1)
    #save info to session to pass to html

    #adding to gold total
    request.session['gold_total'] += random_gold_farm
    print "this is the gold total:",request.session['gold_total']

    activities = {
        'gold':random_gold_farm,
        'time': str(datetime.now().strftime('%Y-%m-%d %H:%M')),
        'location': "farm",
        'win_loss_found':"found"

        }

    print"activities:", activities
    # request.session['activities_list'].append(request.session['activities'])
    request.session['activities_list'].append(activities)
    print request.session['activities_list']

    return redirect('/')

def process_cave(request):
    #if no farm gold in session then we create it
    if 'cave_gold' not in request.session:
        request.session['cave_gold'] = 0
        request.session['location'] = 'cave'

    random_gold_cave = random.randrange(5,10+1)

    #adding to gold total
    request.session['gold_total'] += random_gold_cave
    print "this is the gold total:",request.session['gold_total']

    activities = {
        'gold':random_gold_cave,
        'time': str(datetime.now().strftime('%Y-%m-%d %H:%M')),
        'location': "cave",
        'win_loss_found':"found"

        }

    print"activities:", activities
    # request.session['activities_list'].append(request.session['activities'])
    request.session['activities_list'].append(activities)
    print request.session['activities_list']

    return redirect('/')

def process_house(request):
    #if no house gold in session then we create it
    if 'house_gold' not in request.session:
        request.session['house_gold'] = 0
        request.session['location'] = 'house'

    random_gold_house = random.randrange(2,5+1)

    #adding to gold total
    request.session['gold_total'] += random_gold_house
    print "this is the gold total:",request.session['gold_total']

    activities = {
        'gold':random_gold_house,
        'time': str(datetime.now().strftime('%Y-%m-%d %H:%M')),
        'location': "house",
        'win_loss_found':"found"
        }

    print"activities:", activities
    # request.session['activities_list'].append(request.session['activities'])
    request.session['activities_list'].append(activities)
    print request.session['activities_list']

    return redirect('/')

def process_casino(request):

    random_gold_casino = random.randrange(-50,50+1)

    #adding to gold total
    request.session['gold_total'] += random_gold_casino
    print "this is the gold total:",request.session['gold_total']

    if random_gold_casino < 0:
        activities = {
            'gold':random_gold_casino,
            'time': str(datetime.now().strftime('%Y-%m-%d %H:%M')),
            'location': "casino",
            'win_loss_found':"lost"
            }
    elif random_gold_casino > 0:
        activities = {
            'gold':random_gold_casino,
            'time': str(datetime.now()),
            'location': "casino",
            'win_loss_found':"won"
            }

    print"activities:", activities
    # request.session['activities_list'].append(request.session['activities'])
    request.session['activities_list'].append(activities)
    print request.session['activities_list']
    return redirect('/')

def clear(request):
    request.session['gold_total'] = 0
    request.session['activities_list'] = []
    return redirect('/')

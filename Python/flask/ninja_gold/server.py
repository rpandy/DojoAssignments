from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'SECRETSSSSSSSS'
import random, time, datetime

#
time_stamp = time.time()
print time_stamp
time_stamp = datetime.datetime.fromtimestamp(time_stamp).strftime('%Y-%m-%d %H:%M')
print time_stamp

@app.route('/')
def index():
    #check to see if gold total is saved in session already
    if 'gold_total' not in session:
        session['gold_total'] = 0
        session['activities_list'] = []
        session['activities_list_cave'] = []
        session['activities_list_house'] = []
        session['activities_list_casino'] = []

    print "Index route for Ninja Gold"

    return render_template('index.html')


@app.route('/process_farm', methods=['POST'])
def farm():
    #generate random numbers
    random_gold_farm = random.randrange(10,20+1)
    random_gold_house = random.randrange(2,5+1)
    random_gold_casino = random.randrange(-50,50+1)
    #check to see if farm is saved in session already
    #if not then we set it to 0
    # time_stamp = datetime.datetime.fromtimestamp(time_stamp).strftime('%Y-%m-%d %H:%M')
    if 'farm_gold' not in session:
        session['farm_gold'] = 0
        session['location'] = 'farm - '
        session['time'] = time_stamp
        session['counter'] = 0
        session['string'] = "pieces of gold found on the"

    #set session['farm_gold'] to the random number previously generated
    session['farm_gold'] = random_gold_farm
    # print 'farm', session['farm_gold']

    #create a list of dictionaries
    activities = {
        'farm_gold': session['farm_gold'],
        'location': session['location'],
        'time': session['time'],
        'id': session['counter'],
        'string': session['string']
    }

    #set session['farm'] to the random number previously generated
    session['activities_list'].append(activities)
    #session.clear()
    print session['activities_list']
    #added to gold total
    session['gold_total'] += session['farm_gold']

    #append to activities display
    session['activities'] = "you earned",session['farm_gold'],"on the farm!"
    # session['activities_list'].append(random_gold_farm)
    print session['activities_list']
    session['counter'] += 1
    return redirect('/')

@app.route('/process_cave', methods=['POST'])
def cave():
    #generate random numbers
    random_gold_cave = random.randrange(5,10+1)
    #check to see if farm is saved in session already
    #if not then we set it to 0
    if 'cave_gold' not in session:
        session['cave_gold'] = 0
        session['location'] = 'cave - '
        session['time'] = time_stamp
        session['counter'] = 0
        session['string'] = "pieces of gold found in the"

    #set session['cave_gold'] to the random number previously generated
    session['cave_gold'] = random_gold_cave

    #create a list of dictionaries
    activities_cave = {
        'cave_gold': session['cave_gold'],
        'location': session['location'],
        'time': session['time'],
        'id': session['counter'],
        'string': session['string']
    }

    #set session['cave] to the random number previously generated
    session['activities_list_cave'].append(activities_cave)
    #session.clear()
    print session['activities_list_cave']
    #added to gold total
    session['gold_total'] += session['cave_gold']

    #append to activities display
    session['activities'] = "you earned",session['cave_gold'],"in the cave!"
    # session['activities_list'].append(random_gold_farm)
    print session['activities_list']
    session['counter'] += 1
    return redirect('/')


@app.route('/process_house', methods=['POST'])
def house():
    #generate random numbers
    random_gold_house = random.randrange(2,5+1)
    #check to see if house is saved in session already
    #if not then we set it to 0
    if 'house_gold' not in session:
        session['house_gold'] = 0
        session['location'] = 'house - '
        session['time'] = time_stamp
        session['counter'] = 0
        session['string'] = "pieces of gold found in the"

    #set session['house_gold'] to the random number previously generated
    session['house_gold'] = random_gold_house

    #create a list of dictionaries
    activities_house = {
        'house_gold': session['house_gold'],
        'location': session['location'],
        'time': session['time'],
        'id': session['counter'],
        'string': session['string']
    }

    #set session['house] to the random number previously generated
    session['activities_list_house'].append(activities_house)
    #session.clear()
    print session['activities_list_house']
    #added to gold total
    session['gold_total'] += session['house_gold']

    #append to activities display
    session['activities'] = "you earned",session['house_gold'],"in the house!"
    # session['activities_list'].append(random_gold_farm)
    print session['activities_list']
    session['counter'] += 1
    return redirect('/')

@app.route('/process_casino', methods=['POST'])
def casino():
    #generate random numbers
    random_gold_casino = random.randrange(-50,50+1)
    #check to see if casino is saved in session already
    #if not then we set it to 0 along with o

    if 'casino_gold' not in session:
        session['casino_gold'] = 0
        session['location'] = 'casino - '
        session['time'] = time_stamp
        session['counter'] = 0
        # session['string'] = "pieces of gold earned in the"

    #set session['house_gold'] to the random number previously generated
    session['casino_gold'] = random_gold_casino

    if session['casino_gold'] < 0:
        session['string'] = 'pieces of gold lost in the'
        session['location'] = 'casino!! WHOOPS!!! - '
    else:
        session['string'] = 'pieces of gold earned in'
        session['location'] = 'casino!! Time to retire!!! - '
    #create a list of dictionaries
    activities_casino = {
        'casino_gold': session['casino_gold'],
        'location': session['location'],
        'time': session['time'],
        'id': session['counter'],
        'string': session['string']
    }

    #set session['house] to the random number previously generated
    session['activities_list_casino'].append(activities_casino)
    #session.clear()
    print session['activities_list_casino']
    #added to gold total
    session['gold_total'] += session['casino_gold']

    #append to activities display
    session['activities'] = "you earned",session['casino_gold'],"in the house!"
    # session['activities_list'].append(random_gold_farm)
    print session['activities_list']
    session['counter'] += 1
    return redirect('/')

# app.route('/process_money/<id>', methods=['POST'])
# def locale(user):
#     location = session['activities_list']['id']
#     print 'location variable ID is', location
#     return render_template("/process_money.html", user=user)

@app.route('/clear')
def clear():
    session.clear()
    return redirect('/')
app.run(debug=True)

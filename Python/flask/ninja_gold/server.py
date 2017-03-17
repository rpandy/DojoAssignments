from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'SECRETSSSSSSSS'
import random

@app.route('/')
def index():
    #check to see if gold total is saved in session already
    if 'gold_total' not in session:
        session['gold_total'] = 0
        total = session['gold_total']
        print 'gold total is', total
    if 'activities' not in session:
        session['activities'] = []
        print session['activities']

    return render_template('index.html')
@app.route('/process_farm', methods=['POST'])
def farm():
    #generate random number from 10-20
    random_gold_farm = random.randrange(10,20+1)
    #check to see if farm is saved in session already
    #if not then we set it to 0
    if 'farm' not in session:
        session['farm'] = 0
        session['activities_list'] = []
    #set session['farm'] to the random number previously generated
    session['farm'] = random_gold_farm
    print 'farm', session['farm']
    #session.clear()

    #added to gold total
    session['gold_total'] += session['farm']

    #append to activities display
    session['activities'] = "you earned",session['farm'],"on the farm!"
    session['activities_list'].append(random_gold_farm)
    print session['activities_list']
    return redirect('/')

@app.route('/process_cave', methods=['POST'])
def cave():
    #import random
    random_gold_cave = random.randrange(5,10+1)
    if 'cave' not in session:
        session['cave'] = 0
        session['cave'] = random_gold_cave
    print 'cave', session['cave']
    #session.clear()

    session['gold_total'] += session['cave']

    session['activities'] = "you earned",session['cave'],"in the farm!"

    return redirect('/')

@app.route('/process_house', methods=['POST'])
def house():
    #import random
    random_gold_house = random.randrange(2,5+1)
    if 'house' not in session:
        session['house'] = 0
    session['house'] = random_gold_house
    print 'house', session['house']
    #session.clear()

    session['gold_total'] += session['house']

    session['activities'] = "you earned",session['house'],"in the house!"
    return redirect('/')

@app.route('/process_casino', methods=['POST'])
def casion():
    #import random
    random_gold_casino = random.randrange(-50,50+1)
    if 'casino' not in session:
        session['casino'] = 0
    session['casino'] = random_gold_casino
    print 'casino', session['casino']
    #session.clear()

    session['gold_total'] += session['casino']

    session['activities'] = "you earned",session['casino'],"in the casino!"

    return redirect('/')

@app.route('/clear')
def clear():
    session.clear()
    return redirect('/')
app.run(debug=True)

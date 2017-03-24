#import necessary dependencies from flask
from flask import Flask, render_template, request, redirect, session

app=Flask(__name__)

app.secret_key = "SECRETSSSS"

#remember to add decorator (@) to route.
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninjas')
def ninjas():
    #create dictionary of items to loop through on template.
    #REMEMBER - commas between key/value pairs in dictionary.
    ninjas = {
    'blue': 'images/leonardo.jpg', #value should be the full string you want to use
    'purple': 'images/donatello.jpg',
    'red': 'images/raphael.jpg',
    'orange': 'images/michelangelo.jpg'
    }
    return render_template('ninjas.html', ninjas=ninjas) #pass ninjas dictionary into jinja templating engine

@app.route('/ninjas/<color>')
def one_ninja(color):
    ninjas = {
    'blue': ['images/leonardo.jpg', 'Leonardo'],
    'purple': ['images/donatello.jpg', 'Donatello'],
    'red': ['images/raphael.jpg', 'Raphael'],
    'orange': ['images/michelangelo.jpg', 'Michelangelo']
    }
    if color in ninjas:
        turtle = {
        'img': ninjas[color][0],
        'color': color,
        'name':ninjas[color][1]
        }
    else:
        turtle = {
        'img':'images/notapril.jpg'
        }
    return render_template('ninjas.html', turtle=turtle)

app.run(debug='True', port=8000)

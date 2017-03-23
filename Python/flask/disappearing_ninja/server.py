from flask import Flask, render_template, request, redirect, session

app=Flask(__name__)

app.secret_key = "SECRETSSSS"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninja')
def ninjas():
    # create dictionary of characters
    ninjas = {
    'blue': 'images/leonardo.jpg', #use full img link in dictionary instead of just turtle name
    'purple': 'images/donatello.jpg',
    'red': 'images/raphael.jpg',
    'orange': 'images/michelangelo.jpg'
    }
    return render_template('ninja.html', ninjas=ninjas) # pass ninjas dictionary to jinja

#use the <color> variable to specify specific character
@app.route('/ninja/<color>')
def one_ninja(color): # <-- pass variable into function

# if statements to determine which character shows up given the color route
    ninjas = {
    "blue": ['images/leonardo.jpg', 'Leonardo'],
    "purple":['images/donatello.jpg','Donatello'],
    "red":['images/raphael.jpg','Raphael'],
    "orange":['images/michelangelo.jpg','Michelangelo']
    }

    if color in ninjas:
        turtle = {
            'img': ninjas[color][0],
            'color': color,
            'name': ninjas[color][1]
        }
    else:
        turtle = {
            'img': 'images/notapril.jpg'
        }
    return render_template('ninja.html', turtle=turtle)

app.run(debug=True)

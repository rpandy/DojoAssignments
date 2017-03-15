from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'SECRET'

#generate random number.
#Do this before the index route so a new number isnt generated after every refresh
import random
random_number = random.randrange(1,101)

@app.route('/')
def index():
    #import random
    #random_number = random.randrange(0,101)
    #print random_number
    session['random'] = random_number
    print 'the randomly generated number is:', session['random']


    return render_template('index.html', random = session['random'])


@app.route('/', methods=['POST'])
def guess_submission():
    #print request.form
    session['guess'] = request.form['guess']
    print 'the guess is:', session['guess']
    #guess will not print in HTML doc because it is a POST request
    return redirect('/')


#create another route that runs function after guess is submitted
@app.route('/test')
def test_logic():
    print 'random is', session['random']
    print 'guess is', session['guess']

    if session['random'] > session['guess']:
        print session['random'], 'is greater than', session['guess']
    elif session['random'] < session['guess']:
        print session['random'], 'is less than', session['guess']
    return redirect('/')
#if statement comparing the guess to session['random']

app.run(debug=True)

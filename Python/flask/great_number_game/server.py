from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'SECRET'

#generate random number.
#Do this before the index route so a new number isnt generated after every refresh
import random
random_number = random.randrange(1,101)


@app.route('/')
def index():
    #print random_number
    session['random'] = random_number
    #print 'the randomly generated number is:', session['random']

    return render_template('index.html', random = session['random'])


@app.route('/', methods=['POST'])
def guess_submission():
    #print request.form
    # session['guess'] = 0
    session['guess'] = request.form['guess']
    #guess = session['guess']
    print 'the guess is:', session['guess']
    print 'the randomly generated number is:', session['random']

    return redirect('/')


#create another route that runs function after guess is submitted
@app.route('/test')
def test_logic():
    print 'random is', session['random']
    print 'guess is', session['guess']
    #print 'answer is', session ['answer']
    random = session['random']
    guess = session['guess']

    if random < guess:
        print 'random < guess'
    elif random > guess:
        print 'random > guess'
    else:
        print 'random = guess'

    # if random < guess:
    #     session['answer'] = 'guess is too high'
    #     print session['answer']
    # elif random > guess:
    #     session['answer'] = 'guess is too low'
    #     print session['answer']
    return redirect('/')
#if statement comparing the guess to session['random']
@app.route('/clear')
def clear():
    session.clear()
    #guess is set to 0 after session is cleared
    session['guess'] = 0
    return redirect('/')
app.run(debug=True)

from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'SECRET'

@app.route('/') #route listener for index
#get request comes from the local host
def index():
    #we run an if statement to check and see if the variable counter exists in the counter dictionary.
    #if it does we increment by 1. if it doesnt we set to one
    # if 'counter' in [session]:
    #     session['counter'] += 1
    # else:
    #     session['counter'] = 1
    try:
        session['counter'] += 1
    except:
        session['counter'] = 1
    return render_template('index.html') #index is rendered
#function to reset the counter
@app.route('/clear')
def clear():
    session.clear()
    return redirect('/')

@app.route('/addTwo')
def addTwo():
    # only added 1 extra tick because counter will be
    # incremented automatically following the redirect.
    session['counter'] += 1
    return redirect('/')

app.run(debug=True, port=8000)

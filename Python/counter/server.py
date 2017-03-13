from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)

app.secret_key = 'SECRET'

@app.route('/')
#code below is looking into the session dictionary for a variable named counter.
#if it finds counter then it adds 1 to it
#if it doesnt find counter then it sets it to 1.
def index():
    try:
        session['counter'] += 1
    except:
        session['counter'] = 1
#or a more pythonic way. a if statement that checks to see if there is a counter key in session. if not it
    # if 'counter' in session:
    #     session['counter'] += 1
    # else:
    #     session['counter'] = 1
    # return render_template('index.html')

app.run(debug=True, port=8000)

    # for count in range(counter_num, times):
    #     print count

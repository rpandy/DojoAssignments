# Import Flask to allow us to create our app, and import
# render_template to allow us to render index.html.
from flask import Flask, render_template, request, redirect, session, flash
# Global variable __name__ tells Flask whether or not we
# are running the file directly or importing it as a module.
import re
app = Flask(__name__)
app.secret_key = "I<3Secrets"

#first part is checking for allowable characters.
#when regex uses the period its seen as a specialized character. This is done with backslash "\"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]*$')
NAME_REGEX = re.compile(r'^[a-zA-Z]{2,}$')

#each route should do one thing.
#Either post information or gather information to send elsewhere
# The "@" symbol designates a "decorator" which attaches the
# following function to the '/' route. This means that
# whenever we send a request to localhost:5000/ we will run the following function
@app.route('/')
def index():
    if "counter" not in session:
        session['counter'] = 0
        session['name_list'] = []
    print "Im in my route for index!"
    age = 33
    job = "who knows"
    #name you expect variable to be on template and what the variable will be equal to

    # Render the template and return it!
    return render_template('index.html',age = age, job=job)

@app.route('/users', methods = ["POST"])
def new_user():
    # if len(request.form['first_name']) == 0:
    #keep an error count
    #LOOPING THROUGH A DICTIONARY
    print request.form
    for key in request.form:
        print "they key is", key, "and the value is", request.form[key]
    errors = 0
    if not NAME_REGEX.match(request.form['first_name']):
        flash('FILL ME IN! I need a name!')
        errors += 1
    if not EMAIL_REGEX.match(request.form['email']):
        flash("email must be a valid email")
        errors+=1
    if errors:
        return redirect('/')
    #another way to check for flash errors/ validation!
    #if '_flashes' in session:
        #return redirect
    print request.form["first_name"]
    print request.form['id']
    user = {
        'first_name': request.form['first_name'],
        'email': request.form['email'],
        'id': session['counter']
    }

    session['name_list'].append(user) #creating a list of dictionaries
    session['first_name'] = request.form['first_name']
    session['counter'] += 1
    return redirect('/success')

@app.route('/success')
def showUser():
    print "in sucess route", session['name_list']
    return render_template('success.html')

@app.route('/user/<user_id>')
def one_user(user_id): #passing in the variable (user_id). Looking for a route parameter
    user = session['name_list'][int(user_id)]
    print user
    return render_template("/oneuser.html", user = user)

@app.route("/clear")
def clear_session():
    session.clear()
    return redirect('/')
app.run(debug='True', port=8000)

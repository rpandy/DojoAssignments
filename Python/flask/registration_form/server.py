from flask import Flask, render_template, redirect, request, session, flash
import re

#regex objects for validation
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
NAME_REGEX = re.compile(r'^[a-zA-Z]*$')
PASSWORD_LENGTH = re.compile(r'^.{,8}$')
app = Flask(__name__)
app.secret_key = "SECRETSSSSS"

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def form_submission():
    #Validation - fields cannot be empty
    print request.form
    errors = 0
    if len(request.form['email']) < 1:
        print "testing testing"
        flash("Email field cannot be empty")
        errors += 1
    if len(request.form['first_name']) < 1:
        flash("First Name field cannot be empty")
        errors += 1
    if len(request.form['last_name']) < 1:
        flash("Last Name field cannot be empty")
        errors += 1
    if len(request.form['password']) < 1:
        flash("Password field cannot be empty")
        errors += 1
    if len(request.form['password_confirmation']) < 1:
        flash("Password Confirmation field cannot be empty")
        errors += 1
    #validation - First and Last name fields must contain only letters.
    #REGEX object above.

    if not(NAME_REGEX.match(request.form['first_name'])):
        flash("First Name field must contain letters only")
        errors += 1
    if not(NAME_REGEX.match(request.form['last_name'])):
        flash("Last Name field must contain letters only")
        errors += 1

    #validation - email should be a valid email address
    if not EMAIL_REGEX.match(request.form['email']):
        flash('Invalid email address')
        errors +=1

    #validation - password should be no longer than 8 characters
    if not PASSWORD_LENGTH.match(request.form['password']):
        flash('Password should not be longer than 8 characters')

    #validation - Password and Password Confirmation should match
    if not request.form['password'] == request.form['password_confirmation']:
        flash('Password & Password Confirmation do not match')

    if errors:
        #print "ERROR STATEMENT WORKS"
        return redirect('/')


    return redirect('/')
app.run(debug=True, port=8000)

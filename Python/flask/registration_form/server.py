from flask import Flask, render_template, redirect, request, session, flash
import re

#regex objects for validation
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
NAME_REGEX = re.compile(r'^[a-zA-Z]*$')
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
    if not(NAME_REGEX.match(request.form['last_name'])):
        flash("Last Name field must contain letters only")

    




    # if errors:
    #     return redirect('/')



    return redirect('/')
app.run(debug=True, port=8000)

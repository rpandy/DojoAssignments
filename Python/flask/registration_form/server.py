from flask import Flask, render_template, redirect, request, session, flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
app = Flask(__name__)
app.secret_key = "SECRETSSSSS"

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def form_submission():
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
    return redirect('/')
app.run(debug=True, port=8000)

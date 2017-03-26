from flask import Flask, request,redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt

import re #dont forget to import re for validation
app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = "SEEEECRETTTS" # dont forget secret key w/ flash and session
mysql = MySQLConnector(app,'users_login_and_registration')


#for email validation
EMAIL_REGEX =re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
LETTERS_ONLY = re.compile(r'[A-Za-z]')


@app.route('/')
def index():
    users = mysql.query_db("SELECT * FROM users")
    # print users
    print "email is ",session['users_login_and_registration']['email']

    return render_template('index.html', all_users = users)

@app.route('/users', methods=['POST'])
def validateUserRegistration():
    errors = 0
    #validate first name (2+ char/ Letters only/ cannot be empty)
    if len(request.form['first_name']) < 2:
        flash("First Name must be at least 2 characters")
        errors+=1
    if len(request.form['first_name']) < 1:
        flash("First Name cannot be empty")
        errors+=1
    if not LETTERS_ONLY.match(request.form['first_name']):
        flash("First Name must contain letters only")
        errors+=1
    #validate last name (2+ char/ Letters only/ cannot be empty)
    if len(request.form['last_name']) < 2:
        flash("Last Name must be at least 2 characters")
        errors+=1
    if len(request.form['last_name']) < 1:
        flash("Last Name cannot be empty")
        errors+=1
    if not LETTERS_ONLY.match(request.form['first_name']):
        flash("Last Name must contain letters only")
        errors+=1
    #validate email (valid email format/ cannot be empty)
    if len(request.form['email']) < 1:
        flash("Email cannot be empty")
        errors+=1
    if not EMAIL_REGEX.match(request.form['email']):
        flash("Not a valid email address")
        errors+=1
    #validate password (at least 8 characters/ cannot be empty)
    if len(request.form['password']) < 8:
        flash("Password must be at least 8 characters long")
        errors+=1
    if len(request.form['email']) < 1:
        flash("Password cannot be empty")
        errors+=1
    #validate password confirmation(match password)
    if request.form['password'] != request.form['password_confirmation']:
        flash("Passwords do not match")
    if errors:
        return redirect('/success')

    #INSERT W/ SQL Query
    add_user_query = "INSERT INTO users (first_name, last_name, email, created_at, updated_at) VALUES (:first_name, :last_name, :email, now(), now())"

    user_data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email'],
    }

    session['users_login_and_registration'] = user_data

    mysql.query_db(add_user_query,user_data)
    return redirect('/success')


@app.route('/success')
def registered_user():
    all_users = mysql.query_db('SELECT * FROM users')
    return render_template('success.html', all_users = all_users)
app.run(debug=True, port=8000)

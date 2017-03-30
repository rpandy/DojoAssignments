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
    users = mysql.query_db("SELECT first_name, last_name FROM users")
    # print users
    # print "email is ",session['users_login_and_registration']['email']

    return render_template('index.html',login = users)

@app.route('/registration')
def showRegistration():
    users = mysql.query_db("SELECT first_name last_name FROM users")
    return render_template('index.html', registration = users)


@app.route('/login')
def showLogin():
    users = mysql.query_db("SELECT first_name FROM users")
    return render_template('index.html', login = users)

@app.route('/create_user', methods=['POST'])
def validateUserRegistration():
    #check to see if email already exists in the system
    user_query = "SELECT id FROM users WHERE email = :email"
    user_data = {
        'email': request.form['email']
    }
    userExists = mysql.query_db(user_query,user_data)

    if userExists:
        flash("Email address is invalid. Please use another address")


    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    password = request.form['password']

    errors = 0
    #validate first name (2+ char/ Letters only/ cannot be empty)
    if len(first_name) < 2:
        flash("First Name must be at least 2 characters")
        errors+=1
    if not LETTERS_ONLY.match(first_name):
        flash("First Name must contain letters only")
        errors+=1
    #validate last name (2+ char/ Letters only/ cannot be empty)
    if len(last_name) < 2:
        flash("Last Name must be at least 2 characters")
        errors+=1
    if not LETTERS_ONLY.match(last_name):
        flash("Last Name must contain letters only")
        errors+=1
    #validate email (valid email format/ cannot be empty)
    if not EMAIL_REGEX.match(email):
        flash("Not a valid email address")
        errors+=1
    #validate password (at least 8 characters/ cannot be empty)
    if len(password) < 8:
        flash("Password must be at least 8 characters long")
        errors+=1
    #validate password confirmation(match password)
    if request.form['password'] != request.form['password_confirmation']:
        flash("Passwords do not match")
    if errors:
        return redirect('/registration')

    pw_hash = bcrypt.generate_password_hash(password)

    #INSERT W/ SQL Query
    add_user_query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :pw_hash, now(), now())"

    user_data = {
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'pw_hash': pw_hash
    }
    newUserId = mysql.query_db(add_user_query,user_data)
    print bcrypt.check_password_hash(pw_hash,password)
    # we dont want to save the entire user_data object into session because it contains the password and doesnt have the user id
    session['users_login_and_registration'] = user_data
    return redirect('/success')

@app.route('/login', methods=['POST'])
def login():

    email = request.form['email']
    password = request.form['password']
    errors = 0
    if len(request.form['password']) < 1:
        # print "TEST IF STATEMENT"
        flash("Valid password must be entered")
        errors += 1
    if len(request.form['email']) < 1:
        # print "TEST IF STATEMENT"
        flash("Valid email must be entered")
        errors +=1
    if errors:
        return redirect('/login')

    login_query = "SELECT * FROM users WHERE email = :email LIMIT 1"
    login_data = {'email':email }
    user = mysql.query_db(login_query,login_data)
    print "this is the login query:", mysql.query_db(login_query,login_data)
    all_users = mysql.query_db('SELECT first_name, last_name, email FROM users')
    if bcrypt.check_password_hash(user[0]['password'],password):
        # print "TEST TEST"
        return redirect('/success')
    else:
        flash("Incorrect login info: Email and password combination does not match")
        return redirect('/login')

@app.route('/success')
def registered_user():
    all_users = mysql.query_db('SELECT first_name, last_name, email FROM users')
    return render_template('success.html', all_users = all_users)

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

app.run(debug=True, port=8000)

#import proper dependencies
from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt

import re #needed for validation
app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = "SEEEECRETTTS"
mysql = MySQLConnector(app, 'the_wall')

#validation
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
LETTERS_ONLY = re.compile(r'[A-Za-z]')

@app.route('/')
def index():
    users = mysql.query_db("SELECT * FROM users")
    print "this is the index route"
    print "users dictionary:", users
    return render_template('index.html', login = users) #DOUBLE CHECK

@app.route('/registration')
def showRegistration():
    users = mysql.query_db("SELECT * FROM users")
    return render_template('index.html', registration = users)

@app.route('/login') #show login form on index.html
def showLogin():
    users = mysql.query_db("SELECT * FROM users")
    return render_template('index.html', login = users)

@app.route('/create_user', methods=['POST'])
def newUser():
    #set request_form values to easy variables
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    password = request.form['first_name']

    #registration validation
    errors = 0
    #validate first name (letters only/ cannot be empty)
    if len(request.form['first_name']) < 1:
        flash("First Name field cannot be empty")
        errors += 1
    if not LETTERS_ONLY.match(request.form['first_name']):
        flash("First Name must contain letters only")
        errors += 1

    #validate last name (letters only/ cannot be empty)
    if len(request.form['last_name']) < 1:
        flash("Last Name field cannot be empty")
        errors += 1
    if not LETTERS_ONLY.match(request.form['last_name']):
        flash("Last Name must contain letters only")
        errors += 1

    #validate email address (cannot be empty/ must be valid email format)
    if len(request.form['email']) < 1:
        flash("Email field cannot be empty")
        errors += 1
    if not EMAIL_REGEX.match(request.form['email']):
        flash("Not a valid email")
        errors += 1

    #validate password (>8 characters/ cannot be empty)
    if len(request.form['password']) < 8:
        flash("Password must exceed 8 characters")
        errors += 1
    if len(request.form['password']) < 1:
        flash("Password field cannot be empty")
        errors += 1

    #validate password confirmation (must match password field)
    if request.form['password'] != request.form['password_confirmation']:
        flash("Password fields do not match")
        errors += 1

    #if there are any errors redirect user to /registration page
    if errors:
        return redirect('/registration')

    #encrypt password via Bcrpyt
    pw_hash = bcrypt.generate_password_hash(password)

    #insert new user into user table via SQL
    #pass pw_hash variable into table as encrypted password
    insert_user_query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES(:first_name, :last_name, :email, :pw_hash, now(), now())"

    insert_user_data = {
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'pw_hash': pw_hash #encrypted variable
    }

    print "is bcrypt working???", bcrypt.check_password_hash(pw_hash,password)

    #save insert_user_data to session
    session['the_wall'] = insert_user_data

    #function to run SQL query
    mysql.query_db(insert_user_query,insert_user_data)
    return redirect('/the_wall')

@app.route('/login', methods=['POST'])
def login():

    email = request.form['email']
    password = request.form['password']

    #login validation
    errors = 0

    #validate password (cannot be empty)
    if len(request.form['password']) < 1:
        flash("Password field cannot be empty")
        errors += 1

    #validate email address (cannot be empty/ must be valid email format)
    if len(request.form['email']) < 1:
        flash("Email field cannot be empty")
        errors += 1
    if not EMAIL_REGEX.match(request.form['email']):
        flash("Not a valid email")
        errors += 1
    #if there are any errors redirect user to /login page
    if errors:
        return redirect('/login')
    #if validation is successful complete login via else statement
    else:
        select_user_query = "SELECT * FROM users WHERE email = :email LIMIT 1"

        select_user_data = {'email': email }

        user = mysql.query_db(select_user_query, select_user_data)
        print "login query:", mysql.query_db(select_user_query, select_user_data)

        all_users = mysql.query_db('SELECT * FROM users')
        print "password:", user[0]['password']
        user_pw = user[0]['password']
        print user_pw
        if bcrypt.check_password_hash(user_pw,password):
            print "test test"
            return redirect('/the_wall')
        else:
            flash("Incorrect login info: Email and password combination does not match")
            return redirect('/login')

@app.route('/the_wall')
def wall_activity():
    all_users = mysql.query_db('SELECT * FROM users')
    return render_template('the_wall.html', all_users = all_users)

app.run(debug=True) #leave at default port 5000

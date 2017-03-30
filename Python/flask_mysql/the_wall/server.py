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
    users = mysql.query_db("SELECT first_name FROM users")
    # print "this is the index route"
    # print "users dictionary:", users
    return render_template('index.html', login = users)

# @app.route('/the_wall')
# def showWall():
#     users = mysql.query_db("SELECT first_name FROM users")
#     render_template('the_wall.html', users=users)

@app.route('/create_user', methods=['POST'])
def newUser():

    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    password = request.form['password']
    pw_conf = request.form['password_confirmation']

    #check if email has already been registered
    check_user_query = "SELECT id FROM users WHERE email = :email"
    check_user_data = {
        'email': email
    }
    userExists = mysql.query_db(check_user_query, check_user_data)
    print "Does this user exist? userExists query says:", userExists
    if userExists:
        flash("Email address is invalid. Please use another address.")
        return redirect('/')
    #set request_form values to easy variables

    #registration validation
    errors = 0
    #validate first name (letters only/ cannot be empty)
    if len(first_name) < 2:
        flash("First Name must have at least 2 characters")
        errors += 1
    if not LETTERS_ONLY.match(first_name):
        flash("First Name must contain letters only")
        errors += 1
    #validate last name (letters only/ cannot be empty)
    if len(last_name) < 2:
        flash("Last Name must have at least 2 characters")
        errors += 1
    if not LETTERS_ONLY.match(last_name):
        flash("Last Name must contain letters only")
        errors += 1
    #validate email address (cannot be empty/ must be valid email format)
    if not EMAIL_REGEX.match(email):
        flash("Not a valid email")
        errors += 1
    #validate password (>8 characters/ cannot be empty)
    if len(password) < 8:
        flash("Password must exceed 8 characters")
        errors += 1

    #validate password confirmation (must match password field)
    if password != pw_conf:
        flash("Password fields do not match")
        errors += 1
    #if there are any errors redirect user back to index page
    if errors:
        return redirect('/')
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
    if len(password) < 1:
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
    all_users = mysql.query_db('SELECT first_name FROM users')
    return render_template('the_wall.html', all_users = all_users)

app.run(debug=True) #leave at default port 5000









# @app.route('/registration')
# def showRegistration():
#     users = mysql.query_db("SELECT first_name FROM users")
#     return render_template('index.html', registration = users)
#
# @app.route('/login')
# def showLogin():
#     users = mysql.query_db("SELECT first_name FROM users")
#     # print "this is the index route"
#     # print "users dictionary:", users
#     return render_template('index.html', login = users)
#
# @app.route('/user', methods=['POST'])
# def log_reg():
#     #check the form names to see if we're registering or logging in.
#     #REGISTRATION
#     #variables for request_form
#     first_name = request.form['first_name']
#     last_name = request.form['last_name']
#     email = request.form['email']
#     password = request.form['password']
#
#     #differentiate between which form to show. Show Registration form
#     if "register" in request.form:
#         user_query = "SELECT id FROM users WHERE email = :email"
#         user_data = {
#             'email': email
#         }
#         #check to see if the user already exists
#         userExists = mysql.query_db(user_query, user_data)
#         print "this is the if userExists query", userExists
#
#         #if there is a value in user exists then email is already in system
#         if userExists:
#             flash("Email address is invalid. Please use another address")
#         else:
#             if not EMAIL_REGEX.match(email):
#                 flash("Email must be a valid email")
#             if len(first_name) < 2:
#                 flash("First Name must be longer than two characters")
#             if len(last_name) < 2:
#                 flash("Last Name must be longer than two characters")
#             if len(password) < 8:
#                 flash("Password must be longer than 8 characters")
#         if '_flashes' in session:
#             return redirect('/')
#
#         # pass password though bcrypt
#         password_hash = bcrypt.generate_password_hash(password)
#
#         # if email is valid we register them
#         new_user_query = "INSERT INTO users(first_name, last_name, email, password, created_at, updated_at) VALUES(:first_name, :last_name, :email, :password, now(), now())"
#
#         new_user_data = {
#             'first_name':first_name,
#             'last_name':last_name,
#             'email':email,
#             'password': password_hash #<--insert encrypted password
#         }
#         newUserId = mysql.query_db(new_user_query,new_user_data)
#         flash('You are now registered')
#         return redirect('/')
#     #LOGIN
#     elif 'login' in request.form:
#         user_query = "SELECT id, first_name, last_name, email, password FROM users WHERE email = :email"
#
#         user_data = {
#             'email': email,
#         }
#         # Check if CheckUser is a empty list or not.
#         checkUser = mysql.query_db(user_query,user_data)
#         print "checkUser:",checkUser
#         print "this is the user query:", user_query
#         #if checkUser
#         if not checkUser:
#             flash('Invalid Email and/or Password')
#         elif not bcrpyt.check_password_hash(checkUser[0]['pass'],password):
#             flash('Invalid Email and/or Password')
#         if '_flashes' in session:
#             return redirect('/')
#         session['the_wall'] = {
#             'first_name': checkUser[0]['first_name'],
#             'last_name': checkUser[0]['last_name'],
#             'email': checkUser[0]['email'],
#             'id': checkUser[0]['id']
#         }
#         return redirect('/the_wall')
#
#
# @app.route('/the_wall')
# def the_wall():
#     return render_template('the_wall.html')
#
# @app.route('/logout')
# def logout():
#     session.clear()
#     return redirect('/')

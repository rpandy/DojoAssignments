#import proper dependencies
from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt
import re #needed for validation
app = Flask(__name__)
bcrypt = Bcrypt(app)
app.secret_key = "SEEEECRETTTS"
mysql = MySQLConnector(app, 'wall_db')

#validation
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
LETTERS_ONLY = re.compile(r'[A-Za-z]')

@app.route('/')
def index():
    all_users = mysql.query_db("SELECT first_name, id FROM users")
    # print "this is the index route"
    # print "users dictionary:", users
    return render_template('index.html', all_users = all_users)

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
    print"this is the pw hash:", pw_hash
    #insert new user into user table via SQL
    #pass pw_hash variable into table as encrypted password
    insert_user_query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES(:first_name, :last_name, :email, :password, now(), now())"

    insert_user_data = {
        'first_name': first_name,
        'last_name': last_name,
        'email': email,
        'password': pw_hash #encrypted variable
    }

    #function to run SQL query
    newUserId = mysql.query_db(insert_user_query,insert_user_data)
    return redirect('/the_wall')

@app.route('/login', methods=['POST'])
def login():
    # login variables
    email = request.form['email']
    password = request.form['password']

    #CHECK TO SEE IF EMAIL IS ALREADY IN DATABASE - CHECK REGISTRATION

    #login validation (1/2)
    email_errors = 0
    login_query = "SELECT id, first_name, last_name, email, password FROM users WHERE email = :email"
    login_data = {'email': email }
    loginUser = mysql.query_db(login_query,login_data)
    print "encrypted password:", loginUser[0]['password']
    # print "this is loginUser:", loginUser
    if not loginUser:
        flash("Invalid Email/Password combination")
        email_errors += 1
    elif not bcrypt.check_password_hash(loginUser[0]['password'],password):
        flash("Invalid Email/Password combination")
        email_errors += 1
        # return redirect('/the_wall')
    if email_errors:
        return redirect('/')
    #login validation (2/2).
    errors = 0
    #validate password (cannot be empty)
    if len(password) < 2:
        flash("Password field cannot be empty")
        errors += 1
    #validate email address (cannot be empty/ must be valid email format)
    if not EMAIL_REGEX.match(request.form['email']):
        flash("Not a valid email")
        errors += 1
    #if there are any errors redirect user to /login page
    if errors:
        return redirect('/')

    #save only what we need in the session.
    #do not save the user ID
    session['the_wall'] = {
        'first_name': loginUser[0]['first_name'],
        'last_name': loginUser[0]['last_name'],
        'email': loginUser[0]['email'],
        'id': loginUser[0]['id'],
    }
    print "currently saved in session:", session['the_wall']
    return redirect('/the_wall')

@app.route('/the_wall')
def wall_activity():

    users = mysql.query_db("SELECT first_name, id FROM users")
    all_messages = mysql.query_db("SELECT message, id FROM messages")


    return render_template('the_wall.html', users = users, all_messages=all_messages)

#route to post new messages to The Wall.
@app.route('/the_wall/<user_id>/post', methods=['POST'])
def postMessage(user_id):

    message_query = "INSERT INTO messages(user_id, message, created_at, updated_at)VALUES(:user_id, :message, now(), now())"

    message_data = {
        'message': request.form['message'],
        'user_id': user_id
    }
    messages = mysql.query_db(message_query, message_data)

    print user_id
    print "this is the posted messages:",request.form['message']

    return redirect('/the_wall')

#ROUTE TO GET MESSAGE ID
#???
@app.route('/the_wall/<user_id>/comment')
def get_message_id(user_id):

    #PASSING VARIABLES TO THE NEW TEMPLATE AFTER COMMENTS ARE ADDED> FIND A BETTER WAY TO DO THIS

    users = mysql.query_db("SELECT first_name, id FROM users")
    all_messages = mysql.query_db("SELECT message, id FROM messages")

    get_message_query = "SELECT id, message FROM messages WHERE user_id = :user_id"
    get_message_data = {
    'user_id': session['the_wall']['id']
    }
    get_messages = mysql.query_db(get_message_query,get_message_data)

    print "this is the get_messages query:", get_messages
    return render_template('/the_wall.html', users = users, all_messages=all_messages, get_messages = get_messages)



@app.route('/the_wall/<message_id>/comment', methods=['POST'])
def postComment(message_id):
    comment_query = "INSERT INTO comments(user_id, message_id, comment, created_at, updated_at)VALUES(:user_id, :message_id, :comment, now(), now())"

    comment_data = {
        'user_id': session['the_wall']['id'],
        'message_id': message_id,
        'comment': request.form['comment']
        }

    get_comments = mysql.query_db(comment_query, comment_data)
    print "this is the posted comment:", request.form['comment']

    # comment_user_query = "SELECT first_name FROM users WHERE user_id = :user_id"
    #
    # comment_user_data = {
    #     'user_id': session['the_wall']['id']
    # }


    return redirect('/the_wall')


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

app.run(debug=True) #leave at default port 5000


#route to select user not necessary because that info was
#saved in session
#might not be necessary
# @app.route('/the_wall/<user_id>/post')
# def selectUser(user_id):
#     select_query = "SELECT first_name FROM users WHERE id = :id"
#     select_data = {
#         'id': user_id
#     }
#     selected_user = mysql.query_db(select_query, select_data)
#     print "Selected User query:", selected_user
#
#     return render_template('/the_wall.html', selected_user = selected_user)

        #if validation is successful complete login via else statement
    # else:
    #     select_user_query = "SELECT * FROM users WHERE email = :email LIMIT 1"
    #
    #     select_user_data = {'email': email }
    #
    #     user = mysql.query_db(select_user_query, select_user_data)
    #     print "login query:", mysql.query_db(select_user_query, select_user_data)
    #
    #     all_users = mysql.query_db('SELECT * FROM users')
    #     print "password:", user[0]['password']
    #     user_pw = user[0]['password']
    #     print user_pw
    #     if bcrypt.check_password_hash(user_pw,password):
    #         print "test test"
    #         return redirect('/the_wall')
    #     else:
    #         flash("Incorrect login info: Email and password combination does not match")
    #         return redirect('/login')









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

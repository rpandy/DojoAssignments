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
#initial get route to the wall. Passing all three tables to html for future use
@app.route('/the_wall')
def wall_activity():

    users = mysql.query_db("SELECT first_name, id FROM users")
    all_messages = mysql.query_db("SELECT message, id, created_at FROM messages")
    all_comments = mysql.query_db("SELECT user_id, message_id, comment FROM comments")

    return render_template('the_wall.html', users=users, all_messages=all_messages, all_comments=all_comments)

#route to post new messages to The Wall.
@app.route('/the_wall/<user_id>/post', methods=['POST'])
def postMessage(user_id):

    message_query = "INSERT INTO messages(user_id, message, created_at, updated_at)VALUES(:user_id, :message, now(), now())"

    message_data = {
        'message': request.form['message'],
        'user_id': session['the_wall']['id']
    }
    messages = mysql.query_db(message_query, message_data)

    print user_id
    print "this is the posted messages:",request.form['message']

    return redirect('/the_wall')

@app.route('/the_wall/<message_id>/comment')
def showComments(message_id):
    show_comments_query = "SELECT comment FROM comments WHERE message_id =:message_id"

    show_comments_data = {
    'message_id': message_id
    }
    show_comments = mysql.query_db(show_comments_query,show_comments_data)

    print "this is the show_comments query:", show_comments
    return render_template('the_wall.html', show_comments=show_comments)

# post comment to the wall
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

    return redirect('/the_wall')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

app.run(debug=True) #leave at default port 5000

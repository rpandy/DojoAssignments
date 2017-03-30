from flask import Flask, redirect, render_template, request, session,flash
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt
import re
app = Flask(__name__)
app.secret_key = "SEEEECRETTTS"
bcrpyt = Bcrypt(app)
mysql = MySQLConnector(app, 'userinfo')

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

@app.route('/')
def index():
    # users = mysql.query_db('SELECT * FROM users')
    return render_template('index.html')


@app.route('/user', methods=['POST'])
def logreg():
    #checking the name from the forms to determine
    #whether we are registering or logging in.
    if "register" in request.form:
    #checking to see if email exist
    #to protect from sql injection we pass
    #email from form into a data variable
    #simply entering request.form['email'] would leave us exposed.
        user_query = "SELECT id FROM users WHERE email = :email"
        user_data = {
            'email': request.form['email']
        }
        #this will return a list based on mysqlconnection file.
        #if nothing is found we get an empty list
        userExists = mysql.query_db(user_query, user_data)
        print "This is the if userExists query:",userExists
        #check if there is actually a value in userExists w/ conditionals.
        #dont let the user know that email is already in database.
        #use a more cryptic message
        if userExists:
            flash("Email address is invalid. Please use another address")
            print user_data['email']
            print userExists
        #email validation
        else:
            if not EMAIL_REGEX.match(request.form['email']):
                flash("Email must be a valid email")
            if len(request.form['fname']) < 2:
                flash("First Name must be longer than two characters")
            if len(request.form['lname']) < 2:
                flash("Last Name must be longer than two characters")
            if len(request.form['password']) < 8:
                flash("Password must be longer than 8 characters")
            #ran check to see items saved in session
            # for item in session:
            #     print item

            #statement to determine whether we have messages in flash
            #flash messages are saved in session.
            # 'underbar' flashes in session
        if '_flashes' in session:
            return redirect('/')
        #pass password through salt and bcrypt for encrpytion
        passHash = bcrpyt.generate_password_hash(request.form['password'])
        #if email is valid we register them
        new_user_query = "INSERT INTO users(first_name, last_name, email, pass, created_at, updated_at)VALUES(:first_name, :last_name, :email, :pass, now(), now())"
        #cleans up the data by making it a literal string.
        new_user_data = {
            'first_name': request.form['fname'],
            'last_name': request.form['lname'],
            'email': request.form['email'],
            'pass': passHash
        }


        newUserId = mysql.query_db(new_user_query, new_user_data)
        # do not save the password to session
        # so we build out user info instead of setting new_user_data to session['userinfo']
        # we need to save this info into session so we dont need to make multiple database queries,
        # we can save settings and we can track the user on multiple pages
        flash('You are now registered')
        return redirect('/')

    #2 methods on the same route. in order to differentiate we can use  names in the forms. SEE ABOVE (BEFORE REGISTRATION)
    elif 'login' in request.form:
        #SQL query is doing the comparison to check whether email and password match
        user_query = "SELECT id, first_name, last_name, email, pass FROM users WHERE email = :email"

        user_data = {
        'email': request.form['email'],
        }

        #this will always be a list of something or an empty list
        checkUser = mysql.query_db(user_query,user_data)
        # print "CheckUser is:",checkUser
        #we use a conditional
        #if its correct we login the user. if incorrect name OR password is incorrect.
        #for security reasons we dont tell them what they have right or wrong
        if not checkUser:
            print "no user"
            flash('Invalid Email and/or Password')
            #taking password that you just entered into form, hashing it again
            #and comparing it to the previously hashed password saved in the database
            #at checkUser[0]['pass']. If not equal then redirect.
        elif not bcrpyt.check_password_hash(checkUser[0]['pass'],request.form['password']):
            print "bad pass"
            flash('Email or Password is invalid')
        if "_flashes" in session:
            return redirect('/')
            # since this is a list we need to use [0] to access that list
        session['userinfo'] = {
            'first_name': checkUser[0]['first_name'],
            'last_name': checkUser[0]['last_name'],
            'email': checkUser[0]['email'],
            'id': checkUser[0]['id']
        }
        return redirect('/home')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')

app.run(debug=True, port=8000)

#list of semirestful routes (semi because we cannot use update or delete w/ flask)

# GET ALL USERS - GET ('/user', methods=['GET'])
# SHOW NEW USER CREATION PAGE = GET ('/user/new', methods=['GET'])
# CREATE NEW USER - POST ('/user', methods=['POST'])
# UPDATE USER  - POST/UPDATE ('/user/<id>', methods=['POST'])
# SHOW USER to UPDATE - GET ('/user/<id>/update', methods=['GET'])
# DELETE USER - POST/DELETE ('/user/<id>/delete', methods=['POST'])
# SHOW USER to DELETE - GET ('/user/<id>/delete', methods=['GET'])
# GET ONE USER - GET ('/user/<id>', methods=['GET'])

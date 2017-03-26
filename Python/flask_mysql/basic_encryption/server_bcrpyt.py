from flask import Flask, request, render_template
from mysqlconnection import MySQLConnector
#imports Bcrypt module
from flask_bcrypt import Bcrypt
app = Flask(__name__)
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app, 'DATABASE_NAME_HERE')


#registration
@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/create_user', methods = ['POST'])
def create_user():
    email = request.form['email']
    username = request.form['username']
    password = request.form['password']


    #run validations and if they are successful we can create the password hash with bcrypt

    pw_hash = bcrypt.generate_password_hash(password)

    #now we insert the new user into the database via SQL statement

    insert_query = "INSERT INTO users (email, username, pw_hash, created_at, updated_at) VALUES (:email, :username, :pw_hash, NOW(), NOW())"

    query_data = {
    'email': email,
    'username': username,
    'pw_hash': pw_hash
    }

    user = mysql.query_db(insert_query,query_data)
    #redirect to success page
    return redirect('/success')

    #check_password_hash

    password = 'password'
    pw_hash = bcrypt.generate_password_hash(password)
    test_password_1 = 'thisiswrong'
    bcrypt.check_password_hash(pw_hash, test_password_1) #this will return false
    test_password_2 = 'password'
    bcrypt.check_password_hash(pw_hash, test_password_2) #this will return true

    #when logging in

@app.route('/login', METHODS=['POST'])
    def login():
        email = request.form['email']
        password = request.form['password']
        user_query = "SELECT * FROM users WHERE email = :email LIMIT 1"
        query_data = {'email': email}
        user = mysql.query_db(user_query,query_data) #user will be returned in a list
        if bcrypt.check_password_hash(user[0]['pw_hash'], password):
            #login user
        else:
            #set flash error message and redirect to login page
    








app.run(debug=True, port=8000)

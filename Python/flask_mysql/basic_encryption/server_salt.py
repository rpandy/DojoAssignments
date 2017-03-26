from flask import Flask, redirect, render_template, request, session
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = "SEEEECRETTTS"
mysql = MySQLConnector(app, 'userinfo')

import os, binascii #included at the top of the file
#os.urandom() function returns a string of bytes. its not a normal alphanumeric string so we turn it into a string using the function b2a_hex() to return the value from the open SSL function into a normal alphanumeric string. New random string is set to salt
salt = binascii.b2a_hex(os.urandom(15))


#registration
@app.route('/users/create', methods=[POST])
def create_user():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    encrypted_pw = md5.new(password + salt).hexdigest()
    insert_query = "INSERT INTO users (username, email, password, salt, created_at, updated_at) VALUES (:username, :email, :encrypted_pw, :salt, NOW(), NOW())"

#authentication
    email = request.form['email']
    password = request.form['password']
    user_query = "SELECT * FROM users WHERE users.email = :email LIMIT 1"
    query_data = {'email': email}
    user = mysql.query_db(user_query,query_data)
    if user[0]:
        encrypted_password = md5.new(password + user[0]['salt']).hexdigest();
        if user[0]['password'] == encrypted_password:
            #this means we have a successful login
        else:
            #invalid password!
    else:
        #invalid email



    query_data = {
    'username':username,
    'email':email,
    'encrypted_pw': encrypted_pw,
    'salt': salt
    }
    mysql.query_db(insert_query,query_data)
    return redirect('/')






app.run(debug=True, port=8000)

from flask import Flask, redirect, render_template, request, session
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = "SEEEECRETTTS"
mysql = MySQLConnector(app, 'userinfo')

import md5 #imports the md5 module to generate a hash
password = 'password'
#encrypt the password we provided as 32 character string
encrypted_password = md5.new(password).hexdigest();
print "encrypted password is:", encrypted_password; #this will show you the encrypted value

@app.route('/users/create', methods=['POST'])
def create_user():
    username = request.form['username']
    email = request.form['email']
    password = md5.new(request.form['password']).hexdigest();
    insert_query = "INSERT INTO users (username, email, password, created_at, updated_at) VALUES (:username, :email, :password, NOW(), NOW())"
    query_data = {
    'username':username,
    'email':email,
    'password': password
    }
    mysql.query_db(insert_query,query_data)
    return redirect('/')






app.run(debug=True, port=8000)

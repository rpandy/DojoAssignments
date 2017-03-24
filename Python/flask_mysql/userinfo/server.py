from flask import Flask, redirect, render_template, request, session
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = "SEEEECRETTTS"
mysql = MySQLConnector(app, 'userinfo')

@app.route('/')
def index():
    users = mysql.query_db('SELECT * FROM users')
    return render_template('index.html', user_info=users)


@app.route('/user', methods=['POST'])
def addUser():
    newUser_query = "INSERT INTO users(first_name, last_name, created_at, updated_at)VALUES(:first_name, :last_name, now(), now());"
    #cleans up the data by making it a literal string.
    data = {
        'first_name': request.form['fname'],
        'last_name': request.form['lname']
    }
    newUserId = mysql.query_db(newUser_query, data)
    session['userinfo'] = data
    session['userinfo']['user_id'] = newUserId

    # {
    # 'first_name': request.form['fmame'],
    # 'last_name': request.form['lname'],
    # 'user_id': newUserId
    # }

    # print sesion['userinfo']
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

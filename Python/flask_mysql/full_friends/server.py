from flask import Flask, request, redirect, render_template

import re
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'friendsdb')

@app.route('/')
def index():
    #use double quotes on SQL queries in order to account for the possibility of single quotes withing SQL query.
    query = "SELECT * FROM friends"
    friends = mysql.query_db(query)
    print friends
    print "index route executed"

    return render_template('index.html', friends=friends)

@app.route('/friends', methods=['POST'])
def create():
    insert_query = "INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at) VALUES(:first_name, :last_name, :occupation, now(), now())"

    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'occupation': request.form['occupation']
    }

    mysql.query_db(insert_query,data)
    return redirect('/')
@app.route('/friends/<friend_id>/edit')
def edit(friend_id):
    query = "SELECT * FROM friends"
    friends = mysql.query_db(query)

    edit_query = "SELECT * FROM friends WHERE id = :id"

    data = {'id': friend_id}

    friends = mysql.query_db(edit_query,data)
    return render_template('friends.html', friends=friends)

@app.route('/friends/<friend_id>', methods=['POST'])
def update(friend_id):

    update_query = "UPDATE friends SET first_name = :first_name, last_name = :last_name, occupation = :occupation WHERE id = :id"

    data = {
    'first_name': request.form['first_name'],
    'last_name': request.form['last_name'],
    'occupation': request.form['occupation'],
    'id': friend_id
    }

    mysql.query_db(update_query,data)
    return redirect('/')

@app.route('/friends/<friend_id>/delete', methods=['POST'])
def destroy(friend_id):

    query = "SELECT * FROM friends"
    friends = mysql.query_db(query)

    delete_query = "DELETE FROM friends WHERE ID = :id"
    data = {'id': friend_id}
    mysql.query_db(delete_query,data)
    return redirect('/')

app.run(debug=True, port=8000)

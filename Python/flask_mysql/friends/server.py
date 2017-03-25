from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'friendsdb')

@app.route('/')
def index():
    # use the MySQL object's query_db function
    #define your query
    query = "SELECT * FROM friends"
    friends = mysql.query_db(query)
    print friends
    #pass data to our template
    return render_template('index.html', all_friends = friends)

@app.route('/friends', methods=['POST'])
def create():
    query = "INSERT INTO friends (first_name, last_name, occupation, created_at, updated_at)VALUES(:first_name, :last_name, :occupation, now(), now())"
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'occupation': request.form['occupation']
    }
    # add a friend to the database
    mysql.query_db(query,data)
    return redirect('/')

@app.route('/friends/<friend_id>')
def show(friend_id):
    #write a query to selelct specific user by id. At every poiunt where
    #we want to insert data, we write ":" and variable name
    query = "SELECT * FROM friends WHERE id = :specific_id"
    #then define a dictionary with key that matches :variable_name in query.
    data = {'specific_id': friend_id}
    #run query with inserted data
    friends = mysql.query_db(query,data)
    #Friends should be a list with a single object,
    #so we pass the value at [0] to our template under alias one_friend.

    print "this is the friend id:", friend_id
    return render_template('index.html', one_friend=friends[0])

@app.route('/update_friend/<friend_id>', methods=['POST'])
def update(friend_id):
    query = "UPDATE friends SET first_name = :first_name, last_name = :last_name, occupation = :occupation WHERE id = :id"
    data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'occupation': request.form['occupation'],
            'id': friend_id
            }
    mysql.query_db(query, data)
    return redirect('/')

@app.route('/remove_friend/<friend_id>', methods=['POST'])
def delete(friend_id):
    query = "DELETE FROM friends WHERE if = :id"
    data = {'id': friend_id}
    mysql.query_db(query, data)
    return redirect('/')

app.run(debug=True)

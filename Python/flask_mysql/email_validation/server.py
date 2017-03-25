from flask import Flask, request, redirect, render_template, session, flash

import re
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = "SEEEECRETTTS"
mysql = MySQLConnector(app,'emailsdb')

EMAIL_REGEX =re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')

@app.route('/')
def index():
    print "index route executed"
    emails = mysql.query_db("SELECT * FROM emails")
    # print emails
    return render_template('index.html', all_emails=emails)

@app.route('/email', methods = ['POST'])
def validateEmail():
    # print request.form['email']
    errors = 0
    if len(request.form['email']) < 1:
        flash("EMAIL CANNOT BE BLANK")
        errors+=1

    if not EMAIL_REGEX.match(request.form['email']):
        flash("EMAIL IS NOT VALID")
        errors+=1
    if errors:
        return redirect('/')

    add_email_query = "INSERT INTO emails (email, created_at, updated_at)VALUES(:email, now(), now())"

    data = {'email': request.form['email']}

    newEmail = mysql.query_db(add_email_query,data)
    session['emailsdb'] = data
    return redirect('/success')

@app.route('/success')
def showEmails():
    emails = mysql.query_db("SELECT * FROM emails")
    print emails

    return render_template('success.html', all_emails = emails)

@app.route('/success/delete/<email_id>', methods=['POST'])
def deleteEmail(email_id):
    delete_query = "DELETE FROM emails WHERE ID = :id"
    data = {'id': request.form['email_id']}
    mysql.query_db(delete_query,data)
    return redirect('/success')

app.run(debug=True)

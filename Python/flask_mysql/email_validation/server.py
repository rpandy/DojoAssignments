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
    print emails
    return render_template('index.html', all_emails=emails)

@app.route('/email', methods = ['POST'])
def addEmail():
    print request.form['email']
    if len(request.form['email']) < 1:
        flash("EMAIL CANNOT BE BLANK")
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("EMAIL IS NOT VALID")
    else:
        flash("Thank you!")
    add_email_query = "INSERT INTO emails (email, created_at, updated_at)VALUES(':specific_email', now(), now())"

    data = {'specific_email': request.form['email']}

    newEmail = mysql.query_db(add_email_query,data)
    # session['emailsdb'] = data
    return redirect('/')

app.run(debug=True)

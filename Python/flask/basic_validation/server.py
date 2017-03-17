from flask import Flask, render_template, redirect, request, session, flash
app = Flask(__name__)
app.secret_key = "SECRETSSSSS"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=['POST'])
def process():
    if len(request.form['name']) < 1:
        flash("ERROR ERROR ERROR!! Name cannot be empty!") # just pass a string to the flash function
    else:
        flash("SUCCESS! The name entered into the survey is {}".format(request.form['name']))# just pass a string to the flash function
    return redirect('/')#either way the application should return to the index and display the message
app.run(debug=True)

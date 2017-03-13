from flask import Flask, render_template, request, redirect
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/ninjas')
def ninjas():
    return render_template("ninjas.html")

@app.route('/dojos/new')
def ninja_info():
    return render_template("dojos.html")
    print request.form
    return redirect ('/')

app.run(debug=True)

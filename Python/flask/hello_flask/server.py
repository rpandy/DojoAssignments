from flask import Flask, render_template, request, redirect, session, flash # Import Flask to allow us to create our app, and import
app = Flask(__name__)
app.secret_key = "I<3Secrets"


#each route should do one thing.
#Either post information or gather information to send elsewhere
@app.route('/')
def index():
    if "counter" not in session:
        session['counter'] = 0
    print "Im in my route for index!"
    age = 33
    job = "coder"
    #name you expect variable to be on template and what the variable will be equal to
    
    return render_template('index.html',age = age, job=job)

@app.route('/users', methods = ["POST"])
def new_user():
    if len(request.form['first_name']) == 0:
        flash('FILLE ME IN! I need a name!')
        return redirect('/')
    print request.form["first_name"]
    print request.form['id']
    session['counter'] += 1
    # print session['first_name']
    return redirect('/success')

@app.route('/success')
def showUser():
    # print "in sucess route", session['first_name']
    return render_template('success.html')

@app.route("/clear")
def clear_session():
    session.clear()
    return redirect('/')
app.run(debug='True', port=8000)

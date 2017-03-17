from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = "SECRETSSSSS"

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/result', methods=["POST"])
def survey_submission():
    #print request.form
    user = request.form
    #validation - Name & comment field
    errors = 0
    if len(request.form['name']) < 1:
        #print "if statement works"
        flash("Name field cannot be empty!")
        errors += 1
    if len(request.form['comments']) < 1:
        flash("Comment field cannot be empty!")
        errors += 1
    if len(request.form['comments']) > 120:
        flash("Comment field cannot exceed 120 characters")
        errors += 1
    if errors:
        return redirect('/')
    location = request.form['location']
    fav_language = request.form['fav_language']
    # else:
    #     flash("Thank you for your feedback!")
    #return render_template("results.html", context = {name,location,fav_language,comments})
    #using jinja context dictionary to send variables to the HTML template
    #return render_template("results.html", name = name, location = location, fav_language = fav_language, comments = comments)
    return render_template("results.html", user=user)

@app.route('/')
def goback():
     return redirect('/')
app.run(debug=True, port=8000)

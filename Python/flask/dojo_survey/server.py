from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")
@app.route('/result', methods=["POST"])
def survey_submission():
    #print request.form
    user = request.form
    #print user['name']
    name = request.form['name']
    location = request.form['location']
    fav_language = request.form['fav_language']
    comments = request.form['comments']
    #return render_template("results.html", context = {name,location,fav_language,comments})
    #using jinja context dictionary to send variables to the HTML template
    #return render_template("results.html", name = name, location = location, fav_language = fav_language, comments = comments)
    return render_template("results.html", user=user)
# @app.route('/')
# def goback():
#      return redirect('/')
app.run(debug=True, port=8000)

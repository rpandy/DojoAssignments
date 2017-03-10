from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# @pp.route - now you'll know where youre going. When typing something into address bar this shows
#how to get there. provides a route for the application.
#we're trying to go to the root of the application so we pass in '/'
@app.route('/')
#index function.
def index():
    print "Im in my route for index!"
    return render_template('index.html')

#takes us to localhost:8000/users via get request
@app.route('/users', methods = ["POST"])
def new_user():
    print request.form
    return redirect('/')
app.run(debug='True', port=8000)

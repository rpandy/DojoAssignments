from flask import Flask, render_template, request, redirect # Import Flask to allow us to create our app, and import
                                                            # render_template to allow us to render index.html.


app = Flask(__name__)                                       # Global variable __name__ tells Flask whether or not we
                                                            # are running the file directly or importing it as a module.

# @pp.route - now you'll know where youre going. When typing something into address bar this shows
#how to get there. provides a route for the application.
#we're trying to go to the root of the application so we pass in '/'
@app.route('/')                                             # The "@" symbol designates a "decorator" which attaches the
#index function                                             #following function to the '/' route. This means that
                                                            # whenever we send a request to localhost:8000/ we will run
                                                            # the following "hello_world" function.

def index():
    print "Im in my route for index!"
    return render_template('index.html')                    # Render the template and return it!
#takes us to localhost:8000/users via get request
@app.route('/users', methods = ["POST"])
def new_user():
    print request.form
    return redirect('/')
app.run(debug='True', port=8000)                             # Run the app in debug mode.

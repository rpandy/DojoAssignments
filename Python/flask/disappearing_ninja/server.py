from flask import Flask, render_template, request, redirect, session
app=Flask(__name__)
app.secret_key = "SECRETSSSS"

@app.route('/')
def index():
    if "ninja_details" not in session:
        session['ninja_details'] = []
    return render_template('index.html')

@app.route('/ninja')
def four_turtles():
    ninja_color = {
        'blue': 'Leonardo',
        'purple': 'Donatello',
        'red': 'Raphael',
        'orange': 'Michelangelo'
    }
    #attempting to combine templates.
    #When main_page = TRUE then we show all four turtles
    #When main_page = FALSE we execute the code on the one_character template
    main_page = 'True'
    #print "this is the main page", main_page
    #print "the ninja_color dictionary is the following:", ninja_color
    #print "The value for the key:blue is:", ninja_color['blue']
    session['ninja_details'].append(ninja_color)
    print "list items are indexed... at index 0", session['ninja_details']
    return render_template('/ninja.html', turtles = ninja_color, main_page=main_page)

@app.route('/ninja/<ninja_id>')
def one_turtle(ninja_id):
    print "this is the ninja_id:", ninja_id
    main_page = 'False'
    print "this is the main page", main_page


    return render_template('/one_character.html', ninja_id = ninja_id)
@app.route('/clear')
def clear_session():
    session.clear()
    return redirect('/')
app.run(debug=True)

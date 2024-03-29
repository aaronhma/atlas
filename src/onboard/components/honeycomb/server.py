import sys
sys.path.append('../../../../')

from flask import Flask, render_template, redirect, request
from shared import components
from shared import Gui
from shared import medical
from shared import skyforce
from shared import error

app = Flask(__name__)



    
@app.route('/')
def home():
    return render_template("rocket.html")

@app.route('/homepage')
def homepage():
    c1 = "Navigation"
    c2 = "Guidiance"
    c3 = "Cooling"
    c4 = "Heater"
    c5 = "Computer"
    c6 = "Honeycomb"
    c7 = "Engine"
    c8 = "Thruster"
    c9 = "Communications"
    return render_template("home.html",c1 = c1,c2 = c2, c3 = c3, c4 = c4,c5= c5,c6=c6,c7=c7,c8=c8,c9=c9)

@app.route('/rocket')
def rocket():
    #@TODO(aaronhma): make err get passed
    #error.error_handler(err)
    return redirect('/')

@app.route('/support')
def support(): 
    #@TODO(aaronhma): make err get passed
    #error.error_handler(err)
    return render_template("support.html")

@app.route('/medical')
def medical():
    #@TODO(aaronhma): make err get passed
    #error.error_handler(err)
    if request.method == "GET":
        #@TODO(aaronhma): make err get passed
        error.error_handler(err)
        # @NOTE what to do when you are using GET including adding variables
        medical.__init__()
        return render_template("Medical.html")
    elif request.method == "POST":
        #@TODO(aaronhma): make err get passed
        #error.error_handler(err)
        # @NOTE this is what happens when people submit the form 
        # @NOTE lets use python for the medical info ( log the info)
        medical.post()
        print("POST method called!")
        return render_template("Medical.html")
        
@app.route('/guidance')
def guidance():
    #@TODO(aaronhma): make err get passed
    #error.error_handler(err)
    # @NOTE: keep this here to tell astronauts guidance was migrated to another system - APPROVED
    return render_template("migrated/guidance.html")

@app.route('/games')
def games_home():
    #@TODO(aaronhma): make err get passed
    #error.error_handler(err)
    return render_template("games/home.html")

@app.route('/disney')
def disney():
    #@TODO(aaronhma): make err get passed
    #error.error_handler(err)
    return render_template('disney.html')

@app.route('/appletv')
def appletv():
    #@TODO(aaronhma): make err get passed
    #error.error_handler(err)
    return render_template('appletv.html')

app.run(port=7777) 
# @TODO(aaronhma): Make this work:
# @NOTE: this won't work as server issues
# del app

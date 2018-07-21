""" A basic website created using python and flask """
from flask import Flask, render_template

APP = Flask(__name__)

@APP.route('/')
def home():
    """ This function renders the home.html page. """
    return render_template("home.html")

@APP.route('/about/')
def about():
    """ This function renders the about.html page. """
    return render_template("about.html")

if __name__ == "__main__":
    APP.run(debug=True)

"""
Tao Su
lab13, Flask application
"""
from flask import Flask, render_template, redirect, url_for

"""
create  an object 'app' from the Flask module.
    __name__ set to __main__ if it is the script is running from the main file

"""
app = Flask(__name__)

"""
Set the routing to the main page
"""


# "route" decorator is used to access the roo URL
@app.route('/')
def index():
    name = "taosu"
    check_fruit = "kiwi"
    fruits = ["apple", "pear", "orange", "banana"]
    return render_template('index.html', userName = name, listFruits = fruits, checkFruit = check_fruit)


@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/users')
def users():
    return render_template('users.html')

@app.route('/quotes')
def quotes():
    return redirect(url_for('index'))


# set the 'app' to run if you execute the file directly(not when it is imported)
if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)

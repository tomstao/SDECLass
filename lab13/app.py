"""
Tao Su
lab13, Flask application
"""
from flask import Flask, render_template, redirect, url_for, request
from flask_sqlalchemy import SQLAlchemy

"""
create  an object 'app' from the Flask module.
    __name__ set to __main__ if it is the script is running from the main file

"""
app = Flask(__name__)

# connection to PostgresSQL

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://sutommy:9750@localhost:5432/demoDB'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

"""
Create an object db
"""
db = SQLAlchemy(app)

# define a model (create table in the 'demoDB' database)


# the class name is going to be the table name
class UserLogin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)


"""
Set the routing to the main page
"""


# "route" decorator is used to access the roo URL
@app.route('/', methods=['GET', 'POST'])
def index():

    if request.method == 'POST':
        return 'Successfully requested! Password:' + request.form['password']

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
    with app.app_context():db.create_all()
    app.run(debug=True, host='127.0.0.1', port=5000)

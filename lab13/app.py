"""
Tao Su
lab13, Flask application
"""
from flask import Flask, render_template, redirect, url_for, request, flash, session
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
# Create a secret key to handle data within our server

import os

app.config['SECRET_KEY'] = os.urandom(24)

class UserLogin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)

class Employee(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    employee_id = db.Column(db.String(20), unique=True, nullable=False)
    employee_name = db.Column(db.String(100), nullable=False)
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

@app.route('/users', methods=['GET', 'POST'])
def users():
    if request.method == 'POST':
        try:
            form = request.form
            emp_name = form['employee_name']
            emp_id = form['employee_id']

            # check if employess already exists by name (or use employee if that's unique)
            existing_employee = Employee.query.filter_by(employee_id = emp_id).first()

            if existing_employee:
                flash(f'Employee ID {emp_id} already exists for {existing_employee.employee_name}')
            # Create a new employee with name '{emp_name}' and add data into the database
            new_employee = Employee(employee_name = emp_name, employee_id = emp_id)

            # store first employee name in session
            session['employee1'] = new_employee.employee_name

            # add the new object to our database
            db.session.add(new_employee)
            db.session.commit()

            # message using flash
            flash(f'{request.form["employee_name"]} is successfully registered!')
        except:
            flash('Failed to register employee!')

    return render_template('users.html')

@app.route('/quotes')
def quotes():
    return redirect(url_for('index'))


# set the 'app' to run if you execute the file directly(not when it is imported)
if __name__ == '__main__':
    with app.app_context():db.create_all()
    app.run(debug=True, host='127.0.0.1', port=5000)

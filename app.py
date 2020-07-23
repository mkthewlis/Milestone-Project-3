import os
from flask import Flask, render_template, redirect, request, url_for, session
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import bcrypt

from os import path
if path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_BDNAME"] = 'moveon_database'
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")


# Defines variables used throughout app
mongo = PyMongo(app)
tasks = mongo.db.tasks.find()
users = mongo.db.users


""" The following code creates a simple app that allows a user to register, login and view their account. From there, they can 
manage their tasks with all CRUD functions to optimise the user's experience to get ready for their move. The following tutorials
listed below were used as a basis to inspire the login/ logout functionality:
Register/ login: https://www.youtube.com/watch?v=vVx1737auSE&list=PLXmMXHVSvS-Db9KK1LA7lifcyZm4c-rwj&index=5
Logout: https://flask.palletsprojects.com/en/0.12.x/quickstart/#sessions"""


# Routes user to home page
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


# Routes user to top tips
@app.route('/tips')
def tips():
    return render_template('tips.html')

# Routing for returning users to log back in
@app.route('/sign_in', methods=['POST', 'GET'])
def sign_in():
    if request.method == "GET":
        # If user is already logged in, redirect to /'overview'
        if 'username' in session:
            return redirect(url_for('overview'))
    # This simply returns to html page if the request is 'GET'
        else: 
            return render_template('signin.html')
    # If 'POST', this checks the returning user's details to see if they match what is stored in the DB
    elif request.method == "POST":     
        login_user = users.find_one({'name': request.form['username']})
        # This checks to see if the hashed password written matches the hashed password in the DB and adds them to the session
        if login_user:
            if bcrypt.hashpw(request.form['pass'].encode('utf-8'), login_user['password']) == login_user['password']:
                session['username'] = request.form['username']
                # If correct, the user is sent to their personal overview page with all task functions available to them
                return redirect(url_for('overview'))

        return 'Invalid username/ password combination'


# Routing that shows the users overview/ dashboard when they have logged in or registered
@app.route('/overview', methods=['GET', 'POST'])
def overview():
    return render_template('overview.html', tasks=mongo.db.tasks.find())


# Routing for new users to sign up, hashing the password for security
@app.route('/sign_up', methods=['POST', 'GET'])
def sign_up():
    if request.method == 'POST':
        existing_user = users.find_one({'name': request.form['username']})

        # If there is no existing user, the entered password is hashed for security before being sent to store in the DB
        if existing_user is None:
            hashpass = bcrypt.hashpw(request.form['pass'].encode('utf-8'), bcrypt.gensalt())
            users.insert({'name': request.form['username'], 'password': hashpass})
            session['username'] = request.form['username']
            # With the user data stored, they are sent to their new 'overview' page
            return redirect(url_for('overview'))

        return 'That username already exists!'

    return render_template('signup.html')

# Function to logout existing users
@app.route('/logout')
def logout():
    # This removes the current username from the session
    session.pop('username', None)
    return redirect(url_for('sign_in'))


if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)

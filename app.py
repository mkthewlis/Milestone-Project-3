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

mongo = PyMongo(app)


# Defines variables used throughout app
tasks = mongo.db.tasks.find()
users = mongo.db.users


# Begins by routing user to home page
@app.route('/')
@app.route('/index.html')
def index():
    return render_template('index.html')


# Routing for returning users to log back in
@app.route('/sign_in', methods=['POST', 'GET'])
def sign_in():
    if request.method == "GET":
    # a GET request means we want to return the html page
        return render_template('signin.html')

    elif request.method == "POST":     
        # Checks if there is a username already in the DB matching what the user has written
        login_user = users.find_one({'name': request.form['username']})
        return redirect(url_for('overview'))

        # If so, checks to see if the hashed password written matches the hashed password in the DB and adds them to the session
        if login_user:
            if bcrypt.hashpw(request.form['pass'].encode('utf-8'), login_user['password'].encode('utf-8')) == login_user['password'].encode('utf-8'):
                session['username'] = request.form['username']
                # If correct, the user is sent to their personal overview page with all task functions available to them
                return redirect(url_for('overview'))

        return 'Invalid username/ password combination'


# Routing that shows the users overview/ dashboard when they have logged in or registered
@app.route('/overview', methods=['GET'])
def overview():
    # This confirms who the user is when they have logged in/ registered
    if 'username' in session:
        return 'You are logged in as ' + session['username']

    return render_template('overview.html')


@app.route('/login')
def login():
    return ''


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


"""@app.route('/')
@app.route('/user_overview')
def user_overview():
    return render_template("overview.html", tasks=mongo.db.tasks.find())"""


if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)

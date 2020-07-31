import os
from flask import Flask, render_template, redirect, request, url_for, session, flash
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
        # This returns to html page if the request is 'GET' and redirects logged in user to their overview
        if 'username' in session:
            return redirect(url_for('overview'))

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
            else:
                flash('Oops, it looks like you\'ve entered the wrong combination of username and password. Why not try again?')
                return redirect(url_for('sign_in'))

        elif not login_user:
            flash('We don\'t have that username on file! Please check your spelling and try again.')
            return redirect(url_for('sign_in'))


# Routing that shows the users overview/ dashboard when they have logged in or registered
@app.route('/overview', methods=['GET', 'POST'])
def overview():
    if 'username' not in session:
        return render_template('signup.html')

    tasks = list(mongo.db.tasks.find({"username": session["username"]}))
    completed = []  # empty list, so we don't make two calls to the db

    if tasks:
        for task in tasks:
            if task["complete"]:
                completed.append(task)  # if completed=True, add to list above
        return render_template(
                                'overview.html',
                                pending_tasks='Pending tasks:',
                                completed_tasks='Complete tasks:',
                                tasks=tasks,
                                completed=completed)

    elif not tasks:
        empty_list = 'It looks like your moving list is empty!<br>\
                    Why not get started by adding some tasks right away?'
        # Removes image until user has tasks
        image_position = 'image_position'
        return render_template(
                                'overview.html',
                                empty_list=empty_list,
                                tasks=tasks, 
                                image_position=image_position)

    return render_template('overview.html', tasks=tasks, completed=completed, image_position=image_position)


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

        flash('Oops, that username already exists! Please try again with another username.')

    return render_template('signup.html')



# Function to logout existing users
@app.route('/logout')
def logout():
    username = session['username']
    if 'username' in session: 
    # This removes the current username from the session
        session.pop('username', None)

        flash("You've successfully logged out. See you next time, " + username + "!")
        return redirect(url_for('sign_in'))


# Directs to page to add new tasks
@app.route('/new_task')
def new_task():
    if 'username' not in session:
        return render_template('signup.html')

    return render_template('newtasks.html')


""" Code below inspired by Code Institute module, as I learned with this repository: 
https://github.com/mkthewlis/task_manager_app """
@app.route('/add_task', methods=['POST'])
def add_task():
    tasks = mongo.db.tasks
    username = session['username']
    form_data = {
        "username": username,
        "task_title": request.form.get("task_title"),
        "task_info": request.form.get("task_info"),
        "delegation": request.form.get("delegation"),
        "task_due": request.form.get("task_due"),
        "complete": False
    }
    tasks.insert_one(form_data)

    flash('Great, your task has been added! Return to \'My Tasks\' for an overview or add another task while you\'re here.')
    return redirect(url_for('new_task'))


# Source used for reference for this function: https://kb.objectrocket.com/mongo-db/how-to-update-a-mongodb-document-in-python-356

@app.route('/update_tasks/<task_id>', methods=['POST', 'GET'])
def update_tasks(task_id):
    if 'username' not in session:
        return render_template('signup.html')
    #Finds the task with matching id
    username = session['username']

    # if request.method == 'POST':

    #else:   
    updating_task = mongo.db.tasks.find_one_and_update({"_id": ObjectId(task_id)}, 
        {"$set":
        {"username": username,
        "task_title": request.form.get("task_title"),
        "task_info": request.form.get("task_info"),
        "delegation": request.form.get("delegation"),
        "task_due": request.form.get("task_due"),
        "complete": False}
    })
    
    flash('Your task has been changed! Return to \'My Tasks\' for an overview.')
    return render_template('updatetasks.html', task=updating_task)


# Function to update tasks to move them to 'complete tasks' list
@app.route('/complete_task/<task_id>', methods=['POST', 'GET'])
def complete_task(task_id):

    mongo.db.tasks.update(
        {'_id': ObjectId(task_id)}, 
        {"$set": {
        "complete": True}})

    flash("Well done! You\'re one step closer to being ready to MoveOn.")
    return redirect(url_for('overview'))


@app.route('/delete_task/<task_id>')
def delete_task(task_id):
    mongo.db.tasks.remove({'_id': ObjectId(task_id)})
    
    flash("Your task has been deleted. Why not add another?")
    return redirect(url_for('overview'))


if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)

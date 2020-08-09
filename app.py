import os
from flask import (
    Flask,
    render_template,
    redirect,
    request,
    url_for,
    session,
    flash,
    Markup
)
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
import bcrypt
if os.path.exists("env.py"):
    import env


app = Flask(__name__)

# Environment variables to store DB password
app.config["MONGO_BDNAME"] = 'moveon_database'
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")


# Defines variables used throughout app
mongo = PyMongo(app)
tasks = mongo.db.tasks.find()
users = mongo.db.users
tips = mongo.db.tips.find()


# Routes user to index page as default
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')


""" The following code allows a user to register, login and view their
    account. From there, they can manage their tasks with all CRUD functions
    to optimise the user's experience to get ready for their move. The
    following tutorials were used as a basis to inspire the sign in/ sign
    out functionality: Register/ login: https://www.youtube.com/watch?v=
    vVx1737auSE&list=PLXmMXHVSvS-Db9KK1LA7lifcyZm4c-rwj&index=5
    Logout: https://flask.palletsprojects.com/en/0.12.x/quickstart/#sessions"""


# Routing for the sign in feature
@app.route('/sign_in', methods=['POST', 'GET'])
def sign_in():
    if request.method == "GET":
        # If a user is already in session, they are flashed a message
        # confirming this to them, with a prompt to sign out to change account.
        if 'username' in session:
            flash(
                'You\'re already signed in! Sign out ' +
                'first if you want to change account.')
            return redirect(url_for('overview'))

        return render_template('signin.html')
    # This checks the returning user's details to see if they match
    # what is stored in the DB
    elif request.method == "POST":
        login_user = users.find_one({'name': request.form['username']})
        # This checks to see if the hashed password in the form matches the
        # hashed password in the DB and adds them to the session
        if login_user:
            if bcrypt.hashpw(request.form['pass'].encode(
                    'utf-8'), login_user['password']
                    ) == login_user['password']:
                session['username'] = request.form['username']
                # If correct, the user is sent to their personal overview
                # page with all task functions available to them. Otherwise
                # they are flashed a warning message to try again
                return redirect(url_for('overview'))
            else:
                flash(
                    'Oops, it looks like you\'ve entered the wrong' +
                    ' combination of username and password. Why not' +
                    ' try again?')
                return redirect(url_for('sign_in'))

        elif not login_user:
            flash(
                'We don\'t have that username on file! Please check' +
                ' your spelling and try again.')
            return redirect(url_for('sign_in'))


# Routing for new users to sign up, hashing the password for security
@app.route('/sign_up', methods=['POST', 'GET'])
def sign_up():
    if request.method == "GET":
        # If a user is already signed in, they are flashed a warning
        # message to sign out to prevent multiple sign-ins
        if 'username' in session:
            flash(
                'You\'re already signed in! Sign out first if ' +
                'you want to change account.')
            return redirect(url_for('overview'))

    else:
        # If there is no existing user in the DB, the entered password
        # is hashed for security before being sent to store in the DB
        existing_user = users.find_one({'name': request.form['username']})
        if existing_user is None:
            hashpass = bcrypt.hashpw(
                request.form['pass'].encode('utf-8'), bcrypt.gensalt())
            users.insert(
                {'name': request.form['username'], 'password': hashpass})
            session['username'] = request.form['username']
            # With the user data stored, they are sent to their new
            # 'overview' page
            return redirect(url_for('overview'))

        flash(
            'Oops, that username already exists! ' +
            'Please try again with another username.')

    return render_template('signup.html')


# Function to logout existing users
@app.route('/logout')
def logout():
    username = session['username']
    if 'username' in session:
        # This removes the current username from the session
        session.pop('username', None)

        flash(
            "You've successfully logged out. " +
            "See you next time, " +
            username + "!")

        return redirect(url_for('sign_in'))


# Routes user to top tips page with different content depending on
# if they are logged in or not
@app.route('/tips', methods=['POST', 'GET'])
def tips():
    # If the user is not signed in, they cannot add a tip to the
    # community board as it is hidden
    if 'username' not in session:
        hide_form = 'hide_form'
        return render_template('tips.html',
                               tips=mongo.db.tips.find(),
                               hide_form=hide_form)

    # If a user is already in session, the sign in/ sign up prompt is
    # hidden as it is unnecessary
    else:
        hide_prompt = 'hide_prompt'
        return render_template('tips.html',
                               tips=mongo.db.tips.find(),
                               hide_prompt=hide_prompt)


# This routing allows users to add a tip to the community board of moving tips
@app.route('/add_tip', methods=['POST'])
def add_tip():
    tips = mongo.db.tips
    username = session['username']
    form_data = {
        "username": username,
        "user_tip": request.form.get("user_tip")
    }

    # This inserts the user's tip with the username taken from
    # the session so they don't have to type their username again
    tips.insert_one(form_data)
    flash(
        "Your tip has been added! Thanks " + username +
        " for sharing your advice to help others MoveOn.")
    return redirect(url_for('tips'))


# Allows user to only edit tips that they have added
# to the community board through a modal popup
@app.route('/edit_tip/<tip_id>', methods=['POST', 'GET'])
def edit_tip(tip_id):
    username = session['username']

    if request.method == 'POST':
        updating_tip = mongo.db.tips.find_one_and_update(
            {"_id": ObjectId(tip_id)},
            {"$set":
                {"username": username,
                    "user_tip": request.form.get("user_tip")}}
        )
        flash('Success, your tip has been changed!')
        return redirect(url_for('tips', tip=updating_tip))

    else:
        updating_tip = mongo.db.tips.find_one({"_id": ObjectId(tip_id)})
        return render_template('tips.html', tip=updating_tip)


# Checks if username is in session to then allow the user to delete a community
# tip that they have added
@app.route('/delete_tip/<tip_id>')
def delete_tip(tip_id):
    mongo.db.tips.remove({'_id': ObjectId(tip_id)})

    flash(
        "Your tip has been deleted from the " +
        "community board. Why not add another?")
    return redirect(url_for('tips'))


# Routing that shows the user's overview/ dashboard when they have signed in
# or registered
@app.route('/overview', methods=['GET', 'POST'])
def overview():
    # Redirects a user not in session to the signup page
    if 'username' not in session:
        return render_template('signup.html')

    tasks = list(mongo.db.tasks.find({"username": session["username"]}))
    # Empty list to be filled below to prevent two calls to DB
    completed = []

    if tasks:
        for task in tasks:
            # Adds completed tasks to the 'completed' list created above
            if task["complete"]:
                completed.append(task)
        return render_template(
            'overview.html',
            pending_tasks='Pending tasks:',
            completed_tasks='Complete tasks:',
            tasks=tasks,
            completed=completed)

    # If a user doesn't have any tasks, they are shown a prompt to add some
    elif not tasks:
        empty_list = 'It looks like your moving list is empty!<br>\
                    Why not get started by adding some tasks right away?'
        # The image is removed from this page until the user has tasks in place
        image_position = 'image_position'
        return render_template(
            'overview.html',
            empty_list=empty_list,
            tasks=tasks,
            image_position=image_position)

    return render_template(
        'overview.html',
        tasks=tasks,
        completed=completed,
        image_position=image_position)


# Routing to direct users to the page where they can begin to add tasks
@app.route('/new_task')
def new_task():
    # Redirects a user not in session to the signup page
    if 'username' not in session:
        return render_template('signup.html')

    return render_template('newtasks.html')


"""
    Code below inspired by a Code Institute module, as I learned with this
    repository: https://github.com/mkthewlis/task_manager_app
"""


# Function to add user tasks to the DB, collecting username from session
# to prevent user from providing it again
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

    flash(Markup(
        'Great, your task has been added! Return to ' +
        '<a href=\"http://ms3-move-on.herokuapp.com/overview\">\'My Tasks\'' +
        '</a> for an overview or add another task while you\'re here.'))
    return redirect(url_for('new_task'))


# Routing to direct the user to the edit task page if they are signed in
@app.route('/edit_task/<task_id>')
def edit_task(task_id):
    # Redirects a user not in session to the signup page
    if 'username' not in session:
        return render_template('signup.html')

    task = mongo.db.tasks.find_one({'_id': ObjectId(task_id)})
    return render_template('updatetasks.html', task=task)


"""
    Source used for reference for this function:
    https://kb.objectrocket.com/mongo-db/how-to-update-a-mongodb-document-in-python-356
"""


# Function to update a user's task
@app.route('/update_tasks/<task_id>', methods=['POST', 'GET'])
def update_tasks(task_id):
    # Redirects a user not in session to the signup page
    if 'username' not in session:
        return render_template('signup.html')

    # Finds the task with matching id to prefill form with the user's
    # previous values stored in the DB
    username = session['username']

    if request.method == 'POST':
        updating_task = mongo.db.tasks.find_one_and_update(
            {"_id": ObjectId(task_id)},
            {"$set":
                {"username": username,
                    "task_title": request.form.get("task_title"),
                    "task_info": request.form.get("task_info"),
                    "delegation": request.form.get("delegation"),
                    "task_due": request.form.get("task_due"),
                    "complete": False}}
        )

        flash('Success, your task has been changed!')
        return redirect(url_for('overview', task=updating_task))

    # This sets the form to the previous values if the user doesn't actually
    # change the task content by posting it
    else:
        updating_task = mongo.db.tasks.find_one({"_id": ObjectId(task_id)})
        return render_template('updatetasks.html', task=updating_task)


# Function to mark tasks as complete
@app.route('/complete_task/<task_id>', methods=['POST', 'GET'])
def complete_task(task_id):

    mongo.db.tasks.update(
        {'_id': ObjectId(task_id)},
        {"$set": {
            "complete": True}})

    flash("Well done! You\'re one step closer to being ready to MoveOn.")
    return redirect(url_for('overview'))


# Allows the user to delete a pending task from their list
@app.route('/delete_task/<task_id>')
def delete_task(task_id):
    mongo.db.tasks.remove({'_id': ObjectId(task_id)})

    flash("Your task has been deleted. Why not add another?")
    return redirect(url_for('overview'))


# Allows a user to delete a completed task from their 'completed' list
@app.route('/delete_complete_task/<complete_id>')
def delete_complete_task(complete_id):
    mongo.db.tasks.remove({'_id': ObjectId(complete_id)})

    flash("Your completed task has been deleted.")
    return redirect(url_for('overview'))


if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)

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


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sign_in')
def sign_in():
    return render_template('signin.html')


"""
def index():
    if 'username' in session:
        return 'You are logged in as ' + session['username']
    
    return render_template('signin.html')

@app.route('/login')
def login():
    return ''

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        users = mongo.db.users
        returning_user = users.find_one({'name' : request.form['username']}) 

        if returning_user is None:
            hashpass = bcrypt.hashpw(request.form['pass'].encode('utf-8'), bcrypt.gensalt())
            users.insert({'name' : request.form['username'], 'password' : hashpass})
            session['username'] = request.form['username']
            return redirect(url_for('index'))

        return 'That username already exists!'

    return render_template('signup.html')
    """

"""@app.route('/')
@app.route('/user_overview')
def user_overview():
    return render_template("overview.html", tasks=mongo.db.tasks.find())"""


if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)

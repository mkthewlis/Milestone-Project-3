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
@app.route('/user_overview')
def user_overview():
    return render_template("overview.html", tasks=mongo.db.tasks.find())


if __name__ == '__main__':
    app.secret_key = 'mysecret'
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)


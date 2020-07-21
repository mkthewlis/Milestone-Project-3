import os
from flask import Flask
from flask_pymongo import PyMongo
from bson.objectid import ObjectId


from os import path
if path.exists("env.py"):
    import env

app = Flask(__name__)

app.config["MONGO_BDNAME"] = 'moveon_database'
app.config["MONGO_URI"] = os.environ.get("MONGO_URI")


@app.route('/')
def hello():
    return 'Hello World! Here I come!'


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
    port=int(os.environ.get('PORT')),
    debug=True)


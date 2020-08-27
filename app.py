import os
from flask import Flask, render_template, redirect, request, url_for, flash
from flask_pymongo import flask_PyMongo
from bson.objectid import ObjectId
if path.exists("env.py"):
    import env 
 
app = Flask(__name__)


app.config["MONGO_DBNAME"] = "approach_people"
app.config["MONGO_URI"] = os.getenv("MONGO_URI")


mongo = PyMongo(app)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
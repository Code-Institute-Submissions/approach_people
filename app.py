import os
from flask import Flask, render_template, redirect, request, url_for, flash
from flask_pymongo import PyMongo
from bson.objectid import ObjectId
from os import path 
if path.exists("env.py"):
    import env 
 
app = Flask(__name__)


app.config["MONGO_DBNAME"] = "approach_people"
app.config["MONGO_URI"] = os.getenv("MONGO_URI")


mongo = PyMongo(app)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/contact_us')
def contact_us():
    return render_template('contact-us.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/jobs_posted')
def jobs_posted():
    return render_template('jobs-posted.html', jobs=mongo.db.jobs.find())


@app.route('/post_job')
def post_job():
    return render_template('post-job.html')


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
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
def add_job():
    return render_template('post-job.html', 
                            categories=mongo.db.categories.find())


@app.route('/post_job', methods=['POST'])
def post_job():
    jobs = mongo.db.jobs
    jobs.insert_one(request.form.to_dict())
    return redirect(url_for('jobs_posted'))


@app.route('/edit_job/<job_id>')
def edit_job(job_id):
    the_job = mongo.db.jobs.find_one({"_id": ObjectId(job_id)})
    all_categories = mongo.db.categories.find()
    return render_template('edit-job.html', job=the_job,
                           categories=all_categories)


@app.route('/update_job/<job_id>', methods=["POST"])
def update_job(job_id):
    jobs = mongo.db.jobs
    jobs.update({'_id': ObjectId(job_id)},
    {
        'category_name': request.form.get('category_name'),
        'company_name': request.form.get('company_name'),
        'job_title': request.form.get('job_title'),
        'email': request.form.get('email'),
        'telephone': request.form.get('telephone'),
        'job_description': request.form.get('job_description'),
        'job_location': request.form.get('job_location'),
        'posted_date': request.form.get('posted_date'),
        'due_date': request.form.get('due_date'),
        'job_salary': request.form.get('job_salary')
    })
    return redirect(url_for('jobs_posted'))


@app.route('/delete_job/<job_id>')
def delete_job(job_id):
    mongo.db.jobs.remove({'_id': ObjectId(job_id)})
    return redirect(url_for('jobs_posted'))


@app.route('/apply')
def apply():
    return render_template('apply.html')



if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
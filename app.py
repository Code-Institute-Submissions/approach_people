import os
from flask import Flask, render_template, redirect, request, url_for, flash
from flask_pymongo import PyMongo
import flask_pymongo
import math
from bson.objectid import ObjectId
from os import path 
if path.exists("env.py"):
    import env 
 
app = Flask(__name__)


app.config["MONGO_DBNAME"] = "approach_people"
app.config["MONGO_URI"] = os.getenv("MONGO_URI")


mongo = PyMongo(app)
# Create index for job titles in jobs collection
mongo.db.jobs.create_index([("job_title", "text")])


@app.route('/')
@app.route('/home')
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
    jobs = mongo.db.jobs.find()
    # Pagination variable
    limit = 5
    # Find the requested page number (or default to page 1)
    page_number = int(request.args.get('page_number', 1))
    count = mongo.db.jobs.count_documents({})
    # identify how many recipe records to be skipped based on page number
    skip = (page_number - 1) * limit
    # skip relevant number of recipes
    jobs.skip(skip).limit(limit)
    # identify how many pages of results are needed
    pages = int(math.ceil(count / limit))
    # create a page range
    total_pages = range(1, pages + 1)
    return render_template('jobs-posted.html', jobs=jobs,
                            page_number=page_number,
                            pages=total_pages,
                            count=count)


@app.route('/post_job', methods=['GET', 'POST'])
def post_job():
    if request.method == 'POST':
        jobs = mongo.db.jobs
        jobs.insert_one(request.form.to_dict())
        return redirect(url_for('jobs_posted'))
    return render_template('post-job.html', 
                            categories=mongo.db.categories.find())


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
        'job_salary': request.form.get('job_salary'),
        'tags': request.form.get('tags'),
        'image_url': request.form.get('image_url'),
        'requirements': request.form.get('requirements'),
        'employment_type': request.form.get('employment_type'),
        'posted_by': request.form.get('posted_by'),
    })
    return redirect(url_for('jobs_posted'))


@app.route('/delete_job/<job_id>')
def delete_job(job_id):
    mongo.db.jobs.remove({'_id': ObjectId(job_id)})
    return redirect(url_for('jobs_posted'))


@app.route('/apply')
def apply():
    return render_template('apply.html')


@app.route('/job_details/<job_id>')
def job_details(job_id):
    the_job = mongo.db.jobs.find_one({"_id": ObjectId(job_id)})
    return render_template('job-details.html', job=the_job)


@app.route("/search", methods=["POST"])
def search():
    query = request.form.get("search")
    # Search the database for the users search value, and find applicable jobs
    search_results = mongo.db.jobs.find(
        {"$text": {"$search": query}})
    # Render the results of the search
    return render_template("jobs-posted.html",
                           jobs=search_results,
                           search=True)


if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
        port=int(os.environ.get('PORT')),
        debug=True)
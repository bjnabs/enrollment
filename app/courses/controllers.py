import functools
from flask import (Blueprint, flash, g, redirect,
                   render_template, request, session, url_for)
from werkzeug.exceptions import abort
#from app.db import get_db

courses = Blueprint('courses', __name__, template_folder='../templates/courses', url_prefix='/course')


@courses.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        id = request.form['courseID']
        title = request.form['title']
        term = request.form['term']
        return render_template("courses_list.html", courses=True, course={"id": id, "title": title, "term": term})
    else:
        id = request.args.get('courseID')
        title = request.args.get('title')
        term = request.args.get('term')
        return render_template("enrollment.html", enrollment=True, course={"id": id, "title": title, "term": term})


@courses.route('/teachers')
def teachers():
    return render_template("teachers.html")


@courses.route('/testimonials')
def testimonials():
    return render_template("testimonials.html")

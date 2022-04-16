
from flask import Blueprint, render_template, request, Response, json  


courseData = [  {   "courseID":"1111",
                        "title":"PHP 101",
                        "description":"Intro to PHP",
                        "credits":3,
                        "term":"Fall, Spring",
                        "level":"Intermediate"}, 

                    {"courseID":"2222","title":"Java 1","description":"Intro to Java Programming","credits":4,"term":"Spring", "level":"Advanced", "instructor":"Ms P Mkoko"}, 
                    {"courseID":"3333","title":"Adv PHP 201","description":"Advanced PHP Programming","credits":3,"term":"Fall"}, 
                    {   "courseID":"4045",
                        "title":"Angular - The Complete Guider",
                        "description":" Angular is a TypeScript-based JavaScript framework that's commonly used by developers to build applications.  Learn Angular online with courses like Full Stack Web Development with Angular and Single Page Web Applications with Angular.",
                        "credits":3,
                        "term":"Fall, Spring",
                        "level":"Advanced", "instructor":"Prof AD Wekhaso"}, 
                    {   "courseID":"5555",
                        "title":"Java 2",
                        "description":"Advanced Java Programming",
                        "credits":4,
                        "term":"Fall",
                        "level":"Advanced", "instructor":"Prof AD Nabusiu"}
                    ] 


main = Blueprint('main',__name__, template_folder='templates')

@main.route('/') 
@main.route('/home')
@main.route('/index')
def index():
    return render_template("index.html", index = True)


@main.route('/news')
def news():
    return render_template("news.html")


@main.route('/about')
def about():
    return render_template("about.html")


@main.route('/facts')
def facts():
    return render_template("facts.html")


@main.route('/faq')
def faq():
    return render_template("faq.html")


@main.route('/links')
def links():
    return render_template("links.html")


@main.route('/events')
def events():
    return render_template("events.html")


@main.route('/services')
def services():
    return render_template("services.html")


@main.route('/contact')
def contact():
    return render_template("contact.html")


@main.route('/dashboard')
def dashboard():
    return render_template("dashboard.html", dashboard=True)


@main.route('/forum')
def forum():
    return render_template("forum.html", forum=True)




from flask import Blueprint, render_template
from app import projects


projects = Blueprint('projects', __name__,
                 template_folder="../templates/projects", url_prefix='/projects')



@projects.route('/')
def index():
    return render_template("projects/index.html", projects = True )

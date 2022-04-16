from flask_login import current_user
from sqlalchemy import func
from flask import (Blueprint, flash, g, redirect,
                   render_template, request, session, url_for)
from werkzeug.exceptions import abort
from app.auth.controllers import login_required
#from .. db import get_db
from .models import db, Post, Comment, Tag, post_tags
from .forms import CommentForm, PostForm

blog = Blueprint('blog', __name__, template_folder="../templates/blog", url_prefix='/blog')

def sidebar_data():
    pass


@blog.route('/index')
def index():
    return render_template("blog/index.html", articles = True)



@blog.route('/new', methods = ['GET', 'POST'])
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post = Post()
        post.user_id = current_user().id
        post.title = form.title.data
        post.text = form.text.data
        db.session.add(post)
        db.session.commit()
        flash("Post created", category='info')
        return redirect(url_for('blog.post'), post_id = post.id)
    
    return render_template("blog/create.html", form = form)





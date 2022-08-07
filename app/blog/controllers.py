from flask_login import current_user
from sqlalchemy import func
from flask import (Blueprint, flash, g, redirect,
                   render_template, request, session, url_for)
from werkzeug.exceptions import abort
from app.auth.controllers import login_required
from app.auth.models import User
#from .. db import get_db
from .models import db, Post, Comment, Tag, post_tags
from .forms import CommentForm, PostForm

blog = Blueprint('blog', __name__, template_folder="../templates/blog", url_prefix='/blog')

def sidebar_data():
    pass


@blog.route('/index')
def index():
    posts = Post.query.all()
    return render_template("blog/index.html", articles = True, posts = posts)



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




@blog.route('/post/<int:post_id>') 
def post(post_id):
    post = Post.query.get_or_404(post_id)
    render_template('post.html', post=post)


@blog.route('/posts_by_tag/<string:tag_name>')
def posts_by_tag(tag_name):
    pass


@blog.route('/posts_by_user/<string:username>') 
def posts_by_user(username):
    user = User.query.filter_by(username=username).first_or_404()
    posts = user.posts.orber_by(Post.date_published.desc()).all()
    recent, top_tags = sidebar_data()
    return render_template('user.html', user=user, posts=posts, recent=recent, top_tags=top_tags)

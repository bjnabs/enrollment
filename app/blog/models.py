from enum import unique
import re  
from app.main.models import TimestampMixin
from app import db

def slugify(s):
    return re.sub('[^\w] +','-', s).lower()


post_tags = db.Table('post_tags',
                db.Column('post_id', db.Integer, db.ForeignKey('posts.id')),
                db.Column('tag_id', db.Integer, db.ForeignKey('tags.id'))
                )



class Post(TimestampMixin, db.Model):
    __tablename__ = 'posts'

    STATUS_PUBLIC = 0    
    STATUS_DRAFT = 1

    id = db.Column(db.Integer, primary_key=True )
    title = db.Column(db.String(255))
    slug = db.Column( db.String(100),  unique = True )
    body = db.Column( db.Text,   nullable=False ) 
    date_published = db.Column(db.DateTime)
    comment_id = db.Column(db.Integer, db.ForeignKey(
        'comment.id'), nullable=False)
    comments = db.relationship('Comment', backref='post',  lazy=True) 
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)
    tags = db.relationship('Tag',  secondary=post_tags, lazy = 'subquery', backref=db.backref('posts', lazy=True) )
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'), nullable=False)
    category = db.relationship('Category', backref=db.backref('posts', lazy=True))
    status = db.Column(db.SmallInteger, default=STATUS_PUBLIC)                           

    def __init__(self, *args, **kwargs):
        super(Post, self).__init__(*args, **kwargs)
        self.generate_slug()
    

    def generate_slug(self):        
        self.slug = '' 
        if self.title:            
            self.slug = slugify(self.title)



    def __repr__(self):
        return "<Post '{}'>".format(self.title)



class Category(db.Model): 
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return '<Category %r>' % self.name


class Comment(TimestampMixin, db.Model): 
    id = db.Column(db.Integer, primary_key=True)    
    name = db.Column(db.String(255))    
    text = db.Column(db.Text)     
    post_id = db.Column(db.Integer, db.ForeignKey('post.id')) 
    
    def __repr__(self): 
        return "<Comment '{}'>".format(self.text[:15])




class Tag(db.Model):
    __tablename__ = 'tags'    
    id = db.Column(db.Integer, primary_key=True)    
    name = db.Column(db.String(64), nullable=True, unique=True)   
    slug = db.Column(db.String(64), unique=True) 


    def __init__(self, *args, **kwargs):        
        super(Tag, self).__init__(*args, **kwargs)        
        self.slug = slugify(self.name)
    
    
    def __repr__(self):        
        return "<Tag '{}'>".format(self.name)
from datetime import datetime
from email.policy import default
from enum import unique
import re 
from app import db

def slugify(s):
    return re.sub('[^\w] +','-', s).lower()


post_tags = db.Table('post_tags',
                db.Column('post_id', db.Integer, db.ForeignKey('post.id')),
                db.Column('tag_id', db.Integer, db.ForeignKey('tag.id'))
                )



class Post(db.Model):
    __tablename__ = 'Posts'

    STATUS_PUBLIC = 0    
    STATUS_DRAFT = 1

    id = db.Column(db.Integer, 
                    primary_key=True
                    )
    title = db.Column(db.String(255))
    slug = db.Column( db.String(100), 
                        unique = True
                        )
    body = db.Column( db.Text, 
                      nullable=False
                      )
    created_date = db.Column( db.DateTime, 
                              nullable=False, 
                              default = datetime.now
                                ) 
    modified_date = db.Column(db.DateTime,
                             nullable=False,
                             default=datetime.now,
                             onupdate = datetime.now
                             ) 
    comments = db.relationship('Comment',
                                backref='post',      
                                lazy='dynamic') 
    user_id = db.Column(db.Integer, 
                        db.ForeignKey('user.id'))
    tags = db.relationship('Tag',        
                            secondary=post_tags,
                            backref=db.backref('posts', lazy='dynamic')
                           )
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'),
                            nullable=False)
    category = db.relationship('Category',
                               backref=db.backref('posts', lazy=True))
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
    __tablename__ = 'Post Categories'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return '<Category %r>' % self.name


class Comment(db.Model):
    __tablename__ = 'Comments'
    id = db.Column(db.Integer, primary_key=True)    
    name = db.Column(db.String(255))    
    text = db.Column(db.Text)    
    date = db.Column(db.DateTime, default = datetime.now)
    post_id = db.Column(db.Integer, db.ForeignKey('post.id')) 
    
    def __repr__(self): 
        return "<Comment '{}'>".format(self.text[:15])




class Tag(db.Model):
    __tablename__ = 'Tags'    
    id = db.Column(db.Integer, primary_key=True)    
    name = db.Column(db.String(64))   
    slug = db.Column(db.String(64), unique=True) 
    def __init__(self, *args, **kwargs):        
        super(Tag, self).__init__(*args, **kwargs)        
        self.slug = slugify(self.name)
    
    
    def __repr__(self):        
        return "<Tag '{}'>".format(self.name)
from flask_wtf import FlaskForm as Form
from wtforms import StringField, TextAreaField, DateField, DateTimeLocalField, SubmitField
from wtforms.validators import DataRequired, Length
from flask_ckeditor import CKEditorField

class CommentForm(Form):
    name = StringField(
        'Name',
        validators=[DataRequired(), Length(max=255)]
    )
    text = TextAreaField(u'Comment', validators=[DataRequired()])


class PostForm(Form):
    title = StringField('Title', [DataRequired(), Length(max=150)])
    summary = TextAreaField('Abstract', [DataRequired(), Length(max=500)])
    body  = CKEditorField('Body')
    submit = SubmitField('Publish')
import email
from re import sub
from flask_wtf import FlaskForm as Form
from flask_wtf import RecaptchaField
from wtforms import StringField, PasswordField, BooleanField, SubmitField, EmailField, ValidationError
from wtforms.validators import DataRequired, Length, EqualTo, URL, Regexp
from .models import User


class LoginForm(Form):
    #username = StringField('Username', [DataRequired(), Length(min=6, max=10)])
    email = EmailField('Email Address', [DataRequired(), Length(max=30)])
    password = PasswordField('Password', [DataRequired(), Length(min=8)])
    remember = BooleanField("Remember Me")
    submit = SubmitField('Sign in')

    def validate(self):
        check_validate = super(LoginForm, self).validate()
        # if our validators do not pass
        if not check_validate:
            return False

        # Does our user exist
        user = User.query.filter_by(username=self.email.data).first()
        if not user:
            self.username.errors.append('Invalid email or password')
            return False

        # Do the passwords match
        if not user.check_password(self.password.data):
            self.username.errors.append('Invalid email or password')
            return False
        return True


class OpenIDForm(Form):
    openid = StringField('OpenID URL', [DataRequired(), URL()])


class RegisterForm(Form):
    #firstName = StringField('First Name', validators=[DataRequired()])
    #lastName = StringField('Last Name', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired(),
                                                   Length(max=10),
                                                   Regexp('^[A-Za-z0-9_.]*$', 0, 'Usernames must have only letters, numbers, dots or underscores')])
    email = EmailField('Email Address', validators=[DataRequired(), Length(1,64)])
    password = PasswordField('Password', validators=[DataRequired(), EqualTo(
        'password_c', message='Passwords must match')])
    password_c = PasswordField(
        'Confirm Password', validators=[DataRequired()])
    submit = SubmitField('Register')
    recaptcha = RecaptchaField()

    def validate(self):
        check_validate = super(RegisterForm, self).validate()

        # if our validators do not pass
        if not check_validate:
            return False
        user = User.query.filter_by(username=self.username.data).first()
        # Is the username already being used
        if user:
            self.username.errors.append("User account with this email already exists")
            return False
        return True

    def validate_email(self, email):
        if User.query.filter_by(email=self.email.data).first():
            raise ValidationError('Account with this email already exists') 

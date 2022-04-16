import email
from re import sub
from flask_wtf import FlaskForm as Form
from flask_wtf import RecaptchaField
from wtforms import StringField, PasswordField, BooleanField, SubmitField, EmailField
from wtforms.validators import DataRequired, Length, EqualTo, URL
from .models import User


class LoginForm(Form):
    username = EmailField('Email or Username', [DataRequired(), Length(max=55)])
    password = PasswordField('Password', [DataRequired()])
    remember = BooleanField("Remember Me")
    submit = SubmitField('Sign in')

    def validate(self):
        check_validate = super(LoginForm, self).validate()
        # if our validators do not pass
        if not check_validate:
            return False

        # Does our user exist
        user = User.query.filter_by(username=self.username.data).first()
        if not user:
            self.username.errors.append('Invalid username or password')
            return False

        # Do the passwords match
        if not user.check_password(self.password.data):
            self.username.errors.append('Invalid username or password')
            return False
        return True


class OpenIDForm(Form):
    openid = StringField('OpenID URL', [DataRequired(), URL()])


class RegisterForm(Form):
    firstName = StringField('First Name', validators=[DataRequired()])
    lastName = StringField('Last Name', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired()])
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    password_confirm = PasswordField(
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

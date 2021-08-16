from flask_wtf import FlaskForm
from wtforms import StringField, BooleanField, PasswordField
from wtforms.validators import DataRequired
from wtforms.fields.html5 import EmailField

class RegisterForm(FlaskForm):
    
    email = EmailField('Email Address', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    name = StringField("Name", validators=[DataRequired()])
    is_admin = BooleanField("Admin")
    
class LoginForm(FlaskForm):
    
    email = EmailField('Email Address', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField("Remember me")
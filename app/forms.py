from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtForms.validators import DataRequired, Email, EqualTo

class RegisterForm(FlaskForm):
  username = StringField('Username', validators=[DataRequired()])
  email = StringField('Email', validators=[DataRequired()])
  password = PasswordField('Password', validators=[DataRequired()])
  confirm_pass = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
  submit = SubmitField('Register')

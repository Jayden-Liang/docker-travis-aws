from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, StringField, PasswordField
from wtforms.validators import DataRequired, Length, Email

class LoginForm(FlaskForm):
    identity = StringField('', validators=[DataRequired(), Length(0, 60, message='too long')])
    password = PasswordField('', validators=[DataRequired()])

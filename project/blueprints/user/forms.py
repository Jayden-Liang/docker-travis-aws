from flask_wtf import FlaskForm
from wtforms import TextAreaField, SubmitField, StringField, PasswordField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class LoginForm(FlaskForm):
    identity = StringField('', validators=[DataRequired(), Length(0, 60, message='too long')])
    password = PasswordField('', validators=[DataRequired()])


class RegisterForm(FlaskForm):
    email = StringField('', validators=[DataRequired(), Email(message='not email'), Length(0, 60, message='too long')])      #...检查数据库中是否有
    username = StringField('', validators=[DataRequired(), Length(0, 15, message='username is too long')])               #... 正则表达式检查格式
    password = PasswordField('', validators=[DataRequired(), Length(3, 20, message='length must be greater than 8')])              # ...搜索下有没有密码的要求
    confirm_password = PasswordField('',  validators=[DataRequired(), EqualTo('password')])

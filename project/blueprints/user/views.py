from flask import Blueprint, url_for, jsonify, redirect, render_template, flash, current_app, render_template
from project.blueprints.user.forms import LoginForm, RegisterForm
from project.blueprints.user.models import User
from itsdangerous import URLSafeTimedSerializer, \
    TimedJSONWebSignatureSerializer

def serializer(email):
    serializer = TimedJSONWebSignatureSerializer(current_app.config.get('SECRET_KEY'), 3600)
    s = serializer.dumps({'user_email': email}).decode('utf-8')
    return s

def deserializer(token):
    serializer = TimedJSONWebSignatureSerializer(current_app.config.get('SECRET_KEY'))
    user_email = serializer.loads(token).get('user_email')
    return User.find_by_identity(user_email)



users = Blueprint('users',__name__, template_folder='templates')


@users.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        identity = form.identity.data
        u = User.find_by_identity(identity)
        if u:
            return redirect(url_for('blog.index', user=u.username))
    return render_template('login.html',form= form)

@users.route('/register', methods=['GET','POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        u = User(
                username=form.username.data,
                password = User.encryptpassword(form.password.data),
                email = form.email.data
        )
        u.save()
        token= serializer(form.email.data)
        from project.blueprints.user.celery_task import sendgrid_email
        sendgrid_email.delay('no-reply@service.com',form.email.data, name = form.username.data, token=token)
        #flash
        return redirect(url_for('users.register'))
    return render_template('register.html', form = form)

@users.route('/activate')
def activate():
    return 'activate page'

@users.route('/')
def index():
    return redirect(url_for('users.activate'))

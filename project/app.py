from flask import Flask, jsonify, request, Blueprint, current_app
from project.extensions import oauth, csrf, login_manager, mail
from project.blueprints.auth.views import auth
from project.blueprints.user.views import users
from project.blueprints.user.models import db, User
from project.blueprints.blog.views import blog
import os

from celery import Celery
CELERY_TASK_LIST =[
    'project.blueprints.user.celery_task'
]


def create_celery_app(app=None):
    app = app or create_app()
    celery = Celery(app.import_name, broker=app.config['CELERY_BROKER_URL'],
    include=CELERY_TASK_LIST)
    celery.conf.update(app.config)
    TaskBase = celery.Task
    class ContextTask(TaskBase):                #以下是为每个task设置context，如果要access数据库，就要设置context
        abstract = True
        def __call__(self, *args, **kwargs):
            with app.app_context():
                return TaskBase.__call__(self, *args, **kwargs)
    celery.Task = ContextTask
    return celery

def create_app(settings_override=None):
    app = Flask(__name__)
    app.config.from_object('config.settings')
    if settings_override is not None:
        app.config.update(settings_override)
    extent(app)
    register_blueprint(app)

    return app

def extent(app):
    oauth.init_app(app)
    csrf.init_app(app)
    db.init_app(app)
    db.app = app
    try:
        db.create_all()
    except:
        print('already exist')    
    login_manager.init_app(app)
    mail.init_app(app)
    return None

def register_blueprint(app):
    app.register_blueprint(auth)
    app.register_blueprint(users)
    app.register_blueprint(blog)
    return None


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

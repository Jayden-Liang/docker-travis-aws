from flask import Flask, jsonify, request, Blueprint, current_app
from project.extensions import oauth, csrf, login_manager
from project.blueprints.auth.views import auth
from project.blueprints.user.views import users
from project.blueprints.user.models import db, User
from project.blueprints.blog.views import blog
import os

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
    login_manager.init_app(app)
    return None

def register_blueprint(app):
    app.register_blueprint(auth)
    app.register_blueprint(users)
    app.register_blueprint(blog)
    return None


@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

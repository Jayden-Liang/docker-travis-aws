from flask import Blueprint, url_for, jsonify, redirect, render_template, flash
from project.blueprints.user.forms import LoginForm
from project.blueprints.user.models import User


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

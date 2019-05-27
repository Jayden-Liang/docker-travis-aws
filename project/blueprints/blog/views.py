from flask import Blueprint, url_for, jsonify, redirect, render_template, flash
from project.blueprints.user.models import User, Blog

blog = Blueprint('blog',__name__, template_folder='templates')


@blog.route('/<user>/blog')
def index(user):
    u = User.find_by_identity(str(user))
    blogs = u.blogs
    return render_template('blog_index.html', blogs=blogs)


@blog.route('/detail/<title>')
def detail(title):
    u = Blog.query.filter_by(title=title)[0]
    return render_template('blog_detail.html', blog = u)

@blog.route('/all-user')
def userlist():
    all = User.query.all()
    return render_template('all.html', all = all)

@blog.route('/all-blogs')
def bloglist():
    all = Blog.query.all()
    return render_template('all-blog.html', all= all)

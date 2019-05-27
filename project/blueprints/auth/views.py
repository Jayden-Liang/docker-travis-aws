from flask import Blueprint, current_app, url_for, jsonify, flash, redirect
from flask_login import login_user
from project.blueprints.auth.thirdparty import providers
from project.blueprints.user.models import User


auth = Blueprint('auth',__name__)


@auth.route('/callback/<provider>')
def oauth_callback(provider):
    target = providers[provider]
    response = target.authorized_response()
    if response is not None:
        access_token = response.get('access_token')
        print('access_token', access_token)
    else:
        access_token = None
    if access_token is None:
        print('access denied')
        return redirect('/')
    r = target.get('user', token=access_token)
    username= r.data.get('login')
    if username:
        u = User.find_by_identity(username)
        if u:
            print(u.username, u.emial)
            login_user(u, remember= True)
            return 'loged in'
        else:
            u = User(username=username)
            u.save()
            login_user(u, remember=True)
            return 'saved and loged in'

    return jsonify(r.data)






@auth.route('/login/<provider>')
def auth_login(provider):
    target = providers[provider]
    return target.authorize(url_for('.oauth_callback',provider=provider, _external=True))

from flask_oauthlib.client import OAuth
from flask_wtf.csrf import CSRFProtect
from flask_login import LoginManager


oauth = OAuth()
csrf = CSRFProtect()
login_manager = LoginManager()

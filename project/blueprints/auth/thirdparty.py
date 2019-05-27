from project.extensions import oauth
from dotenv import load_dotenv
import os
from werkzeug import security

envPath = '/project/.env'
load_dotenv(dotenv_path=envPath)








github = oauth.remote_app(
    name='github',
    consumer_key = os.getenv('GITHUB_CLIENT_ID'),
    consumer_secret= os.getenv('GITHUB_CLIENT_SECRET'),
    request_token_params={'scope': 'user',
                          'state': lambda: security.gen_salt(10)
   },
    base_url ='https://api.github.com/',
    request_token_url=None,                                     #请求新的token的URL，用于OAuth1
    access_token_method='POST',
    access_token_url='https://github.com/login/oauth/access_token',
    authorize_url ='https://github.com/login/oauth/authorize',
)
#
# google = oauth.remote_app(
#     name='google',
#     consumer_key=os.getenv('GOOGLE_CLIENT_ID'),
#     consumer_secret= os.getenv('GOOGLE_CLIENT_SECRET'),
#     request_token_params={'scope': 'email',
#                           'state': lambda: security.gen_salt(10)
#    },
#    base_url ='https://www.googleapis.com/oauth2/v1/',
#    request_token_url=None,
#    access_token_method='POST',
#    access_token_url='https://accounts.google.com/o/oauth2/token',
#    authorize_url ='https://accounts.google.com/o/oauth2/auth'
#
# )

providers ={
    'github': github,
    # 'google': google
}

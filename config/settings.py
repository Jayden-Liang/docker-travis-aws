import os
from dotenv import load_dotenv
b = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
env_path = os.path.join(b, '.env')
load_dotenv(dotenv_path=env_path)


DEBUG = True
SECRET_KEY = 'fahdkjgh6*%$$%((%$j))'
SERVER_NAME ='localhost:5000'

# SQLAlchemy.
db_uri = 'mysql+mysqldb://root:devpassword@mysql:3306/flaskdb'
SQLALCHEMY_DATABASE_URI = db_uri
SQLALCHEMY_TRACK_MODIFICATIONS = False

FIRST_ADMIN='devemail@qq.com'
ADMIN_PWD='123456'


# Celery.
CELERY_BROKER_URL = 'redis://:devpassword@redis:6379/0'          #0代表默认的redis数据库名称
CELERY_RESULT_BACKEND = 'redis://:devpassword@redis:6379/0'
CELERY_ACCEPT_CONTENT = ['json']                    #这几行表示只接受json格式和序列化成json
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_REDIS_MAX_CONNECTIONS = 10     #防止redis因连接过多挂掉， 这里是开发环境限制5个,运行设置为10个

#sendgrid
SENDGRID_API_KEY = os.getenv('SENDGRID_API_KEY')

#flask-mail
MAIL_SERVER = 'smtp.qq.com'
MAIL_PORT = 587
MAIL_USE_TLS = True
MAIL_USERNAME = os.getenv('MAIL_USERNAME')      #邮箱地址
MAIL_PASSWORD = os.getenv('MAIL_PASSWORD')      #授权码
MAIL_DEFAULT_SENDER = ('Jayden-Liang', os.getenv('MAIL_USERNAME'))

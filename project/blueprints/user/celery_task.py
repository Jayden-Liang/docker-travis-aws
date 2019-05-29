from flask import render_template, current_app
# import sendgrid
# from sendgrid.helpers.mail import Mail, Email, Content
from flask_mail import Message
from project.extensions import mail

from project.app import create_celery_app
import os
# from dotenv import load_dotenv
#
# b = os.path.abspath(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))))
# print(b)
# env_path = os.path.join(b, '.env')
# load_dotenv(dotenv_path=env_path)

celery = create_celery_app()


@celery.task()
def send_email(subject, to, **kwargs):
    # x = render_template('email/sendgrid_template.txt')
    # print(os.getenv('SENDGRID_API_KEY'))
    # sg = sendgrid.SendGridAPIClient(apikey=os.getenv('SENDGRID_API_KEY'))
    # from_email = Email("hi@test.com")
    # subject = "Hello World from the SendGrid Python Library on Heroku!"
    # to_email = Email("liangjisong@foxmail.com")
    # content = Content("text/plain", 'fuck yu')
    # mail = Mail(from_email, subject, to_email, content)
    # response = sg.client.mail.send.post(request_body=mail.get())
    body = render_template('email/sendgrid_template.txt', **kwargs)
    message = Message(subject, recipients=[to], body=body)
    mail.send(message)

    return "OK"

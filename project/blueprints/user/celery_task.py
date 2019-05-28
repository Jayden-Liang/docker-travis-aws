from flask import render_template
import sendgrid
from sendgrid.helpers.mail import Mail, Email, Content

from project.app import create_celery_app

celery = create_celery_app()


@celery.task()
def sendgrid_email(email, to, **kwargs):
    x = render_template('email/sendgrid_template.txt', **kwargs)
    print(x)
    sg = sendgrid.SendGridAPIClient(apikey='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')
    from_email = Email(email)
    subject = "activation email"
    to_email = Email(to)
    content = Content("text/plain", x)
    mail = Mail(from_email, subject, to_email, content)
    response = sg.client.mail.send.post(request_body=mail.get())
    return None

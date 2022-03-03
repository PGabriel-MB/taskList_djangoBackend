from threading import Thread
from flask_mail import Message

from app import app, mail

def send_async_email(app, msg):
    ...

def send_email(subject, sender, recipients, text_body, html_body):
    ...

import datetime
from flask import request, render_template
from flask_jwt_extended import create_access_token, decode_token
from flask_restful  import Resource
from jwt.exceptions import ExpiredSignatureError, DecodeError, InvalidTokenError

from models.User import User
from resources.errors import (
    SchemaValidationError, InternalServerError,
    EmailDoesnotExistsError, BadTokenErrorr
)
from services.mail_service import send_email


class ForgotPassword(Resource):
    def post(self):
        url = request.host_url + 'reset/'

        try:
            body = request.get_json()
            email = body.get('email')
            if not email:
                raise SchemaValidationError
            
            user = User.objects.get(email=email)
            if not user:
                raise EmailDoesnotExistsError
            
            expires = datetime.timedelta(hours=24)
            reset_token = create_access_token(str(user.id), expires_delta=expires)
            
            return  send_email(
                '[ToDoer] Reset Your Password',
                sender='86c96cc952-8b00cc@inbox.mailtrap.io',
                recipients=[user.email],
                text_body=render_template(
                    'email/reset_password.txt',
                    url=url+reset_token
                ),
                html_body=render_template('email/reset_password.html', url=url+reset_token)
            )
        except SchemaValidationError:
            raise SchemaValidationError
        except EmailDoesnotExistsError:
            raise EmailDoesnotExistsError
        except Exception as e:
            raise InternalServerError


class ResetPassword(Resource):
    def post(self):
        url = request.host_url + 'reset/'

        try:
        except SchemaValidationError

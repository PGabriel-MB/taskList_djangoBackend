from os import access
from flask import json, request, Response
from flask_restful import Resource
from flask_jwt_extended import create_access_token
from itsdangerous import exc
from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist
import datetime

from models.User import User
from resources.errors import SchemaValidationError, EmailAlreadyExistsError, \
    UnauthorizedError, InternalServerError


class SignUpApi(Resource):

    def is_valid_email(self, email):

        if not'@' in email:
            return False
        
        return True


    def post(self):
        body = request.get_json()

        name, email, password = body.values()

        if not name or not email or not password:
            return {'error': 'check that all fields are filled in correctly'}, 400
        
        if not self.is_valid_email(email):
            return {'error': 'make sure if yor email is correct'}, 400

        if len(password) < 7:
            return {'error': 'The password is too small - minimun of 8 caracteres'}, 400
        

        try:
            user = User(**body)
            user.hash_password()
            user.save()
            id = user.id
            return {'id': str(id), 'message': 'User registered succesfully!'}, 200
        except FieldDoesNotExist:
            raise SchemaValidationError
        except NotUniqueError:
            raise EmailAlreadyExistsError
        except Exception as err:
            return {'message': 'There was an error saving your data!', 'error': f'{err.args}'}


class SignInApi(Resource):
    def post(self):
        try:
            body = request.get_json()
            user = User.objects(email=body.get('email')).first()

            if not user:
                return {'error': 'Unidentified user'}

            authorized = user.check_password(body.get('password'))

            if not authorized:
                return {'error': 'Email or password invalid'}, 401
            
            expires = datetime.timedelta(days=7)
            access_token = create_access_token(identity=str(user.id), expires_delta=expires)

            obj = {
                'token': access_token,
                'user': user,
                'isAuthenticated': True
            }
            return Response(json.dumps(obj), mimetype="application/json", status=200)
        except (UnauthorizedError, DoesNotExist):
            raise UnauthorizedError
        except Exception as err:
            raise InternalServerError

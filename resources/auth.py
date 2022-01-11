from flask import request
from flask_restful import Resource

from models.User import User


class SignUpApi(Resource):

    def is_valid_email(self, email):
        name, dom = email.split('@')

        if not name or not dom:
            return False
        
        return True


    def post(self):
        body = request.get_json()

        name, email, password = body.values()

        if not name or not email or not password:
            return {'error': 'check that all fields are filled in correctly'}, 400
        
        if not self.is_valid_email(email):
            return {'error': 'make sure if yor email is correct'}, 400

        if len(password):
            return {'error': 'The password is too small - minimun of 8 caracteres'}, 400
        

        """ user = User(**body)
        user.hash_password()
        user.save()
        id = user.id

        return {'id': str(id)}, 200 """
        return {'teste': 'testado'}
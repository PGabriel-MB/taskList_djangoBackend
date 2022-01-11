from flask import request
from flask_restful import Resource

from models.User import User


class SignUpApi(Resource):
    def post(self):
        body = request.get_json()
        user = User(**body)
        user.hash_password()
        user.save()
        id = user.id

        return {'id': str(id)}, 200
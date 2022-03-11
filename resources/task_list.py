import imp
from flask import Response, request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from mongoengine.errors import FieldDoesNotExist, DoesNotExist

from models.TaskList import TaskList
from models.User import User
from resources.errors import UnauthorizedError, InternalServerError

class TaskListsApi(Resource):

    @jwt_required
    def get(self, user_id):

        user = User.objets(id=user_id)

        if not user:
            return { 'error': 'this User not exists!' }, 400
        
        try:
            task_lists = TaskList.objects(created_by=user)

            return Response(task_lists, mimetype="application/json", status=200)
        except (UnauthorizedError, DoesNotExist):
            raise UnauthorizedError
        except FieldDoesNotExist:
            raise FieldDoesNotExist
        except Exception as err:
            raise InternalServerError

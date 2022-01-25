from flask import Response, request
from flask_restful import Resource
from flask_jwt_extended import jwt_required
from mongoengine.errors import FieldDoesNotExist, \
    NotUniqueError, DoesNotExist, ValidationError, InvalidQueryError

from models.Task import Task
from resources.errors import SchemaValidationError, TaskAlreadyExistsError, \
    InternalServerError, UpdatingTaskError, DeletingTaskError, TaskNotExistsError


class TasksApi(Resource):
    @jwt_required
    def get(self):
        tasks = Task.objects().to_json()
        return Response(tasks, mimetype="application/json", status=200)

    @jwt_required
    def post(self):
        try:
            body = request.get_json()
            task = Task(**body).save()
            id = task.id
            return { 'id': str(id) }, 200
        except (FieldDoesNotExist, ValidationError):
            raise SchemaValidationError
        except NotUniqueError:
            raise TaskAlreadyExistsError
        except Exception as e:
            raise InternalServerError


class TaskApi(Resource):
    @jwt_required
    def put(self, id):
        try:    
            body = request.get_json()
            Task.objects.get(id=id).update(**body)
            return '', 200
        except InvalidQueryError:
            raise SchemaValidationError
        except DoesNotExist:
            raise UpdatingTaskError
        except Exception:
            raise InternalServerError
    
    @jwt_required
    def delete(self, id):
        try:
            task = Task.objects.get(id=id).delete()
            return '', 200
        except DoesNotExist:
            raise DeletingTaskError
        except Exception:
            raise InternalServerError
    
    @jwt_required
    def get(self, id):
        try:
            task = Task.objects.get(id=id).to_json()
            return Response(task, mimetype="application/json", status=200)
        except DoesNotExist:
            raise TaskNotExistsError
        except Exception:
            raise InternalServerError
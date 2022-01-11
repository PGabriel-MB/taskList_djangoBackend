from flask import Response, request
from flask_restful import Resource
from flask_jwt_extended import jwt_required

from models.Task import Task


class TasksApi(Resource):
    @jwt_required
    def get(self):
        tasks = Task.objects().to_json()
        return Response(tasks, mimetype="application/json", status=200)

    @jwt_required
    def post(self):
        body = request.get_json()
        task = Task(**body).save()
        id = task.id
        return { 'id': str(id) }, 200


class TaskApi(Resource):
    @jwt_required
    def put(self, id):
        body = request.get_json()
        Task.objects.get(id=id).update(**body)
        return '', 200
    
    @jwt_required
    def delete(self, id):
        task = Task.objects.get(id=id).delete()
        return '', 200
    
    @jwt_required
    def get(self, id):
        task = Task.objects.get(id=id).to_json()
        return Response(task, mimetype="application/json", status=200)
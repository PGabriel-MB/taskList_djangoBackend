from flask import Response, request
from flask_restful import Resource
from flask_jwt_extended import jwt_required

from models.TaskList import TaskList


class TaskListApi(Resource):
    ...

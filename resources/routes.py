from .task import TaskApi, TasksApi
from .auth import SignUpApi


def initialize_routes(api):
    api.add_resource(SignUpApi, '/auth/register')

    api.add_resource(TasksApi, '/tasks')
    api.add_resource(TaskApi, '/task/<id>')
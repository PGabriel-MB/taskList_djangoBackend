from resources.task import TaskApi, TasksApi
from resources.auth import SignUpApi, SignInApi
from resources.reset_password import ForgotPassword, ResetPassword


def initialize_routes(api):
    api.add_resource(SignUpApi, '/auth/register')
    api.add_resource(SignInApi, '/auth/login')

    api.add_resource(TasksApi, '/tasks')
    api.add_resource(TaskApi, '/task/<id>')

    api.add_resource(ForgotPassword, '/auth/forgot')
    api.add_resource(ResetPassword, '/auth/reset')
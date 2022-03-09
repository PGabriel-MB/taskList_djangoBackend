class InternalServerError(Exception):
    ...

class SchemaValidationError(Exception):
    ...

class TaskListAlreadyExistsError(Exception):
    ...

class TaskAlreadyExistsError(Exception):
    ...

class UpdatingTaskListError(Exception):
    ...

class UpdatingTaskError(Exception):
    ...

class DeletingTaskListError(Exception):
    ...

class DeletingTaskError(Exception):
    ...

class TaskListNotExistsError(Exception):
    ...

class TaskNotExistsError(Exception):
    ...

class EmailAlreadyExistsError(Exception):
    ...

class UnauthorizedError(Exception):
    ...

class EmailDoesnotExistsError(Exception):
    pass

class BadTokenError(Exception):
    pass

errors = {
    "InternalServerError": {
        "message": "Something went wrong",
        "status": 500
    },
    "SchemaValidationError": {
        "message": "Request is missing required fields",
        "status": 400,
    },
    "TaskListAlreadyExistsError": {
        "message": "TaskList with given name already exists",
        "status": 400
    },
    "TaskAlreadyExists": {
        "message": "Task with given name already existis",
        "status": 400
    },
    "UpdatingTaskListError": {
        "message": "Updating tasklist added by other is forbidden",
        "status": 403
    },
    "UpdatingTaskError": {
        "message": "Updating task added by other is forbidden",
        "status": 403
    },
    "DeletingTaskListError": {
        "message": "Deleting tasklist added by other is forbidden",
        "status": 403
    },
    "DeletingTaskError": {
        "message": "Deleting task added by other is forbidden",
        "status": 403
    },
    "TaskListNotExistsError": {
        "message": "TaskList with given id doesn't exists",
        "status": 400
    },
    "TaskNotExistsError": {
        "message": "Task with given id doesn't exists",
        "status": 400
    },
    "EmailAlreadyExistsError": {
        "message": "User with given email address already exists",
        "status": 400
    },
    "UnauthorizedError": {
        "message": "Invalid username or password",
        "status": 401
    },
    "EmailDoesnotExistsError": {
         "message": "Couldn't find the user with given email address",
         "status": 400
     },
     "BadTokenError": {
         "message": "Invalid token",
         "status": 403
      }
}

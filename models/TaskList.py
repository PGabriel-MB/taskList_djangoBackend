from database.db import db
from .Base import BaseModel
from .User import User

class TaskList(BaseModel):
    user = db.ReferenceField(User, reverse_delete_rule=db.CASCADE)

    name = db.StringField(required=True)
    dead_line = db.DateTimeField(required=False)

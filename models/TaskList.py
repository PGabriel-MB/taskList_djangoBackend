from database.db import db
from .Base import BaseModel
from .User import User

class TaskList(BaseModel):
    name = db.StringField(required=True)
    dead_line = db.DateTimeField(required=False)
    tasks = db.ListField(
        db.ReferenceField('Task', reverse_delete_rule=db.CASCADE)
    )

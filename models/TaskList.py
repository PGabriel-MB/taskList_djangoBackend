from database.db import db
from .Base import BaseModel

class TaskList(BaseModel):
    name = db.StringField(required=True)
    dead_line = db.DateTimeField(required=False)
    tasks = db.ListField(
        db.ReferenceField('Task', reverse_delete_rule=db.CASCADE)
    )

    created_by = db.ReferenceField('User')

from .Base import BaseModel
from database.db import db


class Task(BaseModel):
    name = db.StringField(required=True)
    description = db.StringField(required=False)
    dead_line = db.DateTimeField(required=False)
    is_completed = db.BooleanField(default=False)
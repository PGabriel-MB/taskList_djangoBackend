from .Base import BaseModel
from database.db import db


class Task(BaseModel):
    name = db.StringField(required=True)
    dead_line = db.DateTimeField(required=False)
    is_completed = db.BooleanField(default=False)
from mongoengine.queryset.transform import update
from database.db import db
from .Base import BaseModel


class User(BaseModel):
    name = db.StringField(required=True, unique=True)
    email = db.EmailField(requred=True)
    password = db.StringField(required=True, min_length=6)

    task_lists = db.ListField(
        db.ReferenceField('TaskList', revese_delete_rule=db.CASCADE)
    )

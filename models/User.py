from mongoengine.queryset.transform import update
from database.db import db
from datetime import datetime

class User(db.Document):
    name = db.StringField(required=True, unique=True)
    email = db.EmailField(requred=True)
    password = db.StringField(required=True)
    created = db.DateTimeField(default=datetime.now())
    updated = db.DateTimeField(default=datetime.now())

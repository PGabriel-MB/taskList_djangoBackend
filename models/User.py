from flask_bcrypt import check_password_hash, generate_password_hash

from database.db import db
from .Base import BaseModel


class User(BaseModel):
    name = db.StringField(required=True, unique=True)
    email = db.EmailField(requred=True, unique=True)
    password = db.StringField(required=True, min_length=6)

    task_lists = db.ListField(
        db.ReferenceField('TaskList', revese_delete_rule=db.CASCADE),
        required=False
    )


    def hash_password(self):
        self.password = generate_password_hash(self.password).decode('utf8')
    

    def check_password(self, password):
        return check_password_hash(self.password, password)

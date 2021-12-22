from database.db import db
from datetime import datetime


class BaseModel(db.Document):
    meta = {
        'abstract': True
    }

    created = db.DateTimeField(default=datetime.utcnow())
    updated = db.DateTimeField(default=datetime.utcnow())
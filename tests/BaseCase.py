import imp
import unittest

from app import app
from database.db import db


class BaseCase(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.app = db.get_db()
    
    def tearDown(self):
        for collection in self.db.list_collection_names():
            self.db.drop_collection(collection)
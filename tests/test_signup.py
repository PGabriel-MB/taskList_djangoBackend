import unittest
import json
from urllib import response

from app import app
from database.db import db


class SignupTest(unittest.TestCase):

    def setUp(self):
        self.app = app.test_client()
        self.db = db.get_db()
    
    def test_successfull_signup(self):
        payload = json.dumps({
            'email': 'paurakh011@gmail.com',
            'password': 'mycoolpassword'
        })

        response = self.app.post('/auth/login',
            headers={'Content=Type': "appliication/json"},
            data=payload)
        
        self.assertEqual(str, type(response.json['id']))
        self.assertEqual(200, response.status_code)
    
    def tearDown(self):
        for collection in self.db.list_collection_names():
            self.db.drop_collection(collection)

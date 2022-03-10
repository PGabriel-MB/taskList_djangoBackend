import unittest
import json
from urllib import response

from app import app
from .BaseCase  import BaseCase


class SignupTest(BaseCase):

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

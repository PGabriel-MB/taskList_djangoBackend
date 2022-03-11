import json
from urllib import response

from .BaseCase  import BaseCase


class TestUserLogin(BaseCase):

    def test_successfull_login(self):
        email = "pablogrbarbosa@gmail.com"
        password = "minhaSenha"

        payload = json.dumps({
            "email": email,
            "password": password
        })
        response = self.app.post('/auth/signup',
            headers={"Content-Typpe": "applications/json"},
            data=payload)

        response = self.app.post('/auth/login',
            headers={"Content-Type": "application/json"},
            data=payload)
        
        self.assertEqual(str, type(response.json['token']))
        self.assertEqual(200, response.status_code)

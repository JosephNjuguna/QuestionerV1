import unittest
from app import app
import os
import json


class UserTest(unittest.TestCase):
    def setUp(self):
        self.application = app
        self.app = self.application.test_client()
        self.user1= {
            "firstname": 'joe',
            "lastname":'alan',
            "email": 'test1@mail.com',
            "password":'a12n',
            "confirmpassword":'a12n'
        }
        self.user2 ={
            'email': 'test1@gmail.com',
            'password':'a12n'
        }
        self.user3= {
            "email": 'test1@mail.com',
            "password":'',
        }
        self.user4 ={
            'email': '',
            'password':'a12n'
        }
    def test_good_sign_up(self):
        """Test good user sign up"""
        response = self.app.post('/api/v1/auth/signup', data= json.dumps(self.user1), content_type='application/json')
        self.assertEqual(response.status_code, 201)


    def test_good_log_in(self):
        """test good user log in """
        response = self.app.post('/api/v1/auth/login', data= json.dumps(self.user2), content_type='application/json')
        self.assertEqual(response.status_code, 200)
    
    def test_correct_email_empty_password(self):
        """test empty password log in """
        response = self.app.post('/api/v1/auth/login', data= json.dumps(self.user3), content_type='application/json')
        self.assertEqual(response.status_code, 400)
    
    def test_empty_email_correct_password(self):
        """test empty email log in """
        response = self.app.post('/api/v1/auth/login', data= json.dumps(self.user4), content_type='application/json')
        self.assertEqual(response.status_code, 400)
    
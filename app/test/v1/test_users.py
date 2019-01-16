import unittest
from app import app
import os
import json


class UserTest(unittest.TestCase):
    def setUp(self):
        self.application = app
        self.app = self.application.test_client()
        self.user1= {
            "firstname": 'jose',
            "lastname":'alan',
            "email": 'test1@mail.com',
            "password":'a12nj',
            "confirm_password":'a12nj'
        }

        self.user2 ={
	        "email": "test1@mail.com",
            "password":"a12nj"
        }
        self.user3 ={
	        "": "test1@mail.com",
            "password":"a12nj"
        }
        self.user4= {
            "firstname": 'joe',
            "lastname":'alan',
            "email": 'test1@mail.com',
            "password":'a12nj',
            "confirm_password":'a12nj'
        }
        self.user5= {
            "firstname": 'joe',
            "lastname":'alan',
            "email": 'test1@mail.com',
            "password":'a12n',
            "confirm_password":'a12'
        }
    
    def test_1_good_sign_up(self):
        """Test good user sign up"""
        response = self.app.post('/api/v1/auth/signup', data= json.dumps(self.user1), content_type='application/json')
        self.assertEqual(response.status_code, 201)
    
    def test_2_good_sign_up(self):
        """Test good firstname length"""
        response = self.app.post('/api/v1/auth/signup', data= json.dumps(self.user4), content_type='application/json')
        self.assertEqual(response.status_code, 400)
    
    def test_3_good_sign_up(self):
        """Test password mismatch"""
        response = self.app.post('/api/v1/auth/signup', data= json.dumps(self.user4), content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_4_good_log_in(self):
        """test good user log in """
        response = self.app.post('/api/v1/auth/login', data= json.dumps(self.user2), content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_5_empty_key_field_login(self):
        """test empty key  """
        response = self.app.post('/api/v1/auth/login', data= json.dumps(self.user3), content_type='application/json')
        self.assertEqual(response.status_code, 500)


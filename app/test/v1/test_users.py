import unittest
import os
import json

#local imports
from app import app

class UserTest(unittest.TestCase):
#setup
    def setUp(self):
        self.application = app
        self.app = self.application.test_client()
#test good sign up 201
        self.user1= {
            "firstname": 'jose',
            "lastname":'alan',
            "email": 'test1@mail.com',
            "password":'a12njose',
            "confirm_password":'a12njose'
        }
#test valid log in 200
        self.user2 ={
	        "email": 'test1@mail.com',
            "password":'a12njose'
        }
#test empty key 500
        self.user3 ={
	        "":"test1@mail.com",
            "password":"a12nj"
        }
#test password and passwordconfirm not matching 400
        self.user4= {
            "firstname": 'joe',
            "lastname":'alan',
            "email": 'test1@mail.com',
            "password":'a12njJOSE',
            "confirm_password":'a12nj'
        }
#test that email not found 404
        self.user5 ={
	        "email":"test10@mail.com",
            "password":"a12njose"
        }
#test incorrect password 400
        self.user6 ={
	        "email": 'test1@mail.com',
            "password":'a12nse'
        }
#actual api endpoint test
    def test_1_good_sign_up(self):
        """Test good user sign up"""
        response = self.app.post('/api/v1/auth/signup', data= json.dumps(self.user1), content_type='application/json')
        self.assertEqual(response.status_code, 201)
    
    def test_2_good_log_in(self):
        """test good user log in """
        response = self.app.post('/api/v1/auth/login', data= json.dumps(self.user2), content_type='application/json')
        self.assertEqual(response.status_code, 200)
    
    def test_3_short_username_sign_up(self):
        """Test firstname length"""
        response = self.app.post('/api/v1/auth/signup', data= json.dumps(self.user4), content_type='application/json')
        self.assertEqual(response.status_code, 400)
    
    def test_4_invalid_passwords(self):
        """Test password mismatch"""
        response = self.app.post('/api/v1/auth/signup', data= json.dumps(self.user4), content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_5_not_found_email(self):
        """Test email not found"""
        response = self.app.post('/api/v1/auth/login', data= json.dumps(self.user5), content_type='application/json')
        self.assertEqual(response.status_code, 404)

    def test_6_empty_key_field_login(self):
        """test empty key  """
        response = self.app.post('/api/v1/auth/login', data= json.dumps(self.user3), content_type='application/json')
        self.assertEqual(response.status_code, 500)
    
    def test_7_failed_log_in(self):
        """test failed log in due to incorrect email"""
        response = self.app.post('/api/v1/auth/login', data= json.dumps(self.user6), content_type='application/json')
        self.assertEqual(response.status_code, 400)
    

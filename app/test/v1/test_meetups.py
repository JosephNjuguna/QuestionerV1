"""test for api endpoints"""
# inbuilt modelues
import json
import unittest
# local imports
from app import app
class MeetupTest(unittest.TestCase):
    def setUp(self):
        self.appliaction = app
        self.app = self.appliaction.test_client()
        self.record1 = {
            'topic': "AI",
            'location': "iHub Upperhill,Nairobi Kenya ",
            'tag': "fight fake news",
            'id': 1,
            "meetup_id": "1e0326b0-5425-4c81-8f29-69bee50c3cba",
            'meetup_date': "2019-01-16 07:09:44.822295",
        }
        self.record2 = {
            "topic": "using AI to create jobs",
            "status": "yes",
            "name": "alan"
        }
        self.record3 = {
            "": "AI meetup fsffakenya",
            "location": "iHub Upperhill,Nairobi Kenya",
            "tag": "@ankarae grill"
        }
        self.record4 = {
            "name": "Jose",
            "topic": "",
            "status": "yes"
        }

    def test_1_create_meetup(self):
        """test user should be able to create meetup"""
        response = self.app.post(
            '/api/v1/meetup', data=json.dumps(self.record1), content_type='application/json')
        self.assertEqual(response.status_code, 201,
                         msg='Successful meetup createion')

    def test_test_empty_fields(self):
        """test create meetup"""
        response = self.app.post(
            '/api/v1/meetup', data=json.dumps(self.record4), content_type='application/json')
        self.assertEqual(response.status_code, 500,
                         msg='Ensure that all Keys are Provided in the Data')

    def test_2_upcoming_meetups(self):
        """user view upcoming meetups"""
        response = self.app.get(
            '/api/v1/meetup/upcoming', data=json.dumps(self.record1), content_type='application/json')
        self.assertEqual(response.status_code, 200,
                         msg='Get Upcoming Meetups successfully')

    def test_3_get_specific_meetup(self):
        response = self.app.get(
            '/api/v1/meetup/1', data=json.dumps(self.record1), content_type='application/json')
        self.assertEqual(response.status_code, 200,
                         msg='Get Specific Question ')

    def test_4_user_rsvp(self):
        """test user rsvp for a meetup"""
        response = self.app.post(
            '/api/v1/meetup/1/rsvp', data=json.dumps(self.record2), content_type='application/json')
        self.assertEqual(response.status_code, 201,
                         msg='Successful Meetup RSVP')

    def test_5_empty_topic_in_rsvp(self):
        """test user has empty key"""
        response = self.app.post(
            '/api/v1/meetup/1/rsvp', data=json.dumps(self.record4), content_type='application/json')
        self.assertEqual(response.status_code, 400,
                         msg='Ensure that Topic fields are Provided')

    def test_6_empty_key_in_rsvp(self):
        """test user has no key"""
        response = self.app.post(
            '/api/v1/meetup/1/rsvp', data=json.dumps(self.record1), content_type='application/json')
        self.assertEqual(response.status_code, 500,
                         msg='Ensure that all Keys are Provided in the Data')

    def test_7_if_meetup_id_exist(self):
        """test meetup id does not exist"""
        response = self.app.get(
            '/api/v1/meetup/2', data=json.dumps(self.record1), content_type='application/json')
        self.assertEqual(response.status_code, 404,
                         msg='Check whether id exist or not ')

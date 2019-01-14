import unittest
import os
import json
from app import app

class MeetupTest(unittest.TestCase):
    def setUp(self):
        self.appliaction= app
        self.app = self.appliaction.test_client()
        self.record1={
            'topic' : "AI",
            'location' : "iHub Upperhill,Nairobi Kenya " ,
            'happeningOn' : "Sat 14th Jan 2019",
        }
        self.record2 = {
            "topic":"using AI to create jobs",
            "status": "yes",
            "name":"alan"
        }
    
    def test_upcoming_meetups(self):
        """user view upcoming meetups"""
        response = self.app.get('/api/v1/meetup/upcoming', data= json.dumps(self.record1), content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_user_rsvp(self):
        """test user rsvp for a meetup """
        response = self.app.post('/api/v1/meetup/rsvp', data= json.dumps(self.record2), content_type='application/json')
        self.assertEqual(response.status_code, 201)
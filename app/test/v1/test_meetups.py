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
            "meetup":"Ai",
            "topic":"using AI to create jobs",
            "status": "yes",
            "name":"alan"
        }
    
    def test_upcoming_meetups(self):
        """user view upcoming meetups"""
        response = self.app.get('/api/v1/meetups/upcoming', data= json.dumps(self.record1), content_type='application/json')
        self.assertEqual(response.status_code, 200)

    def test_get_record(self):
        pass
    
    def test_user_authorized(self):
        pass

    def test_not_found(self):
        pass

    def test_user_rsvp(self):
        """test user rsvp for a meetup """
        response = self.app.post('/api/v1/meetups/1/rsvps', data= json.dumps(self.record2), content_type='application/json')
        self.assertEqual(response.status_code, 201)
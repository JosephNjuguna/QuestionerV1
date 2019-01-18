"""testing questions url api endpoints """
import json
import unittest
# local imports
from app import app

class QuestionsTest(unittest.TestCase):
    """Testing Question URL API endpoints"""
    def setUp(self):
        self.application = app
        self.app = self.application.test_client()
        self.question1 = {
            'user': "Joseph",
            'meetup': 1,
            'title': "Entrance Ticket Price",
            'body': "How much will be paid by each person for entrance"
        }
        self.question2 = {
            'user': "Joseph",
            'meetup': 1,
            'title': "",
            'body': "How much will be paid by each person for entrance"
        }
        self.question3 = {
            'user': 1,
            'meetup': 1,
            'title': "Entrance Ticket Price",
            'body': ""
        }
        self.question4 = {
            'user': "",
            'meetup': None,
            'title': "Entrance Ticket Price",
            'body': "How much will be paid by each person for entrance"
        }
        self.question5 = {
            'user': "",
            'meetup': 2,
            'title': "Entrance Ticket Price",
            'body': "How much will be paid by each person for entrance"
        }

    def test_qood_question_post(self):
        """test that user post a question with all required fields"""
        response = self.app.post(
            '/api/v1/meetup/1/question', data=json.dumps(self.question1), content_type='application/json')
        self.assertEqual(response.status_code, 201)

    def test_empty_title_question_post(self):
        """test user input question with empty title"""
        response = self.app.post(
            '/api/v1/meetup/1/question', data=json.dumps(self.question2), content_type='application/json')
        self.assertEqual(response.status_code, 400)

    def test_empty_body_question_post(self):
        """test user inputs"""
        response = self.app.post(
            '/api/v1/meetup/1/question', data=json.dumps(self.question3), content_type='application/json')
        self.assertEqual(response.status_code, 400)

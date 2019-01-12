from flask_restful import Api
from flask import Blueprint

from app.api.v1.views.meetupviews import CreateMeetup, UpcomingMeetup, SpecificMeetup, MeetupRsvp

version_one = Blueprint('api_v1', __name__)
api = Api(version_one)

api.add_resource(UpcomingMeetup, '/meetup/upcoming', '/meetup/upcoming/')
api.add_resource(CreateMeetup, '/meetup', '/meetup', '/meetup/' , '/meetup/')
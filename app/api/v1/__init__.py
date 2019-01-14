from flask_restful import Api
from flask import Blueprint

from app.api.v1.views.meetupviews import CreateMeetup, UpcomingMeetup, SpecificMeetup, MeetupRsvp
from app.api.v1.views.questionsviews import PostQuestion, UpvoteQuestion, DownvoteQuestion
from app.api.v1.views.usersviews import Signup, Login

version_one = Blueprint('api_v1', __name__)
api = Api(version_one)

api.add_resource(UpcomingMeetup, '/meetup/upcoming', '/meetup/upcoming/')
api.add_resource(CreateMeetup, '/meetup', '/meetup', '/meetup/' , '/meetup/')
api.add_resource(SpecificMeetup,'/meetup/<string:id>','/meetup/<string:id>/')
api.add_resource(MeetupRsvp,'/meetup/rsvp','/meetup/rsvp/')
api.add_resource(UpvoteQuestion,'/questions/<string:id>/upvote','/questions/<string:id>/upvote/')
api.add_resource(DownvoteQuestion,'/questions/<string:id>/downvote','/questions/<string:id>/downvote/')
api.add_resource(PostQuestion,'/question', '/question/' , '/questions','/questions/')
api.add_resource(Signup, '/auth/signup', '/auth/signup/')
api.add_resource(Login, '/auth/login', '/auth/login/')

from flask_restful import Api
from flask import Blueprint

from app.api.v1.views.meetupviews import CreateMeetup, UpcomingMeetup, SpecificMeetup, MeetupRsvp
from app.api.v1.views.questionsviews import PostQuestion, UpvoteQuestion, DownvoteQuestion, GetSpecificQuestion
from app.api.v1.views.usersviews import Signup, Login

version_one = Blueprint('api_v1', __name__)
api = Api(version_one)

api.add_resource(UpcomingMeetup, '/meetup/upcoming', '/meetup/upcoming/')
api.add_resource(CreateMeetup, '/meetup', '/meetup', '/meetup/', '/meetup/')
api.add_resource(SpecificMeetup, '/meetup/<string:id>', '/meetup/<string:id>/')
api.add_resource(MeetupRsvp, '/meetup/<string:id>/rsvp',
                 '/meetup/<string:id>/rsvp/')
api.add_resource(UpvoteQuestion, '/meetup/<string:id>/question/<string:questionid>/upvote',
                 '/meetup/<string:id>/question/<string:questionid>/upvote/')
api.add_resource(DownvoteQuestion, '/meetup/<string:id>/question/<string:questionid>/downvote',
                 '/meetup/<string:id>/question/<string:questionid>/downvote/')
api.add_resource(PostQuestion, '/meetup/<string:q_id>/question', '/meetup/<string:q_id>/question/',
                 '/meetup/<string:q_id>/question/', '/meetup/<string:q_id>/question/')
api.add_resource(GetSpecificQuestion,
                 '/meetup/<string:id>/question/<string:quizid>')
api.add_resource(Signup, '/auth/signup', '/auth/signup/')
api.add_resource(Login, '/auth/login', '/auth/login/')

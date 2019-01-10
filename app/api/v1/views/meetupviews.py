from flask import Flask,Blueprint,jsonify,make_response
from app.api.v1.models.meetup import MeetUpModels, meetuplist

meetup_api = Blueprint('meetup_api',__name__,)

@meetup_api.route('/meetups/upcoming',methods=["GET"])
def upcomingMeetup():
    meetups_upcoming = MeetUpModels().get_meetup()
    return make_response(jsonify({"Upcoming meetup": meetups_upcoming}),200)

@meetup_api.route('/meetups/<string:id>',methods=["GET"])
def getSpecificmeetup(id):
    return make_response(jsonify({"message":"get a specific meetup"}),200)

@meetup_api.route('/meetups/<string:id>/rsvps',methods=["POST"])
def respondMeetuprsvp(id):
    return make_response(jsonify({"message":"PLEASE RSVP TO A MEET UP"}),201)

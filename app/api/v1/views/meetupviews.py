from flask import Flask,Blueprint,jsonify,make_response, request
from app.api.v1.models.meetup import MeetUpModels, meetuplist

meetup_api = Blueprint('meetup_api',__name__,)
meetupmodel = MeetUpModels()

@meetup_api.route('/meetups/upcoming',methods=["GET"])
def upcomingMeetup():
    """
    a user can get details of all upcoming details
    """
    meetups_upcoming = MeetUpModels().get_meetup()
    return make_response(jsonify({"Upcoming meetup": meetups_upcoming}),200)

@meetup_api.route('/meetups/<string:id>',methods=["GET"])
def getSpecificmeetup(id):
    """
        a user can get 
        details of a 
        specific meetup
    """
    return make_response(jsonify({"message":"get a specific meetup"}),200)

@meetup_api.route('/meetups/<string:id>/rsvps',methods=["POST"])
def respondMeetuprsvp(id):
    """
        a user 
        can RSVPS for 
        a specific meetup
    """
    data = request.get_json()
    meetup_id= id
    topic = data['topic']  
    status = data['status']
    username = data['name']

    if topic == "" or status == ""or username == "" or meetup_id == "":
        return make_response(jsonify({"message":"Fields cnat be empty"}))

    user_rsvp = meetupmodel.rsvp_meetup(meetup_id,topic,status,username)
    return make_response(jsonify({"Successful RSVP TO the MEET UP" : user_rsvp}),201)

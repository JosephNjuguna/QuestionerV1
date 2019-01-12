from flask import Flask,Blueprint,jsonify,make_response, request
from app.api.v1.models.meetup import MeetUpModels, meetuplist

meetup_api = Blueprint('meetup_api',__name__,)
meetupmodel = MeetUpModels()

class UpcomingMeetup():
    def get(self):
        """
        a user can get details of all upcoming details
        """
        meetups_upcoming = MeetUpModels().get_meetup()
        return make_response(jsonify({"Upcoming meetup": meetups_upcoming}),200)

class SpecificMeetup():
    def __init__(self):
        pass
    def get(self, id):
        """
            a user can get 
            details of a 
            specific meetup
        """
        meetup_detail =  meetupmodel.get_specific_meeetup(id)
        return make_response(jsonify({"message":meetup_detail}),200)

class MeetupRsvp():
    def __init__(self):
        pass

    def post(self,id):
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

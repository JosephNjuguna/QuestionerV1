from flask import Blueprint,jsonify,make_response, request
from flask_restful import Resource
import datetime
import uuid

from app.api.v1.models.meetup import MeetUpModels, meetuplist

meetup_api = Blueprint('meetup_api',__name__,)
meetupmodel = MeetUpModels()

meetupdata = meetuplist
alert = "Id not found"
empty_alert = "Fields cant be Empty"
class CreateMeetup(Resource):
    def __init__(self):
        self.happeningon = datetime.datetime.utcnow()
        self.id = uuid.uuid4()
    
    def post(self):
        data = request.get_json()

        for k,v in data.items():
            if k== "" or v=="":
                return make_response(jsonify({"message":empty_alert}),400)

        topic = data['topic']
        location = data['location']
        date = self.happeningon
        meetup_id = self.id
        tag = data['tag']

        createmeetup = meetupmodel.create_meetup(topic, meetup_id, location, date, tag)
        return make_response(jsonify({"message":createmeetup}),200)
class UpcomingMeetup(Resource):
    def get(self):
        """
        a user can get details of all upcoming details
        """
        meetups_upcoming = MeetUpModels().get_meetup()
        return make_response(jsonify({"Upcoming meetup": meetups_upcoming}),200)

class SpecificMeetup(Resource):
    def __init__(self):
        self.meetup = MeetUpModels()
    def get(self, id):
        """
            a user can get 
            details of a 
            specific meetup
        """
        specificmeetup= self.meetup.get_specific_meeetup(str(id))
        return make_response(jsonify({"message":specificmeetup}),200)

class MeetupRsvp(Resource):
    def __init__(self):
        pass

    def post(self):
        """
            a user 
            can RSVPS for 
            a specific meetup
        """
        data = request.get_json()
        topic = data['topic']  
        status = data['status']
        username = data['name']

        if topic == "" or status == ""or username == "":
            return make_response(jsonify({"message":"Fields cnat be empty"}),400)

        user_rsvp = meetupmodel.rsvp_meetup(topic,status,username)
        return make_response(jsonify({"Successful RSVP TO the MEET UP" : user_rsvp}),201)

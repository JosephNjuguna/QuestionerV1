meetuplist = []
meetuprsvp = []


empty_alert = "Id not found "
class MeetUpModels():
    def __init__(self):
        self.list = meetuplist
        self.rsvp = meetuprsvp
        
    def create_meetup(self, topic, meetup_id, location, date, tag):
        payload = {
            "status": 200,
            "data" : [ {
                "topic" : topic,
                "location" : location ,
                "happeningOn": date ,
                "tags" : tag,
                "id":meetup_id
            }]
        }
        add_meetup = self.list.append(payload)
        return self.list

    def get_meetup(self):
        upcoming_meetups = self.list
        return upcoming_meetups
    
    def get_specific_meeetup(self,id):
        data = meetuplist
        return data

    def rsvp_meetup(self,meetup_id,topic,status,username):
        payload = {
            "meetup":meetup_id,
            "topic":topic,
            "status": status,
            "user":username
        }
        rsvp_record = self.rsvp.append(payload)
        return True
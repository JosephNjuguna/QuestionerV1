meetup_list = []
meetup_rsvp = []

empty_alert = "Id not found "


class MeetUpModels():

    def create_meetup(self, topic, public_id, id, location, date, tag):
        payload = {
            "status": 200,
            "meetup_id": public_id,
            "topic": topic,
            "location": location,
            "happeningOn": date,
            "tags": tag,
            "id": id
        }
        add_meetup = meetup_list.append(payload)
        return meetup_list

    def get_meetup(self):
        upcoming_meetups = meetup_list
        return upcoming_meetups

    def get_specific_meeetup(self, id):
        get_meetup = [
            meetup_data for meetup_data in meetup_list if meetup_data["id"] == id]
        if get_meetup:
            return get_meetup
        return False

    def rsvp_meetup(self, topic, status, username, public_id, rsvp_date):
        payload = {
            "topic": topic,
            "status": status,
            "user": username,
            "rsvp_id": public_id,
            "rsvp_date": rsvp_date
        }
        rsvp_record = meetup_rsvp.append(payload)
        return meetup_rsvp

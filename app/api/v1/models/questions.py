questions_list= []

class QuestionClass():
    def __init__(self):
        self.data = questions_list

    def post_question(self, user, meetup, title, body):
        payload = {
            'status' : 201,
            'data' : [{
                "user":user,
                "meetup":meetup,
                "questiontitle":title,
                "questionbody": body
            }]
        }
        questiondata =  self.data.append(payload)
        return True
    
    def get_one_question(self,id):
        question_id = [quiz for quiz in self.data if quiz[id]== id]
        if not  question_id:
            return False
        return question_id

    def upvote_question(self, id):
        payload = [payload for payload in self.data if payload['id'] == id]

        if not payload:
            return False

        upvote_votes = self.data[0]["votes"] + 1
        self.data[0]["votes"] = upvote_votes

        if self.data:
            return [{
                "meetup": self.data[0]["meetup"],
                "title": self.data[0]["title"],
                "body": self.data[0]["body"],
                "votes": self.data[0]["votes"]
            }]

    def downvote_question(self, id):
        payload = [payload for payload in self.data if payload['id'] == id]

        if not payload:
            return False

        downvote_votes = self.data[0]["votes"] + 1
        self.data[0]["votes"] = downvote_votes

        if self.data:
            return [{
                "meetup": self.data[0]["meetup"],
                "title": self.data[0]["title"],
                "body": self.data[0]["body"],
                "votes": self.data[0]["votes"]
            }]


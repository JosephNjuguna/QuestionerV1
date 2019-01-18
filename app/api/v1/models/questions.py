from app.api.v1.models.users import users_list
questions_list = []

class QuestionClass():
    def __init__(self, q_list):
        self.data = q_list

    def post_question(self, user, meetup, title, body, public_id, question_id, q_id):
        """ a user should be able to post a question"""
        payload = {
            "user": user,
            "meetup": meetup,
            "question_title": title,
            "question_body": body,
            "id": question_id,
            "public-id": public_id,
            "meetup_id": q_id,
            "votes": 0
        }
        question_data = self.data.append(payload)
        return questions_list

    def get_one_question(self, id):
        """a user should be able to get a single question"""
        question_id = [quiz for quiz in self.data if quiz['id'] == id]
        print(question_id)
        if not question_id:
            return False
        return question_id

    def upvote_question(self, id):
        """ a user should be able to upvote a question"""
        payload = [payload for payload in self.data if payload['id'] == id]
        if not payload:
            return False
        upvote_votes = self.data[0]["votes"] + 1
        self.data[0]["votes"] = upvote_votes
        return "Upvote successful"

    def downvote_question(self, id):
        """ a user should be able to downvote a question"""
        payload = [payload for payload in self.data if payload['id'] == id]
        if not payload:
            return False
        for user in users_list:
            if id == user[0]["id"]:
                return "voted"
        downvote_votes = self.data[0]["votes"] - 1
        if downvote_votes == 0:
            return False
        self.data[0]["votes"] = downvote_votes

        return "Downvote successful"

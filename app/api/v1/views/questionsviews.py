from app.api.v1.models.questions import questions_list, QuestionClass
from flask import jsonify,make_response,request
from flask_restful import Resource
import uuid

from app.api.v1.utilis.validations import InputValidation
questionmodel = QuestionClass(questions_list)

meetup_validation = InputValidation()
class GetSpecificQuestion(Resource):
    """a user should be able to get a specific question api endpoint"""
    def __init__(self):
        self.model = questionmodel

    def get(self,id, quizid):
        verify_id = meetup_validation.validate_meetup_id(int(id))
        if not verify_id:
            return {"message":"Meetup Id not found"}

        verify_id = meetup_validation.validate_question_id(int(quizid))
        if not verify_id:
            return {"message":"Question Id not found"}

        question_specific = self.model.get_one_question(int(quizid))
        return make_response(jsonify({"message": question_specific}),200)
class PostQuestion(Resource):
    def post(self,q_id):
        """
        user should be able to post a question endpoint
        """
        try:
            data = request.get_json()
            data_state = meetup_validation.check_state(data)
            user = data['user']
            meetup= data['meetup']
            title=data['title']
            body=data['body']
            public_id = str(uuid.uuid4())
            question_id = len(questions_list)+1

            if data['user'] == "":
                return {"message": "Input Username please. It cant be empty"},400
            if data['meetup'] == "":
                return {"message": "Input Meetup name please. It cant be empty"},400
            if data['title'] == "":
                return {"message": "Input Title please. It cant be empty"},400
            if data['body'] == "":
                return {"message": "Input short Description of meetup.t cant be empty"},400

            verify_id = meetup_validation.validate_meetup_id(int(q_id))
            if not verify_id:
                return {"message":"Meetup Id not found"},400
            question_payload = questionmodel.post_question(user, meetup, title, body, public_id,question_id, q_id)
            for q_data in question_payload:
                response = {
                    "question_title": q_data['question_title'],
                    "question_body":q_data['question_body'],
                    "user": q_data['user'],
                    "meetup": q_data['meetup'],
                    "id": q_data['id'],
                    "votes": q_data['votes'],
                    "meetup_id":q_data['meetup_id']
                }
            return make_response(jsonify({
                "status":201,
                "message":response
                }),201)
        except KeyError:
            return make_response(jsonify({"status": 500, "error": "Expecting a field key"}),500)
class UpvoteQuestion(Resource):
    """ a user should  be able to upvote a question"""

    def __init__(self):
        self.upvotemodel = questionmodel
    def patch(self,id, questionid):
        try:
            verify_id = meetup_validation.validate_meetup_id(int(id))
            if not verify_id:
                return {"message":"Meetup Id not found"},404

            verify_id = meetup_validation.validate_question_id(int(questionid))
            if not verify_id:
                return {"message":"Question Id not found"},404

            upvote = self.upvotemodel.upvote_question(int(questionid))
            return {"upvote success": upvote},204
        except KeyError:
            return make_response(jsonify({"status": 500, "error": "Expecting a field key"}),500)
class DownvoteQuestion(Resource):
    """ a user should  be able to downvote a question"""
    def __init__(self):
        self.downvotemodel = questionmodel

    def patch(self,id, questionid):
        try:
            verify_id = meetup_validation.validate_meetup_id(int(id))
            if not verify_id:
                return {"message":"Meetup Id not found"},404

            verify_id = meetup_validation.validate_question_id(int(questionid))
            if not verify_id:
                return {"message":"Question Id not found"},404

            down_vote = self.downvotemodel.downvote_question(id= questionid)
            return {"upvote success": down_vote},204
        except:
            return make_response(jsonify({"status": 500, "error": "Expecting a field key"}),500)

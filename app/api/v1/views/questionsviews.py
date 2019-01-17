#inbuilt module
import uuid
#downloaded dependencieds
from flask import jsonify, abort, make_response, request
from flask_restful import Resource
#local imports
from app.api.v1.models.questions import questions_list, QuestionClass
from app.api.v1.utilis.validations import InputValidation

questionmodel = QuestionClass(questions_list)
meetup_validation = InputValidation()

class GetSpecificQuestion(Resource):
    """a user should be able to get a specific question api endpoint"""

    def __init__(self):
        self.model = questionmodel

    def get(self, id, quiz_id):
        """get details of specific meetup"""
        verify_id = meetup_validation.validate_meetup_id(int(id))
        if not verify_id:
            abort(make_response({"message": "Meetup not found"}, 404))

        verify_id = meetup_validation.validate_question_id(int(quiz_id))
        if not verify_id:
            abort(make_response({"message": "Question not found"}, 400))

        question_specific = self.model.get_one_question(int(quiz_id))
        abort(make_response(jsonify({"message": question_specific}), 200))


class PostQuestion(Resource):
    def post(self, q_id):
        """
        user should be able to post a question endpoint
        """
        try:
            data = request.get_json()
            data_state = meetup_validation.check_state(data)
            user = data['user']
            meetup = data['meetup']
            title = data['title']
            body = data['body']
            public_id = str(uuid.uuid4())
            question_id = len(questions_list)+1

            if data['user'] == "":
                abort(make_response({"message": "Input Username please"}), 400)
            if data['meetup'] == "":
                abort(make_response({"message": "Input Meetup name please"}), 400)
            if data['title'] == "":
                abort(make_response({"message": "Input Question Title  please"}), 400)
            if data['body'] == "":
                abort(make_response({"message": "Input your Question Please"}), 400)
            
            question_validity = meetup_validation.validate_question_exist(body)
            if question_validity:
                abort(make_response({"message": "Question already exist ."}, 409))

            verify_id = meetup_validation.validate_meetup_id(int(q_id))
            if not verify_id:
                return {"message": "Meetup not found"}, 400
            question_payload = questionmodel.post_question(
                user, meetup, title, body, public_id, question_id, q_id)
            for q_data in question_payload:
                response = {
                    "question_title": q_data['question_title'],
                    "question_body": q_data['question_body'],
                    "user": q_data['user'],
                    "meetup": q_data['meetup'],
                    "id": q_data['id'],
                    "votes": q_data['votes'],
                    "meetup_id": q_data['meetup_id']
                }
            return make_response(jsonify({
                "status": 201,
                "message": response
            }), 201)
        except KeyError:
            return make_response(jsonify({"status": 409, "error": "Question already exist"}), 409)


class UpvoteQuestion(Resource):
    """ a user should  be able to upvote a question"""

    def __init__(self):
        """constructor"""
        self.upvotemodel = questionmodel

    def patch(self, id, questionid):
        "user upvote  question"
        try:
            verify_id = meetup_validation.validate_meetup_id(int(id))
            if not verify_id:
                return {"message": "Meetup not found"}, 404

            verify_id = meetup_validation.validate_question_id(int(questionid))
            if not verify_id:
                return {"message": "Question not found"}, 404

            upvote = self.upvotemodel.upvote_question(int(questionid))
            return {"upvote success": upvote}, 204
        except KeyError:
            abort(make_response(jsonify({"status": 500, "error": "Expecting a field key"})), 500)
class DownvoteQuestion(Resource):
    """ a user should  be able to downvote a question"""

    def __init__(self):
        """"constructor"""
        self.downvotemodel = questionmodel

    def patch(self, id, questionid):
        """user downvote a question"""
        try:
            verify_id = meetup_validation.validate_meetup_id(int(id))
            if not verify_id:
                return {"message": "Meetup not found"}, 404

            verify_id = meetup_validation.validate_question_id(int(questionid))
            if not verify_id:
                return {"message": "Question not found"}, 404
            down_vote = self.downvotemodel.downvote_question(id=questionid)
            abort(make_response(jsonify({"upvote success":down_vote}), 204))
        except:
             make_response(jsonify({"status": 500, "error": "Expecting a field key"}), 500)

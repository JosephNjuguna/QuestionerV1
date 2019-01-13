from flask import Blueprint,jsonify,make_response
from flask_restful import Resource
from app.api.v1.models.questions import questions_list,QuestionClass

question_api = Blueprint('questions_api',__name__,)

questionmodel = QuestionClass()

@question_api.route('/questions/<string:id>',methods=["GET"])
def get_question(id):
    question_specific = questionmodel.get_one_question(id)
    return make_response(jsonify({"message": question_specific}),200)

@question_api.route('/questions',methods=["POST"])
def question_post():
    return make_response(jsonify({"message":"post questions "}),201)

class UpvoteQuestion(Resource):
    def __init__(self):
        self.upvotemodel = questionmodel

    def patch(self, question_id):
        upvote = self.upvotemodel.upvote_question(id= question_id)
        if not upvote:
            return {
                "status": 404,
                "error": "No question found"
                }, 404
            return {
                "status": 200,
                "data": upvote
            }, 204

@question_api.route('/questions/<string:id>/downvote',methods=["PATCH"])
def downvoteQuestion(id):
    return make_response(jsonify({"message":" downvote a question"}),204)


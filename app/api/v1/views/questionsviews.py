from flask import Flask, Blueprint, jsonify, make_response, request
from flask_restful import Resource

from app.api.v1.models.questions import questions_list,QuestionClass

question_api = Blueprint('questions_api',__name__,)

questionmodel = QuestionClass()

@question_api.route('/questions/<string:id>',methods=["GET"])
def get_question(id):
    question_specific = questionmodel.get_one_question(id)
    return make_response(jsonify({"message": question_specific}),200)

class PostQuestion(Resource):

    def question_post(self):
        """
        user can post question api endpoint
        """
        data = request.get_json()
        user = data['user']
        meetup= data['meetup']
        title=data['title']
        body=data['body']

        for k,v in data.items():
            if len(k) == 0:
                return make_response(jsonify({"message":"Please recheck your data"}))

        question_payload = questionmodel.post_question(user,meetup,title,body)
        
        return make_response(jsonify({"message":question_payload}),201)
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
class DownvoteQuestion(Resource):
    def __init__(self):
        self.downvotemodel = questionmodel

    def patch(self, question_id):
        downvote = self.downvotemodel.downvote_question(id= question_id)
        if not downvote:
            return {
                "status": 404,
                "error": "No question found"
                }, 404
            return {
                "status": 200,
                "data": downvote
            }, 204

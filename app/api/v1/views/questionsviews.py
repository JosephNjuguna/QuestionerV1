from flask import Flask,Blueprint,jsonify,make_response
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
  
@question_api.route('/questions/<string:id>/upvote',methods=["PATCH"])
def upvoteQuestion(id):
    return make_response(jsonify({"message":"please upvote a question"}),204)

@question_api.route('/questions/<string:id>/downvote',methods=["PATCH"])
def downvoteQuestion(id):
    return make_response(jsonify({"message":" downvote a question"}),204)


from flask import Flask,Blueprint,jsonify,make_response
question_api = Blueprint('questions_api',__name__,)

@question_api.route('/questions/<string:id>/upvote',methods=["GET"])
def upvoteQuestion(id):
    return make_response(jsonify({"message":"get details of specific question"}),200)

@question_api.route('/questions',methods=["POST"])
def question_post():
    return make_response(jsonify({"message":"post questions "}),201)

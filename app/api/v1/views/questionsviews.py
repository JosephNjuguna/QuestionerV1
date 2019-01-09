from flask import Flask,Blueprint,jsonify,make_response
question_api = Blueprint('questions_api',__name__,)

@question_api.route('/questions',methods=["POST"])
def question_post():
    return make_response(jsonify({"message":"post questions "}),201)
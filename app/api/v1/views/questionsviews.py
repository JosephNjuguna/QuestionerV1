from flask import Flask,Blueprint,jsonify,make_response
question_api = Blueprint('questions_api',__name__,)

@question_api.route('/questions/<string:id>/upvote',methods=["PATCH"])
def upvoteQuestion(id):
    return make_response(jsonify({"message":"please upvote a question"}),204)

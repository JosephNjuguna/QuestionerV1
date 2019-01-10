from flask import Flask,Blueprint,jsonify,make_response,json, request
from app.api.v1.models.questions import QuestionClass

question_api = Blueprint('questions_api',__name__,)

questionsclass = QuestionClass()


@question_api.route('/questions',methods=["POST"])
def question_post():
    data = request.get_json()
    user= len(data)+1
    meetup= len(data) +1
    title = data['title']
    body = data['body']

    if user == "" or title == "" or body == "":
        return "Field cant be empty",400

    questiondata = questionsclass.post_question(user,meetup,title,body)
    return make_response(jsonify({"successfully posted a question": questiondata }),201)
  
@question_api.route('/questions/<string:id>/upvote',methods=["PATCH"])
def upvoteQuestion(id):
    return make_response(jsonify({"message":"please upvote a question"}),204)

@question_api.route('/questions/<string:id>/downvote',methods=["PATCH"])
def downvoteQuestion(id):
    return make_response(jsonify({"message":" downvote a question"}),204)


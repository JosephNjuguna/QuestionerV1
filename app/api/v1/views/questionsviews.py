from flask import Flask,Blueprint,jsonify,make_response,request
from app.api.v1.models.questions import questions_list,QuestionClass

question_api = Blueprint('questions_api',__name__,)

questionmodel = QuestionClass()

@question_api.route('/questions/<string:id>',methods=["GET"])
def get_question(id):
    question_specific = questionmodel.get_one_question(id)
    return make_response(jsonify({"message": question_specific}),200)

@question_api.route('/questions',methods=["POST"])
def question_post():
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

@question_api.route('/questions/<string:id>/upvote',methods=["PATCH"])
def upvoteQuestion(id):
    """
    user can upvote a question
    """
    return make_response(jsonify({"message":"please upvote a question"}),204)

@question_api.route('/questions/<string:id>/downvote',methods=["PATCH"])
def downvoteQuestion(id):
    """
    user can downvote a question
    """
    return make_response(jsonify({"message":" downvote a question"}),204)
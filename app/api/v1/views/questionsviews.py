@question_api.route('/questions/<string:id>/upvote',methods=["PATCH"])
def upvoteQuestion(id):
    return make_response(jsonify({"message":"please upvote a question"}),204)

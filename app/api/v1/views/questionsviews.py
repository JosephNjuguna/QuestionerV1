@question_api.route('/questions/<string:id>/upvote',methods=["GET"])
def upvoteQuestion(id):
    return make_response(jsonify({"message":"get details of specific question"}),200)

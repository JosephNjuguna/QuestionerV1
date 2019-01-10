questions_list= []

class QuestionClass():
    def post_question(self, user, meetup, title, body):
        payload = {
            'status' : 201,
            'data' : [{
                "user":user,
                "meetup":meetup,
                "questiontitle":title,
                "questionbody": body
            }]
        }
        questiondata =  user_list.append(payload)
        return True

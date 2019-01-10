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
        questiondata =  questions_list.append(payload)
        return True
    
    def get_one_question(self,id):
        question_id = [quiz for quiz in questions_list if quiz[id]== id]
        if not  question_id:
            return False
        return question_id
        

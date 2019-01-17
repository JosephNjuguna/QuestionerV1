from app import app
from flask import jsonify

app = app

@app.route('/' , methods =["GET"])
def welcome():
   return jsonify({"a welcome message":"Welcome to Questioner V1 API", 
    "sign up":"/api/v1/auth/signup",
    "log in":"/api/v1/auth/login", 
    "create meetup":"/api/v1/meetup", 
    "get upcoming meetup":"/api/v1/meetup/upcoming",
    "get specific meetup":"/api/v1/meetup/id", 
    "user rsvp":"/api/v1/meetup/id/rsvp", 
    "post question":"/api/v1/meetup/id/question",
    "get specific question":"/api/v1/meetup/id/question/id",
    "upvote":"/api/v1/meetup/1/question/id/upvote",
    "downvote":"/api/v1/meetup/1/question/id/downvote"
})
if __name__ == '__main__':
    app.run(debug=True)
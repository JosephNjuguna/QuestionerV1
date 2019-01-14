from app import app
from flask import jsonify

app = app

@app.route('/' , methods =["GET"])
def welcome():
    return jsonify({"Welcome to Questioner api":"here are the endpoints for my api",
                    "sign up" :"/api/v1/auth/signup",
                    "log in":"/api/v1/auth/login",
                    "create meetup": "/api/v1/meetup/rsvp",
                    "get specific meetup endpoint": "/api/v1/meetup/<string:id>",
                    "meet up rsvp":"/api/v1/meetup/rsvp",
                    "upvote question":"/api/v1/questions/<string:id>/upvote",
                    "downvote question": "/questions/<string:id>/downvote",
                    "post question": "/api/v1/question"
        })
if __name__ == '__main__':
    app.run(debug=True)
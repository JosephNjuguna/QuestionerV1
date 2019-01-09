from flask import Flask,Blueprint,jsonify, make_response

users_api = Blueprint('users_api',__name__,)

@users_api.route('/auth/signup',methods=["GET"])
def signup():
    return make_response(jsonify({"message": "welcome to users sign up"}),201)


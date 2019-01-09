from flask import Flask,Blueprint,jsonify,make_response

question_api = Blueprint('questions_api',__name__,)
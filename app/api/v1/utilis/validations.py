# inbuilt modules
import re
import os
from functools import wraps

# third party modules
from flask import jsonify, request, make_response, abort 
import jwt

# local imports
from app.api.v1.models.users import users_list
from app.api.v1.models.meetup import meetup_list
from app.api.v1.models.questions import questions_list

DB = users_list
db_meetup = meetup_list
db_questions = questions_list


class InputValidation():
    """Validators Class"""

    def check_state(self, data):
        for k, v in data.items():
            if v == "":
                return jsonify({"status": 400, "error": "empty fields"}, 400)

    def valid_name(self, name):
        """validate username"""
        regex = "^[a-zA-Z]{4,}$"
        return re.match(regex, name)

    def check_username(self, username):
        """Method for checking if username exist"""
        user = [user for user in DB if user['firstname'] == username]
        if user:
            return True
        return False

    def valid_email(self, email):
        """ valid email """
        regex = "^[\w]+[\d]?@[\w]+\.[\w]+$"
        return re.match(regex, email)

    def check_email(self, email):
        """Method for checking if user email exist"""
        user = [user for user in DB if user['email'] == email]
        if user:
            return user

    def valid_password(self, password):
        """ valid password """
        regex = "^[a-zA-Z0-9@_+-.]{5,}$"
        return re.match(regex, password)

    def validate_meetup_exist(self,topic):
        for i in db_meetup:
            if i['topic'] == topic:
                return True
        return False
    
    def validate_meetup_id(self,id):
        for i in db_meetup:
            if i['id'] == id:
                return True
        return False
    
    def validate_question_exist(self,body):
        for i in db_questions:
            if i['body'] == body:
                return True
        return False

    def validate_question_id(self, quiz_id):
        for i in db_questions:
            if i['id'] == quiz_id:
                return True 
        return False 

    def token_required(self, f):
        @wraps(f)
        def decorated(*args, **kwargs):
            token = None
            if 'x-access-token' in request.headers:
                token = request.headers['x-access-token']
            if not token:
                return jsonify({'message': "Token is missing"})
            try:
                data = jwt.decode(token, os.getenv("SECRET_KEY"))
                current_user = [
                    user for user in DB if user['public_id'] == data['public_id']]
            except:
                return jsonify({'message': "Token invalid"})
            return f(current_user, *args, **kwargs)
        return decorated

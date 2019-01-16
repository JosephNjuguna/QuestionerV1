from flask import jsonify, make_response,request
from flask_restful import Resource
from werkzeug.security import generate_password_hash,check_password_hash

from app.api.v1.models.users import UsersModels, userslist
from app.api.v1.utilis.validations import InputValidation
import datetime

date = datetime.datetime.utcnow()
validation = InputValidation()

class Signup(Resource):
    """a user sign up endpoint"""
    def __init__(self):
        self.db = userslist
        self.model = UsersModels()

    def post(self):
        try:
            data = request.get_json()
            validation.check_state(data)
            firstname = data["firstname"]
            lastname = data["lastname"]
            email = data["email"]
            password = data["password"]
            confirm_password = data["confirm_password"]
            if not validation.valid_name(firstname):
                return {'message': "check username: should be 4 words or more"}, 400
            check_name = validation.check_username(firstname)
            if check_name:
                return {'message': 'That username exists. use a unique username'}, 400

            # Checks if email is valid
            if not validation.valid_email(email):
                return {'message': "enter a valid email "}, 400
            check_email = validation.check_email(email)
            if check_email:
                return {'message': 'email already exist'}, 400
            if not validation.valid_password(password):
                return {'message': "confirm your password"}, 400
            if confirm_password != password:
                return {"message": "check your passwords please"}, 400
            hashpassword = generate_password_hash(password)
            data = self.model.sign_up_user(firstname, lastname, email, hashpassword, confirm_password)
            for userdata in data:
                response = {"firstname": userdata["firstname"]}
            return {"status": 201,
                "message": "User successfully created", 
                "user data": response}, 201
        except KeyError:
            return make_response(jsonify({"status": 500, "error": "Expecting a field key"}),500)

class Login(Resource):
    """a user log in """
    def __init__(self):
        self.db = userslist
        self.model = UsersModels()
    def post(self):
        try:
           
            data = request.get_json()
            validation.check_state(data)
            email = data['email']
            password = data['password']
            if not validation.valid_email:
                return {'message': "email should be valid"}, 400
            if not validation.check_email(email):
                return {'message': 'That email does not exist. Register'}, 404
            result = validation.check_email(email)
            for userdata in result:
                userpass = userdata["password"]
            if check_password_hash(userpass, password):
                return {"status": 200, "message": "Log in success"},200
            return {"message": "Incorrect Password "}, 400
        
        except KeyError:
            return make_response(jsonify({"status": 500, "error": "Expecting a field key"}),500)


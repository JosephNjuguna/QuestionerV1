"""user views"""
#inbuilt mofules
import datetime
#downloaded dependecies
from flask import jsonify, make_response, request,abort
from flask_restful import Resource
#local imports
from app.api.v1.models.users import UsersModels, users_list
from app.api.v1.utilis.validations import InputValidation

date = datetime.datetime.utcnow()
validation = InputValidation()

class Signup(Resource):
    """a user sign up endpoint"""

    def __init__(self):
        self.db = users_list
        self.model = UsersModels()

    def post(self):
        '''create a new user'''
        try:
            data = request.get_json()
            data_state = validation.check_state(data)

            firstname = data["firstname"]
            lastname = data["lastname"]
            email = data["email"]
            password = data["password"]
            confirm_password = data["confirm_password"]

            if data["firstname"] == "":
               return make_response(jsonify({"message":"Username empty"}),400)
            if not validation.valid_name(firstname):
                return make_response(jsonify({'message': "Username length too short,should be 4 letters or more"}), 400)
            check_name = validation.check_username(firstname)
            if check_name:
                return make_response(jsonify({'message': 'Username already exists.'}), 409)
            # Checks if email is valid
            if not validation.valid_email(email):
                return make_response(jsonify( {'message': "Enter a valid email"}), 400)
            check_email = validation.check_email(email)
            if check_email:
                return make_response(jsonify({'message': 'Email already exist'}), 409)
            if not validation.valid_password(password):
                return {'message': "confirm your password"}, 400
            if confirm_password != password:
                return {"message": "Invalid Password.Check your passwords please"}, 400
            user_data = self.model.sign_up_user(
                firstname, lastname, email, password, confirm_password)
            for userdata in user_data:
                response = {
                    "firstname": userdata["firstname"],
                    "lastname": userdata["lastname"],
                    "email": userdata["email"],
                    "password": userdata["password"]
                }
            return {"status": 201,
                    "message": "User successfully created",
                    "user data": response}, 201

        except KeyError:
            abort(make_response(jsonify({"status": 500, "error": "Expecting a field key"}), 500))

class Login(Resource):
    """a user log in """

    def __init__(self):
        """constructor"""
        self.db = users_list
        self.model = UsersModels()

    def post(self):
        '''log in nes user'''
        try:

            data = request.get_json()
            data_state = validation.check_state(data)
            email = data['email']
            password = data['password']
            if not validation.valid_email:
                return {'message': "email should be valid"}, 400
            if not validation.check_email(email):
                return {'message': 'Email not found. Please check email or Register'}, 404
            result = validation.check_email(email)
            for userdata in result:
                userpass = userdata["password"]
            if userpass == password:
                return {"status": 200, "message": "Log in successful"}, 200
            return {"message": "Incorrect Password "}, 400

        except KeyError:
            return make_response(jsonify({"status": 500, "error": "Expecting a field key"}), 500)

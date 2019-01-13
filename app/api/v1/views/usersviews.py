from flask import jsonify, make_response,request
from flask_restful import Resource

from app.api.v1.models.users import UsersModels, userslist
import datetime

usermodel = UsersModels()
userdata = userslist

class Signup(Resource):
   
    def post(self):
        date = datetime.datetime.utcnow()
        data = request.get_json()

        id = len(data)+2
        firstname = data['firstname']
        lastname = data['lastname']
        email = data['email']
        password = data['password']
        confirmpassword = data['password']
        registered = date 
        isAdmin = False

        if firstname == "" or lastname == "" or email == "" or password == "" or confirmpassword == "":
            return make_response(jsonify({"message":"Field cant be empty"}),400)

        userdata = usermodel.sign_up_user(firstname,lastname,email,password,confirmpassword, registered, isAdmin)
        return make_response(jsonify({"message":userdata}),201)

class Login(Resource):

    def __init__(self):
        self.db = userdata

    def post(self):
        data = request.get_json()
        email = data['email']
        password = data['password']

        if email == "" or password == "":
            return make_response(jsonify({"message":"Field cant be empty"}),400)

        user_authentcation = [user for user in userdata if user['password'] == password and  user['email'] ==  email]
        if user_authentcation:
            return make_response(jsonify({"message":"User logged in succcessfully" }),200)
        return make_response(jsonify({"message": "Authentication Failed"}),401)

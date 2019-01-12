from flask_restful import Api, Resource
from flask import Blueprint

from .views import Signup, Login, Questions, Meetup,

version_one = Blueprint('api_v1', __name__)
api = Api(version_one)

api.add_resource(Signup, '/auth/signup')
api.add_resource(Login, '/auth/login' , '/auth/logout')
api.add_resource(Questions, '/questions', '/questions/<string:public_id>')

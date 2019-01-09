from flask import Flask

app = Flask(__name__)

from app.api.v1.views.usersviews import users_api as users_blueprint
from app.api.v1.views.questionsviews import question_api as question_blueprint
from app.api.v1.views.meetupviews import meetup_api as meetup_blueprint

app.register_blueprint(users_blueprint, url_prefix='/api/v1')
app.register_blueprint(question_blueprint, url_prefix='/api/v1')
app.register_blueprint(meetup_blueprint, url_prefix='/api/v1')

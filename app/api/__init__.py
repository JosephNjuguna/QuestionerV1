from flask import Flask

app = Flask(__name__)

from app.api.v1 import version_one as questioner1

app.register_blueprint(questioner1, url_prefix='/api/v1')
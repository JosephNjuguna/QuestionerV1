from app import app
from flask import jsonify

app = app

@app.route('/welcome' , methods =["GET"])
def welcome():
    return jsonify({"Welcome to Questioner api":"here are the endpoints for my api"})

if __name__ == '__main__':
    app.run(debug=True)
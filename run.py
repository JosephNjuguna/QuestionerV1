from app import app

app = app

@app.route('/')
def welcome():
    return "Welcome to Questioner api"

if __name__ == '__main__':
    app.run(debug=True)
from app import app

app = app

@app.route('/')
def welcome():
    return "welcome to Quesioner API "

if __name__ == '__main__':
    app.run()
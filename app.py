from falsk import Flask
app = Flask(_name_)

@app.route('/')
def hello_world():
    return 'hello, Simple Flask application'
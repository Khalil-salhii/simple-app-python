from flask import Flask
app = Flask(__name__)  # Correction: __name__ au lieu de _name_

@app.route('/')
def hello_world():
    return 'hello, Simple Flask application'
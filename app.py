from flask import Flask, jsonify
from envparse import env

env.read_envfile()

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/json')
def json_hello_world():
    return jsonify({
        "message": "Hello, World!"
    }), 200

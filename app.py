from flask import Flask
from envparse import env

env.read_envfile()
 
app = Flask(__name__)
 
@app.route('/')
def hello_world():
  return 'Hello, World!'

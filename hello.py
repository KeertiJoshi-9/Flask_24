from flask import Flask

app = Flask(__name__)

@app.route('/')
def func1():
    return("This is the main homepage - Hello, Keerti!")

@app.route('/ping', methods=['GET'])
def func2():
    return("This is the ping page - Ping, KSJ!")



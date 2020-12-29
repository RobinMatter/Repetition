from flask import Flask, jsonify, request
app = Flask(__name__)


@app.route("/")
def welcome():
  return "Welcome to TimeElement"

#@app.route("/math")
#def math():
#  return "calculator: "


math = [
  { "1 + 1": 1+1}
]


@app.route('/math')
def get_math():
  return  jsonify(math)


@app.route('/math', methods=['POST'])
def add_math():
  math.append(request.get_json())
  return '', 204
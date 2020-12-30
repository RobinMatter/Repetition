from flask import Flask, jsonify, request
app = Flask(__name__)


@app.route("/")
def welcome():
  return "Welcome to TimeElement"

#@app.route("/math")
#def math():
#  return "calculator: "

def add(x, y):
  result = x + y
  return result

x = 4
math = [
  {  x "+" "y": add(2,3)}
]


@app.route('/math')
def get_math():
  return  jsonify(math)


@app.route('/math', methods=['POST'])
def add_math():
  math.append(request.get_json())
  return '', 204

########################################################################################################################
#def add(x, y):
# return x + y

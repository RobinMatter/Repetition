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


math = [
  {"result1": add(2,3)},
  {"result2": add(6,5)}
]

@app.route('/math')
def get_math():
  return  jsonify(math)


@app.route('/math', methods=['POST'])
def add_math():
  new_key = ''

  result = request.get_json()
  assert len(result) == 1
  for r in result:
    new_key = r

  found = False
  for element in math:
    if new_key in element.keys():
      print("Add", new_key)
      element[new_key] = add(element[new_key],result[new_key])
      found = True

  if found == True:
    math.append(result)

  return '', 204
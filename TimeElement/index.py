from flask import Flask, jsonify, request
app = Flask(__name__)



@app.route("/")
def welcome():
  return "Welcome to TimeElement"



def add(x, y):
  result = x + y
  return result


list = [
  {"result1": add(2,3)},
  {"result2": add(6,5)}
]


@app.route('/additor')
def get_additor():
  return  jsonify(list)


@app.route('/additor', methods=['POST'])
def add_additor():
  new_key = ''

  input = request.get_json()
  assert len(input) == 1
  for r in input:
    new_key = r

  found = False
  for element in list:
    if new_key in element.keys():
      print("Add", new_key)
      element[new_key] = add(element[new_key],input[new_key])
      found = True

  if found == False:
    list.append(input)

  return '', 204
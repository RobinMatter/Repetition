from flask import Flask, jsonify, request
app = Flask(__name__)



@app.route("/")
def welcome():
  return "Welcome to TimeElement"


########################################################################################################################
#plus

def add(x, y):
  result = x + y
  return result



list_add = [
  {"result1": add(2,3)},
  {"result2": add(6,5)}
]


@app.route('/calculator/plus')
def get_additor():
  return  jsonify(list_add)


@app.route('/calculator/plus', methods=['POST'])
def add_additor():
  new_key = ''

  input = request.get_json()
  assert len(input) == 1
  for r in input:
    new_key = r

  found = False
  for element in list_add:
    if new_key in element.keys():
      print("Add", new_key)
      element[new_key] = add(element[new_key],input[new_key])
      found = True

  if found == False:
    list_add.append(input)

  return '', 204

########################################################################################################################
#minus
def sub(x, y):
  result = x - y
  return result


list_sub = [
  {"result1": sub(8,3)},
  {"result2": sub(6,5)}
]

@app.route('/calculator/minus')
def get_substrator():
  return  jsonify(list_sub)


@app.route('/calculator/minus', methods=['POST'])
def add_substrator():
  new_key = ''

  input = request.get_json()
  assert len(input) == 1
  for r in input:
    new_key = r

  found = False
  for element in list_sub:
    if new_key in element.keys():
      print("sub", new_key)
      element[new_key] = sub(element[new_key],input[new_key])
      found = True

  if found == False:
    list_sub.append(input)

  return '', 204


########################################################################################################################
#divide
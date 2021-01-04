import self as self
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
def get_addition():
  return  jsonify(list_add)

def add_addition():
  new_key = ''

  input = request.get_json()
  assert len(input) == 1
  for r in input:
    new_key = r

  found = False
  for element in list:
    if new_key in element.keys():
      element[new_key] = operator(element[new_key],input[new_key])
      found = True

  if found == False:
    list.append(input)

  return '', 204


list = list_add
operator = add

@app.route('/calculator/plus', methods=['POST'])
add_addition()
########################################################################################################################
#minus
def sub(x, y):
  result = x - y
  return result


list_sub = [
  {"result1": sub(8,3)},
  {"result2": sub(6,20)}
]

@app.route('/calculator/minus')
def get_substraction():
  return  jsonify(list_sub)


@app.route('/calculator/minus', methods=['POST'])
def add_substraction():
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

def div(x, y):
  result = x / y
  return result


list_div = [
  {"result1": div(9,3)},
  {"result2": div(24,2)}
]

@app.route('/calculator/divide')
def get_division():
  return  jsonify(list_div)


@app.route('/calculator/divide', methods=['POST'])
def add_division():
  new_key = ''

  input = request.get_json()
  assert len(input) == 1
  for r in input:
    new_key = r

  found = False
  for element in list_div:
    if new_key in element.keys():
      print("div", new_key)
      if input[new_key] == 0:
        raise Exception("You can't divide by 0")
      else:
        element[new_key] = div(element[new_key],input[new_key])
        found = True

  if found == False:
    list_div.append(input)

  return '', 204


########################################################################################################################
#multiply

def mul(x, y):
  result = x * y
  return result


list_mul = [
  {"result1": mul(8,3)},
  {"result2": mul(6,5)}
]

@app.route('/calculator/multiply')
def get_multiplication():
  return  jsonify(list_mul)


@app.route('/calculator/multiply', methods=['POST'])
def add_multiplication():
  new_key = ''

  input = request.get_json()
  assert len(input) == 1
  for r in input:
    new_key = r

  found = False
  for element in list_mul:
    if new_key in element.keys():
      print("mul", new_key)
      element[new_key] = mul(element[new_key],input[new_key])
      found = True

  if found == False:
    list_mul.append(input)

  return '', 204


########################################################################################################################

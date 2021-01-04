import self as self
from flask import Flask, jsonify, request
app = Flask(__name__)

def key_from_element(element):
  assert len(element) == 1
  for key in element:
    return key

class DataStore:

  def __init__(self):
    self.__data_list = []

  def append(self, element):
    self.__data_list.append(element)

  def sum(self, key, value1, value2):
    element = {}
    element[key] = value1 + value2
    self.append(element)


  def add(self, key, value):
    element = {}
    element[key] += value
    self.append(element)


  def dif(self, key, value1, value2):
    element = {}
    element[key] = value1 - value2
    self.append(element)


  def get_list(self):
    return self.__data_list

  def get_keys(self):
    keys = {}
    for element in self.__data_list:
      key_element = ''
      for r in element:
        key_element = r
      keys[key_element] = True
    return keys

  def exist(self, key):
    if key in self.get_keys():
      return True
    else:
      return False


@app.route("/")
def welcome():
  return "Welcome to TimeElement"


########################################################################################################################
#plus

def add(x, y):
  result = x + y
  return result


bank_data = DataStore()
bank_data.sum("result1", 2, 3)
bank_data.sum("result1", 6, 5)
bank_data.sum("result1", 8, 5)


@app.route('/calculator/plus')
def get_addition():
  return  jsonify(bank_data.get_list())


@app.route('/calculator/plus', methods=['POST'])
def add_addition():
  element = request.get_json()
  key = key_from_element(element)

  if bank_data.exist(key):
    bank_data.add(key, element[key])
  else:
    bank_data.append(element)

  return '', 204

########################################################################################################################
#minus


post_data = DataStore()
post_data.dif("result1", 8, 3)
post_data.dif("result2", 6, 20)


@app.route('/calculator/minus')
def get_substraction():
  return  jsonify(post_data.get_list())


@app.route('/calculator/minus', methods=['POST'])
def add_substraction():
  new_key = ''

  input = request.get_json()
  new_key = key_from_element(input)

  found = False
  for element in post_data.get_list():
    if new_key in element.keys():
      print("sub", new_key)
      element[new_key] = sub(element[new_key],input[new_key])
      found = True

  if found == False:
    post_data.append(input)

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
  new_key = key_from_element(input)

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
  new_key = key_from_element(input)

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
#main


list_main = [
  {"result1": add(2,3)},
  {"result2": add(6,5)}
]
list_main = bank_data.get_list() + post_data.get_list()

@app.route('/calculator/main')
def get_main():
  dic = {}
  for element in list_main:
    key = ''
    for r in element:
      key = r

    if key in dic:
      dic[key] = dic[key] + element[key]
    else:
      dic[key] = element[key]
  return  jsonify(dic)
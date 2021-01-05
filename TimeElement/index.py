import self as self
from flask import Flask, jsonify, request

app = Flask(__name__)


def key_from_element(element):
    assert len(element) == 1
    for key in element:
        return key


def combine_two_lists(key, dic, element, value):
    if key in dic:
        dic[key] = dic[key] + value
    else:
        dic[key] = element[key]

def get_directory_with_elements_from_two_lists(list1, list2):
    list_main = list1 + list2
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

    def quo(self, key, value1, value2):
        element = {}
        if value2 == 0:
            raise Exception("You can't divide by 0")
        else:
            element[key] = value1 / value2
            self.append(element)

    def mul(self, key, value1, value2):
        element = {}
        element[key] = value1 * value2
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
# plus

def add(x, y):
    result = x + y
    return result


bank_data = DataStore()
bank_data.sum("result1", 2, 3)
bank_data.sum("result1", 6, 5)
bank_data.sum("result1", 8, 5)


@app.route('/calculator/plus')
def get_addition():
    return jsonify(bank_data.get_list())


@app.route('/calculator/plus', methods=['POST'])
def add_addition():
    element = request.get_json()
    print(element)
    key = key_from_element(element)

    if bank_data.exist(key):
        bank_data.add(key, element[key])
    else:
        bank_data.append(element)

    return '', 204


########################################################################################################################
# minus


post_data = DataStore()
post_data.dif("result1", 8, 3)
post_data.dif("result2", 6, 20)


@app.route('/calculator/minus')
def get_substraction():
    return jsonify(post_data.get_list())


@app.route('/calculator/minus', methods=['POST'])
def add_substraction():
    element = request.get_json()
    key = key_from_element(element)

    if post_data.exist(key):
        post_data.add(key, element[key])
    else:
        post_data.append(element)

    return '', 204


########################################################################################################################
# divide

def div(x, y):
    result = x / y
    return result

kred_data = DataStore()
kred_data.quo("result1", 9, 3)
kred_data.quo("result2", 8, 2)


@app.route('/calculator/divide')
def get_division():
    return jsonify(kred_data.get_list())



@app.route('/calculator/divide', methods=['POST'])
def add_division():
    new_key = ''

    element = request.get_json()
    key = key_from_element(element)
    if kred_data.exist(key):
        kred_data.quo(key, element[key])
    else:
        kred_data.append(element)

    return '', 204




########################################################################################################################
# multiply

def mul(x, y):
    result = x * y
    return result

deb_data = DataStore()
deb_data.mul("result1", 8, 3)
deb_data.mul("result2", 6, 5)


@app.route('/calculator/multiply')
def get_multiplication():
    return jsonify(deb_data.get_list())


@app.route('/calculator/multiply', methods=['POST'])
def add_multiplication():
    new_key = ''

    input = request.get_json()
    new_key = key_from_element(input)

    element = request.get_json()
    key = key_from_element(element)
    if deb_data.exist(key):
        deb_data.mul(key, element[key])
    else:
        deb_data.append(element)

    return '', 204


########################################################################################################################
# main


list_main = [
    {"result1": add(2, 3)},
    {"result2": add(6, 5)}
]



@app.route('/calculator/main')
def get_main():
    get_directory_with_elements_from_two_lists(bank_data.get_list(),  post_data.get_list())







# def combine_two_lists(key, dic, element, value):
#     if key in dic:
#         dic[key] = dic[key] + value
#     else:
#         dic[key] = element[key]
#


# @app.route('/calculator/main')
# def get_main():
#   dic = {}
#   for element in list_main:
#     key = ''
#     key_from_element(element)
#     combine_two_lists(key, dic, element, element[key])
#   return  jsonify(dic)
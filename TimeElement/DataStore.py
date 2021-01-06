

def key_from_element(element):
    assert len(element) == 1
    for key in element:
        return key


class DataStore:
    def __init__(self):
        self.__data_list = []

    def append(self, element):
        self.__data_list.append(element)

    def get_value(self, key):
        pass

    def sum(self, key, value1, value2):
        element = {key: value1 + value2}
        self.append(element)

    def add(self, key, value):
        element = {}
        element[key] += value
        self.append(element)

    def dif(self, key, value1, value2):
        element = {key: value1 - value2}
        self.append(element)

    def quo(self, key, value1, value2):
        if value2 == 0:
            raise ZeroDivisionError("You can't divide by 0")
        element = {key: value1 / value2}
        self.append(element)

    def mul(self, key, value1, value2):
        element = {key: value1 * value2}
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

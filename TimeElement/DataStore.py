class DataStore:
    def __init__(self):
        self.__data_list = []

    def get_value(self, key):
        for element in self.__data_list:
            key_from_element = list(element)[0]
            if key == key_from_element:
                return element[key], True
        else:
            return 0, False

    def add(self, key, value):
        '''increase value for an existing element or develop a new element'''
        for element in self.__data_list:
            if key == list(element)[0]:
                element[key] += value
                break
        else:
            self.__data_list.append({key: value})

    def min(self, key, value):
        self.add(key, -value)

    def sum(self, key, value1, value2):
        value = value1 + value2
        self.add(key, value)

    def dif(self, key, value1, value2):
        self.sum(key, value1, -value2)

    def quo(self, key, value1, value2):
        if value2 == 0:
            raise ZeroDivisionError("You can't divide by 0")
        value = value1 / value2
        self.add(key, value)

    def mul(self, key, value1, value2):
        value = value1 * value2
        self.add(key, value)

    def get_list(self):
        return self.__data_list

    def get_keys(self):
        keys = []
        for element in self.__data_list:
            key = list(element)[0]
            keys[key] = True
        return keys

    def exist(self, key):
        if key in self.get_keys():
            return True
        else:
            return False

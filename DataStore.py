import json

class DataStore:
    def __init__(self):
        f = open("data.json")
        contents = f.read()
        f.close()
        self.__data_list = []


    def get_value_of_account_balance(self, key):
        f = open("data.json")
        contents = f.read()
        f.close()
        for element in contents:
            key_from_element = list(element)[0]
            if key == key_from_element:
                return element[key], True
        else:
            return 0, False

    def add_income_to_account_balance(self, key, value):
        """increase value for an existing element or develop a new element"""
        r = []
        with open("data.json") as jsonfile:
            contents = jsonfile.read()
            r = json.loads(contents)
            jsonfile.close()
        print("p3", key, value, r)
        for element in r:
            print("y3", key, value, element)
            if key == list(element)[0]:
                element[key] += value
                break
        else:
            print("h3", key, value)
            r.append({key: value})
            with open('data.json', 'w') as jsonfile:
                json.dump(r, jsonfile)

            self.__data_list = r


    def add_expense_to_account_balance(self, key, value):
        self.add_income_to_account_balance(key, -value)

    def add_ROI_to_account_balance(self, key, value):
        """increase value for an existing element or develop a new element"""
        for element in self.__data_list:
            if key == list(element)[0]:
                if value != 0:
                    element[key] = element[key] / value
                break
        else:
            with open('data.json', 'w') as jsonfile:
                json.dump(self.__data_list, jsonfile)
            self.__data_list.append({key: value})

    def add_value_to_account_balance(self, key, value):
        """increase value for an existing element or develop a new element"""
        for element in self.__data_list:
            if key == list(element)[0]:
                element[key] = element[key] * value
                break
        else:
            with open('data.json', 'w') as jsonfile:
                json.dump(self.__data_list, jsonfile)
            self.__data_list.append({key: value})

    def get_account_balance_data(self):
        return self.__data_list

    def get_key_of_account_balance(self):
        keys = []
        for element in self.__data_list:
            key = list(element)[0]
            keys[key] = True
        return keys

    def does_key_exist_in_account_balance(self, key):
        if key in self.get_key_of_account_balance():
            return True
        else:
            return False


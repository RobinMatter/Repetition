import json

class DataStore:
    def __init__(self):
        f = open("data.json")
        contents = f.read()
        f.close()
        self.__data_list = []



    def get_value_of_account_balance(self, key):
        jsonfile = open("data.json")
        data_input = jsonfile.read()
        data = json.loads(data_input)
        jsonfile.close()
        for element in data:
            key_from_element = list(element)[0]
            if key == key_from_element:
                return element[key], True
        else:
            return 0, False

    def add_income_to_account_balance(self, key, value):
        """increase value for an existing element or develop a new element"""
        data = []
        with open("data.json") as jsonfile:
            data_input = jsonfile.read()
            data = json.loads(data_input)
            jsonfile.close()
            print("A", key, value, data)

        for element in self.__data_list:
            print("B", key, value, element)
            if key == list(element)[0]:
                element[key] += value
                data.append({key: value})
                with open('data.json', 'w') as jsonfile:
                    json.dump(data, jsonfile)

                break

        else:
            print("C", key, value, data)
            self.__data_list.append({key: value})
            data.append({key: value})
            with open('data.json', 'w') as jsonfile:
                json.dump(data, jsonfile)




    # def add_income_to_account_balance(self, key, value):
    #     """increase value for an existing element or develop a new element"""
    #     r = []
    #     with open("data.json") as jsonfile:
    #         contents = jsonfile.read()
    #         r = json.loads(contents)
    #         jsonfile.close()
    #     print("p3", key, value, r)
    #     for element in r:
    #         print("y3", key, value, element)
    #         if key == list(element)[0]:
    #             element[key] += value
    #             break
    #     else:
    #         print("h3", key, value)
    #         r.append({key: value})
    #         with open('data.json', 'w') as jsonfile:
    #             json.dump(r, jsonfile)
    #
    #         self.__data_list = r



    def get_account_balance_data(self):
        jsonfile = open("data.json")
        data_input = jsonfile.read()
        self.__data_list = json.loads(data_input)
        jsonfile.close()
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


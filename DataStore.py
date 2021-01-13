class DataStore:
    def __init__(self):
        self.__data_list = []

    def get_value_of_account_balance(self, key):
        for element in self.__data_list:
            key_from_element = list(element)[0]
            if key == key_from_element:
                return element[key], True
        else:
            return 0, False

    def add_income_to_account_balance(self, key, value):
        """increase value for an existing element or develop a new element"""
        for element in self.__data_list:
            if key == list(element)[0]:
                element[key] += value
                break
        else:
            self.__data_list.append({key: value})

    def add_expense_to_account_balance(self, key, value):
        self.add_income_to_account_balance(key, -value)

    def add_ROI_to_account_balance(self, key, value):
        """increase value for an existing element or develop a new element"""
        for element in self.__data_list:
            if key == list(element)[0]:
                element[key] = element[key] / value
                break
        else:
            self.__data_list.append({key: value})

    def add_value_to_account_balance(self, key, value):
        """increase value for an existing element or develop a new element"""
        for element in self.__data_list:
            if key == list(element)[0]:
                element[key] = element[key] * value
                break
        else:
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


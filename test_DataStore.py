from DataStore import DataStore


def add_expense_to_account_balance(self, key, value):
    self.add_income_to_account_balance(key, -value)


def add_two_values_together(self, key, value1, value2):
    value = value1 + value2
    self.add_income_to_account_balance(key, value)


def subtract_first_value_with_second_value(self, key, value1, value2):
    self.add_two_values_together(key, value1, -value2)

class TestDataStore:

    def test_get_value_of_account_balance(self):
        income = DataStore()
        income.add_income_to_account_balance("rent income", 2000)
        income.add_income_to_account_balance("salary", 1500)
        assert income.get_value_of_account_balance("rent income") == (2000, True)


    def test_new_income_source__add_income_to_account_balance(self):
        incomes = DataStore()
        incomes.add_income_to_account_balance("rent income", 2000)
        incomes.add_income_to_account_balance("salary", 1500)
        assert incomes.get_value_of_account_balance("rent income") == (2000, True)

    def test_existing_income_source__add_income_to_account_balance(self):
        incomes = DataStore()
        incomes.add_income_to_account_balance("rent income", 2000)
        incomes.add_income_to_account_balance("rent income", 2200)
        assert incomes.get_value_of_account_balance("rent income") == (4200, True)
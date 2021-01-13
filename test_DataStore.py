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

    def test_new_expense_source__add_income_to_account_balance(self):
        expenses = DataStore()
        expenses.add_expense_to_account_balance("salary", 2000)
        expenses.add_expense_to_account_balance("rent income", 1500)
        assert expenses.get_value_of_account_balance("salary") == (-2000, True)

    def test_existing_expense_source__add_income_to_account_balance(self):
        expenses = DataStore()
        expenses.add_expense_to_account_balance("salary", 2000)
        expenses.add_expense_to_account_balance("salary", 2200)
        assert expenses.get_value_of_account_balance("salary") == (-4200, True)

    def test_new_ROI__add_ROI_to_account_balance(self):
        ROI = DataStore()
        ROI.add_ROI_to_account_balance("flat", 2000)
        assert ROI.get_value_of_account_balance("flat") == (2000, True)

    # def test_existing_ROI__add_ROI_to_account_balance(self):
    #     ROI = DataStore()
    #     ROI.add_ROI_to_account_balance("flat", 2000)
    #     ROI.add_ROI_to_account_balance("flat", 80000)
    #     assert ROI.get_value_of_account_balance("flat") == (0.025, True)

    def test_second_post_0__add_ROI_to_account_balance(self):
        ROI = DataStore()
        ROI.add_ROI_to_account_balance("flat", 2000)
        ROI.add_ROI_to_account_balance("flat", 0)
        assert ROI.get_value_of_account_balance("flat") == (2000, True)

    def test_new_asset_value__add_values_to_estimate_asset_value_to_account_balance(self):
        assets_value = DataStore()
        assets_value.add_value_to_account_balance("gold", 1500)
        assert assets_value.get_value_of_account_balance("gold") == (1500, True)

    def test_existing_asset_value__add_values_to_estimate_asset_value_to_account_balance(self):
        assets_value = DataStore()
        assets_value.add_value_to_account_balance("gold", 1500)
        assets_value.add_value_to_account_balance("gold", 1.2)
        assert assets_value.get_value_of_account_balance("gold") == (1800, True)

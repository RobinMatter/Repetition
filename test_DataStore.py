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
        income.add_income_to_account_balance("salary", 2000)
        income.add_income_to_account_balance("rent income", 1500)
        assert income.get_value_of_account_balance("robin") == (2000, True)


    def test_new_income_source__add_income_to_account_balance(self):
        income = DataStore()
        income.add_income_to_account_balance("salary", 2000)
        income.add_income_to_account_balance("rent income", 1500)
        assert income.get_value_of_account_balance("robin") == (2000, True)

    def test_existing_income_source__add_income_to_account_balance(self):
        income = DataStore()
        income.add_income_to_account_balance("salary", 2000)
        income.add_income_to_account_balance("salary", 2200)
        assert income.get_value_of_account_balance("robin") == (4200, True)

    def test_add_expense_to_account_balance(self):
        income = DataStore()


def test_min(self):
        post_data = DataStore()
        post_data.min("robin", 6)
        assert post_data.get_value("robin") == (-6, True)

    def test_min(self):
        post_data = DataStore()
        post_data.min("robin", 7)
        assert post_data.get_value("robin") == (-1, True)

    def test_sum(self):
        post_data = DataStore()
        post_data.sum("robin", 3, 7)
        assert post_data.get_value("robin") == (9, True)

    def test_sum(self):
        post_data = DataStore()
        post_data.sum("bjorn", 3, 3)
        assert post_data.get_value("bjorn") == (6, True)

    def test_dif(self):
        post_data = DataStore()
        post_data.subtract_first_value_with_second_value("robin", 3, 7)
        assert post_data.get_value("robin") == (5, True)

    def test_dif(self):
        post_data = DataStore()
        post_data.subtract_first_value_with_second_value("julian", 3, 3)
        assert post_data.get_value("julian") == (0, True)

    def test_quo(self):
        post_data = DataStore()
        post_data.add_values_for_ROI("robin", 4, 2)
        assert post_data.get_value("robin") == (7, True)

    def test_quo(self):
        post_data = DataStore()
        post_data.add_values_for_ROI("paul", 6, 3)
        assert post_data.get_value("paul") == (2, True)
        # assert post_data.quo("paul", 8, 0) == None

    def test_mul(self):
        post_data = DataStore()
        post_data.add_values_to_estimate_asset_value("robin", 4, 2)
        assert post_data.get_value("robin") == (15, True)

    def test_mul(self):
        post_data = DataStore()
        post_data.add_values_to_estimate_asset_value("james", 6, 3)
        assert post_data.get_value("james") == (18, True)

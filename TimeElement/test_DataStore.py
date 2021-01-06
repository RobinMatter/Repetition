from DataStore import DataStore

# def key_from_element(element):
#     for key in element:
#         return key


def test_DataStore():
    bank_data = DataStore()
    bank_data.sum("result1", 2, 3)
    bank_data.quo("result1", 2, 4)
    assert [{'result1': 5}, {'result1': 0.5}] == bank_data.get_list()
    bank_data.quo("robin", 4, 2)
    bank_data.quo("robin", 4, 8)
    bank_data.quo("peter", 7, 3)
    #assert bank_data.get_value("peter") == 7/3




# class TestDataStore
#     def test_yo():
#         assert yo(3) == 9
#
# def test_sum():
#     ds = DataStore
#     assert ds.sum('robin', 3, 5) == {'robin': 8}
#
#
# # def test_add():
# #     assert add(7, 3) == 10
# #     assert add(8, 1) == 9
# #     assert add(5, 3) == 8
# #     assert add(2, 11) == 13
# #     assert add(8, 3) == 11
#
#
# def test_sub():
#     assert sub(7, 3) == 4
#     assert sub(8, 1) == 7
#     assert sub(5, 3) == 2
#     assert sub(2, 11) == -9
#     assert sub(8, 8) == 0
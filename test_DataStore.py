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
    # assert bank_data.get_value("peter") == 7/3




def test_DataStore():
    post_data = DataStore()
    #test self.add
    post_data.add("robin", 5)
    post_data.add("robin", 3)
    post_data.add("tim" , 2)
    assert post_data.get_value("robin") == (8, True)

    #test self.min
    post_data.min("robin",2)
    assert post_data.get_value("robin") == (6, True)
    post_data.min("robin", 7)
    assert post_data.get_value("robin") == (-1, True)

    # test self.sum
    post_data.sum("robin", 3, 7)
    assert post_data.get_value("robin") == (9, True)
    post_data.sum("björn", 3, 3)
    assert post_data.get_value("björn") == (6, True)

    # test self.dif
    post_data.dif("robin", 3, 7)
    assert post_data.get_value("robin") == (5, True)
    post_data.dif("julian", 3, 3)
    assert post_data.get_value("julian") == (0, True)

    # test self.quo
    post_data.quo("robin", 4, 2)
    assert post_data.get_value("robin") == (7, True)
    post_data.quo("paul", 6, 3)
    assert post_data.get_value("paul") == (2, True)
    #assert post_data.quo("paul", 8, 0) == None

    # test self.mul
    post_data.mul("robin", 4, 2)
    assert post_data.get_value("robin") == (15, True)
    post_data.mul("james", 6, 3)
    assert post_data.get_value("james") == (18, True)





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

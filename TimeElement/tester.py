
import pytest
from index import key_from_element

# def key_from_element(element):
#     for key in element:
#         return key


def test_key_from_element():
    assert key_from_element({'robin': 8}) == "robin"
    assert key_from_element({'robin': -8}) == "robin"
    assert key_from_element({'robin': 0}) == "robin"

@pytest.fixture(scope='class')
class DataStore:

    def __init__(self):
        self.__data_list = []

    def append(self, element):
        self.__data_list.append(element)

    def sum(self, key, value1, value2):
        element = {}
        element[key] = value1 + value2
        self.append(element)

    def yo(self, value1):
        a = value1 * value1
        return a

class TestDataStore
    def test_yo():
        assert yo(3) == 9

def test_sum():
    ds = DataStore
    assert ds.sum('robin', 3, 5) == {'robin': 8}


# def test_add():
#     assert add(7, 3) == 10
#     assert add(8, 1) == 9
#     assert add(5, 3) == 8
#     assert add(2, 11) == 13
#     assert add(8, 3) == 11
#
#
# def test_sub():
#     assert sub(7, 3) == 4
#     assert sub(8, 1) == 7
#     assert sub(5, 3) == 2
#     assert sub(2, 11) == -9
#     assert sub(8, 8) == 0
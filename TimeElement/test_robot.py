import pytest

def add(x, y):
  result = x + y
  return result




def test_add():
    assert add(7, 3) == 10
    assert add(5, 2) == 7
    assert add(7, 13) == 20
    assert add(6, 3) == 9

import pytest
from index import add, sub




def test_add():
    assert add(7, 3) == 10
    assert add(8, 1) == 9
    assert add(5, 3) == 8
    assert add(2, 11) == 13
    assert add(8, 3) == 11


def test_sub():
    assert sub(7, 3) == 4
    assert sub(8, 1) == 7
    assert sub(5, 3) == 2
    assert sub(2, 11) == -9
    assert sub(8, 8) == 0
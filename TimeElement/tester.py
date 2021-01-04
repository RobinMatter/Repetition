
import pytest
from index import add




def test_add():
    assert add(7, 3) == 10
    assert add(8, 1) == 9
    assert add(5, 3) == 8
    assert add(2, 11) == 13
    assert add(8, 3) == 11
from roboti import name
import pytest

def test_name():
    if name == "Hugo":
        print("11")
        assert False
    else:
        print("22")
        assert True
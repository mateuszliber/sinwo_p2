from main.main import *
import pytest

def test_NWD_simply_data():
    assert NWD(2, 8) == 2

def test_NWD_nulls():
    assert NWD(0, 0) == 0

def test_NWD_negative():
    with pytest.raises(ValueError):
        NWD(-100, 1)

def test_NWD_same():
    assert NWD(100, 100) == 100

def test_false():
    assert NWD(16, 8) == 8

def test_string():
    with pytest.raises(TypeError):
        NWD(10, "ala")
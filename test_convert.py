import pytest

from convert import convert


def test_int_conversion():
    assert convert(1) == 149597870700
    

def test_error():
    with pytest.raises(TypeError):
        convert('1')
        

def test_flaot_conversion():
    assert convert(0.001) == pytest.approx(149587870.691, abs=0.1) # this means any value that is +/- 0.1 will be accepted as equals
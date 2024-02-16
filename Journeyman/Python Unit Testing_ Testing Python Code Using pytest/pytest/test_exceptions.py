import pytest

def divide(dividend, divisor):
	return dividend / divisor

def test_divide_pass():
	assert divide(18, 2) == 9
    
def test_divide_error_zero():
	with pytest.raises(ZeroDivisionError):
		divide(18, 0)
    
def test_divide_error_type():
	with pytest.raises(TypeError):
		divide(18, 'a')
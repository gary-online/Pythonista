import cal

def test_add_int():
    result = cal.add(5, 2)
    assert result == 7
    
def test_add_float():
    result = cal.add(3.2, 2.4)
    assert result == 5.6   
    
def test_add_string():
    result = cal.add('winter', ' season')
    assert result == 'winter season'
import cal
import pytest

@pytest.mark.parametrize('input_1, input_2, result',
                        [(1, 2, 3),
                        (5.2, 2.4, 7.6),
                        ('winter', ' season', 'winter season')])

def test_add(input_1, input_2, result):
    assert cal.add(input_1, input_2) == result
import pytest
from calculator import div, mul, sub, sum 

class TestCal:
    def setup(self):
        pass

    def test_sum(self):
        result = sum(2,3)
        result2 = sum(5,8)

        assert result == 5
        assert result2 > 10

    def test_sub(self):
        result = sub(1,3)

        assert result == -2

    def test_mul(self):
        result = mul(3,5)

        assert result == 15

    def test_div(self):
        result = div(15,5)

        assert result == 3

        with pytest.raises(ZeroDivisionError):
            div(3,0)

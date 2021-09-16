from hi import fizz
import pytest

class TestCal:
    def setup(self):
        pass

    def test_fizz(self):
        fizz(5) 

        return "fizz"

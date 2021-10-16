import pytest


from gerafibo import iter

class Gerafibo:
    def setup(self):
        pass

    def test__iter__(self):
        resultado = 6
        assert resultado == self
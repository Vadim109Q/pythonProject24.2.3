import pytest
from app.calc import Calculator
class TestCals:
    def setup(self):
        self.calc = Calculator

    def test_success_multiply(self):
        assert self.calc.multiply(self, 8, 0) == 0

    def test_success_division(self):
        assert self.calc.division(self, 9, 2) <= 5

    def test_success_subtraction(self):
        assert self.calc.subtraction(self, 9, 3) < 8

    def test_success_adding(self):
        assert self.calc.adding(self, 3, 7) != 8


    def teardown(self):
        print('Тест завершен')
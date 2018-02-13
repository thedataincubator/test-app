from __future__ import division
import unittest
from formulas import quadratic, NumericFormula
import math
class TestFunctions(unittest.TestCase):

    def test_quadratic(self):
        a = 5
        b = 1
        c = 4
        ans = [1/10*1j*(math.sqrt(79) + 1j), -1/10*1j*(math.sqrt(79) - 1j)]
        for calc, actual in zip(quadratic(a, b, c), ans):
            self.assertAlmostEqual(calc, actual)

class TestFormula(unittest.TestCase):

    @classmethod
    def setUp(cls):
        def func(a, b):
            return a + b
        def func2(a, b):
            return [a+b, a-b]
        cls.formula_one = NumericFormula('testing', func)
        cls.formula_two = NumericFormula('testing1', func2)

    def test_eval(self):
        a = 2
        b = 3
        self.assertEqual(self.formula_one.eval(2, 3), [5])
        self.assertEqual(self.formula_two.eval(2, 3), [5, -1])

    def test_validate(self):

        for arg in ['a', {'a':1}, [2]]:
            with self.assertRaises(ValueError):
                self.formula_one.eval(arg, 1)

            with self.assertRaises(ValueError):
                self.formula_one.eval(1, arg)

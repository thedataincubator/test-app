from __future__ import division
import unittest
from formulas import quadratic, NumericFormula
import math

class NumericStringsMixin(object):
    def _assert_num_strings(self, a, b, method):
            for i,j in zip(a,b):
                method(complex(i), complex(j))

class TestFunctions(unittest.TestCase, NumericStringsMixin):

    def test_quadratic(self):
        a = 5
        b = 1
        c = 4
        ans = [1/10*1j*(math.sqrt(79) + 1j), -1/10*1j*(math.sqrt(79) - 1j)]
        self._assert_num_strings(quadratic(a, b, c), ans, self.assertAlmostEquals)

class TestFormula(unittest.TestCase, NumericStringsMixin):

    @classmethod
    def setUp(cls):
        def func(a, b):
            return a + b
        def func2(aa, bb):
            return [aa + bb, aa - bb]
        cls.formula_one = NumericFormula('testing', func)
        cls.formula_two = NumericFormula('testing1', func2)

    def test_eval(self):
        a = 2
        b = 3
        self._assert_num_strings(self.formula_one.eval(2, 3), [5], self.assertAlmostEquals)
        self._assert_num_strings(self.formula_two.eval(2, 3), [5, -1], self.assertAlmostEquals)

    def test_validate(self):

        for arg in ['a', {'a':1}, [2]]:
            with self.assertRaises(ValueError):
                self.formula_one.eval(arg, 1)

            with self.assertRaises(ValueError):
                self.formula_one.eval(1, arg)

    def test_input(self):
        self.assertEquals(self.formula_one.inputs(), ['a','b'])
        self.assertEquals(self.formula_two.inputs(), ['aa', 'bb'])

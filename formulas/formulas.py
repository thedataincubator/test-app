from __future__ import division
import cmath
from .base import BaseFormula

class NumericFormula(BaseFormula):

    def _validate(self, *args):
        """enusre int or float for numeric quantities
        will raise ValueError if not correct
        """
        try:
            return tuple([float(i) for i in args])
        except TypeError:
            raise ValueError

def quadratic(a, b, c):
    """compute roots for equation of form
    a x^2 + b x + c = 0
    """
    sqrt = cmath.sqrt(b*b - 4 * a * c)
    return [(-b + sqrt)/(2.0 * a ), (-b - sqrt)/(2 * a )]

# Export defined formulas for use in application 
FORMULAS = [NumericFormula('Quadratic Formula', quadratic)]
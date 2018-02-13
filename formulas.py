import cmath

class Formula(object):
    def __init__(self, name, func):
        self._inputs = func.__code__.co_varnames
        self._func = func 
        self._name = name

    def inputs(self):
        return sorted(self._inputs)
    
    def _validate(self, *args):
        pass

    def eval(self, *args):
        self._validate(*args)
        result = self._func(*args)
        return [result] if not isinstance(result, list) else result

class NumericFormula(Formula):

    def _validate(self, *args):
        for arg in args:
            if not isinstance(arg, (int, float)):
                raise ValueError

def quadratic(a, b, c):
    sqrt = cmath.sqrt(b*b - 4 * a * c)
    return [(-b + sqrt)/(2 * a ), (-b - sqrt)/(2 * a )]

    
FORMULAS = [NumericFormula('Quadratic Formula', quadratic)]
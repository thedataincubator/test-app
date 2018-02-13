import math
class Formula(object):
    def __init__(self, name,func):
        self._inputs = func.__code__.co_varnames
        self._func = func 
        self._name = name

    def inputs(self):
        return sorted(self._inputs)

    def eval(self, *args):
        result = self._func(*args)
        return list(result) if not isinstance(result, list) else result

def quadratic(a, b, c):
    sqrt = math.sqrt(b*b - 4 * a * c)
    return [(b**2 + sqrt)/(2 * a ), (b**2 - sqrt)/(2 * a )]

    
FORMULAS = [Formula('Quadratic Formula', quadratic)]
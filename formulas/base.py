from __future__ import division
import inspect

class BaseFormula(object):
    def __init__(self, name, func, info=None):
        self._inputs = inspect.getargspec(func)[0]
        self._func = func 
        self._name = name
        self._info = info

    def inputs(self):
        """returns sorted inputs"""
        return sorted(self._inputs)

    def info(self):
        return self._info

    def name(self):
        """function to return name stringified
        replaces spaces with _ and lowers case
        """
        return self._name.replace(' ', '_').lower()

    def display_name(self):
        """get for _name attribute"""
        return self._name
    
    def _validate(self, *args):
        """can be used to validate argument type if necessary"""
        return args

    def _format(self, num):
        """format a number to a string so we can serialize
        TODO nicer formatting
        """
        return str(num)

    def eval(self, *args):
        """validate arguments and evaluate function
        return a list regardless of function return value"""
        func_args = self._validate(*args)
        result = self._func(*func_args)
        list_r = [result] if not isinstance(result, list) else result
        return [self._format(i) for i in list_r]
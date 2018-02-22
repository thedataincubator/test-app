""" main app"""
import logging
from flask import Flask, render_template, request, jsonify
from formulas import FORMULAS

app = Flask(__name__) # pylint: disable=C0103

def filter_formulas(name):
    """filter formulas to get a single name"""
    return [i for i in FORMULAS if i.name() == name][0]

@app.route('/')
def index():
    """main index route"""
    return render_template('index.html', formulas=FORMULAS)

@app.route('/formula-<calc>')
def formula_(calc):
    """enter parameters into formula"""
    # Can this be improved so I don't need to look up everything?
    formula = filter_formulas(calc)
    return render_template('formula.html', formula=formula)

@app.route('/_calc-<name>')
def calculate(name):
    """calculate the formula"""
    formula = filter_formulas(name)
    # are we sure the order is correct here?
    try:
        ans = {'answer': formula.eval(*request.args.values()),
               'error': False}
    except ValueError as error:
        logging.error(error)
        ans = dict(answer=None, error=True)
    return jsonify(ans)


if __name__ == '__main__':
    app.run(port=33507)

import logging
from flask import Flask, render_template, request, redirect, jsonify
from formulas import FORMULAS

app = Flask(__name__)

def filter_formulas(name):
  return [i for i in FORMULAS if i.name() == name][0]

@app.route('/')
def index():
  return render_template('index.html', formulas=FORMULAS)

@app.route('/formula-<calc>')
def formula(calc):
  # Can this be improved so I don't need to look up everything?
  formula = filter_formulas(calc)
  return render_template('formula.html', formula=formula)

@app.route('/_calc-<name>')
def calc(name):
  formula = filter_formulas(name)
  # are we sure the order is correct here?
  try:
    ans = {'answer': formula.eval(*request.args.values()),
          'error': False}
  except ValueError as e:
    logging.error(e)
    ans = dict(answer=None, error=True)
  return jsonify(ans)


if __name__ == '__main__':
  app.run(port=33507)

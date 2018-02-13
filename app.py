from flask import Flask, render_template, request, redirect
from formulas import FORMULAS

app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html', formulas=FORMULAS)

@app.route('/about')
def about():
  return render_template('about.html')

if __name__ == '__main__':
  app.run(port=33507)

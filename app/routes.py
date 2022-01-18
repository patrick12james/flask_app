from app import app
from flask import render_template

@app.route('/')
def index():
  my_name = 'Patrick'
  my_city = 'Smith Valley'
  colors = []

  return render_template('index.html, name=my_name, city=my_city, colors=colors, person=person');

import os, io
from flask import Flask, request, url_for, render_template, send_file, redirect
from dfk import *

app = Flask(__name__)

@app.route("/")
def hello():
  string = "<form method=\"POST\"><input name=\"text\"><input type=\"submit\"></form>"
  return(string)

@app.route("/", methods=['POST'])
def search():
  return redirect(url_for('say_hello', name = request.form['text']))

# this is where the action is
@app.route("/<string:name>/")
def say_hello(name):
  return hero_list
  # 1. get all hero stats
  # 2. simulate leveling all heroes
  # 3. get hero stats at level 1
  # hero = getHero(name, hero_list)
  # 4. get hero stat ranges at level 100
  # leveled_hero = getHero(name, leveled_hero_list)
  # 5. display
  # 5.1 hero stats at level 1
  # 5.2 bar charts highlight hero stats level 1
  # 5.3 hero stat ranges at level 100
  # 5.4 bar charts highlight hero stat ranges level 100

if __name__ == "__main__":

  # hero_list is a json dict list straight from the dfk api
  global hero_list
  # leveled_hero_list will also be a json dict list, but stats will be 95% interval tuples instead
  global leveled_hero_list
  # before the app starts, index all available heroes
  hero_list = getAllHeroes()
  # remove lag from app, level all heroes in advance
  leveled_hero_list = levelAllHeroes()
  # then run the app
  app.run()

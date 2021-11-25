import os, io, pandas
from flask import Flask, request, url_for, render_template, send_file, redirect
from dfk import *

app = Flask(__name__)

def generatePage(name, images):
  string = "<html><head><title>"+name+"</title></head><body>"
  for i in range(0,len(images)):
    p = os.path.join(os.getcwd(), 'static',  name + str(i) + '.png')
    with open(p,'wb') as ifile:
      ifile.write(images[i].read())
    img = url_for('static', filename=name+str(i)+'.png')
    string += "<img src=\""+img+"\"><br>"
  string += "</body></html>"
  return(string)

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
  images = []
  images.append(getBarChart('strength', name, df_hero)
  return generatePage('test', images)

if __name__ == "__main__":

  global df_hero
  global leveled_hero_list
  # before the app starts, index all available heroes
  # data.txt indexes the first 44089 heroes (scraped 2021-11-24)
  with open ('data.txt', 'r') as f:
    hero_list = json.load(f)
    df_hero = pandas.DataFrame(hero_list)
  # remove lag from app, level all heroes in advance
  # leveled_hero_list = levelAllHeroes(hero_list)
  # then run the app
  app.run()


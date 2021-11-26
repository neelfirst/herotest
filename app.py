import os, io, pandas, sys, statistics
import matplotlib.pyplot as plt
from flask import Flask, request, url_for, render_template, send_file, redirect
from dfk import *

STAT_LIST = ['strength', 'endurance', 'agility', 'luck', 'dexterity', 'intelligence', 'wisdom', 'vitality']

app = Flask(__name__)
# before the app starts, index all available heroes
# data.txt indexes the first 44089 heroes (scraped 2021-11-24)
hero_list = json.load(open('data.txt','r'))
df_hero = pandas.DataFrame(hero_list)

# stat: string name
# hero_id: our query
def getBarChart(stat, hero_id):
  xy = {}
  xy[stat] = df_hero[stat].value_counts().sort_index(ascending=True).keys()
  xy['count'] = df_hero[stat].value_counts().sort_index(ascending=True).values
  buf = io.BytesIO()
  c = ['r' if (df_hero.iloc[int(hero_id)][stat] == x) else 'b' for x in xy[stat]]
  ax = pandas.DataFrame(xy).plot.bar(x=stat, y='count', color=c, rot=0)
  plt.savefig(buf)
  buf.seek(0)
  return buf

def generatePage(name, images):
  string = "<html><head><title>"+name+"</title></head><body>"
  for i in range(0,len(images)):
    p = os.path.join(os.getcwd(), 'static',  name + '_' + str(i) + '.png')
    with open(p,'wb') as ifile:
      ifile.write(images[i].read())
    img = url_for('static', filename=name+'_'+str(i)+'.png')
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
  for stat in STAT_LIST:
    images.append(getBarChart(stat, name))
  return generatePage(name, images)

def main():
  # remove lag from app, level all heroes in advance
  # leveled_hero_list = levelAllHeroes(hero_list)
  # then run the app
  app.run()

if __name__ == "__main__":
  main()

import os, io, pandas, sys, json
import matplotlib.pyplot as plt
from flask import Flask, request, url_for, render_template, send_file, redirect

STAT_LIST = ['strength', 'endurance', 'agility', 'luck', 'dexterity', 'intelligence', 'wisdom', 'vitality']

app = Flask(__name__)
# before the app starts, index all available heroes
# data.txt is irregularly updated by 'batchdfk.main()' 2021-11-26 N
with open('data.txt','r') as f:
  hero_list = json.load(f)
df_hero = pandas.DataFrame(hero_list)

# stat: string hero_id
# hero_id: our query
def getBarChart(stat, hero_id, data):
  stat_keys = data[stat].value_counts().sort_index(ascending=True).keys().astype('str')
  stat_counts = data[stat].value_counts().sort_index(ascending=True).values
  buf = io.BytesIO()
  c = ['r' if (df_hero.iloc[int(hero_id)][stat] == int(x)) else 'b' for x in stat_keys]
  plt.figure(figsize=(3.5,2))
  plt.bar(stat_keys, stat_counts, color=c)
  plt.title(stat)
  plt.savefig(buf)
  buf.seek(0)
  return buf

def generatePage(hero_id, images):
  string = "<html><head><title>"+str(hero_id)+"</title></head><body>"
  string += "<form method=\"POST\"><input name=\"text\"><input type=\"submit\"></form>"
  for i in range(0,len(images)):
    p = os.path.join(os.getcwd(), 'static',  str(hero_id) + '_' + str(i) + '.png')
    with open(p,'wb') as ifile:
      ifile.write(images[i].read())
    img = url_for('static', filename=str(hero_id)+'_'+str(i)+'.png')
    string += "<img src=\""+img+"\"><br>"
  string += "</body></html>"
  return(string)

@app.route("/")
def hello():
  string = "<form method=\"POST\"><input name=\"text\"><input type=\"submit\"></form>"
  return(string)

@app.route("/", methods=['POST'])
def search():
  return redirect(url_for('say_hello', hero_id = request.form['text']))

# this is where the action is
@app.route("/<int:hero_id>/")
def say_hello(hero_id):
  images = []
  for stat in STAT_LIST:
    images.append(getBarChart(stat, hero_id, df_hero))
  return generatePage(hero_id, images)

@app.route("/<int:hero_id>/", methods=['POST'])
def filter(hero_id):
  return redirect(url_for('filterPage', hero_id = hero_id, filter = request.form['text']))

@app.route("/<int:hero_id>/<string:filter>/")
def filterPage(hero_id, filter):
  images = []
  df_filter = df_hero.loc[df_hero[filter]==df_hero.iloc[int(hero_id)][filter]]
  for stat in STAT_LIST:
    images.append(getBarChart(stat, hero_id, df_filter))
  return generatePage(hero_id, images)

def main():
  # remove lag from app, level all heroes in advance
  # leveled_hero_list = levelAllHeroes(hero_list)
  # then run the app
  app.run()

if __name__ == "__main__":
  main()

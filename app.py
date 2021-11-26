import os, io, pandas, sys, json
import matplotlib.pyplot as plt
from flask import Flask, request, url_for, render_template, send_file, redirect

STAT_LIST = ['strength', 'endurance', 'mining', \
             'agility', 'luck', 'fishing', \
             'dexterity', 'intelligence', 'foraging', \
             'wisdom', 'vitality', 'gardening']

app = Flask(__name__)
# before the app starts, index all available heroes
# data.txt is irregularly updated by 'batchdfk.main()' 2021-11-26 N
with open('data.txt','r') as f:
  hero_list = json.load(f)
df_hero = pandas.DataFrame(hero_list)

def match(stat_short, stat_name):
  if stat_short == 'STR':
    return stat_name == 'strength'
  if stat_short == 'END':
    return stat_name == 'endurance'
  if stat_short == 'WIS':
    return stat_name == 'wisdom'
  if stat_short == 'VIT':
    return stat_name == 'vitality'
  if stat_short == 'DEX':
    return stat_name == 'dexterity'
  if stat_short == 'INT':
    return stat_name == 'intelligence'
  if stat_short == 'AGI':
    return stat_name == 'agility'
  if stat_short == 'LCK':
    return stat_name == 'luck'

# stat: string hero_id
# hero_id: our query
def getBarChart(stat, hero_id, data):
  hero = df_hero.iloc[int(hero_id)]
  stat_keys = data[stat].value_counts().sort_index(ascending=True).keys().astype('str')
  stat_counts = data[stat].value_counts().sort_index(ascending=True).values
  buf = io.BytesIO()
  c = ['r' if (hero[stat] == int(x)) else 'b' for x in stat_keys]
  # apply stat boost borders
  if match(hero['statBoost1'],stat) and match(hero['statBoost2'],stat):
    plt.figure(linewidth=4, edgecolor='m')
  elif match(hero['statBoost1'],stat):
    plt.figure(linewidth=4, edgecolor='g')
  elif match(hero['statBoost2'],stat):
    plt.figure(linewidth=4, edgecolor='c')
  elif hero['profession'] == stat:
    plt.figure(linewidth=4, edgecolor='g')
  else:
    plt.figure(linewidth=4, edgecolor='w')
  plt.bar(stat_keys, stat_counts, color=c)
  plt.title(stat)
  plt.savefig(buf)
  plt.clf()
  buf.seek(0)
  return buf

def generatePage(hero_id, images):
  filenames = {}
  for image in images:
    f = str(hero_id) + '_' + image + '.png'
    p = os.path.join(os.getcwd(), 'static', f)
    with open(p,'wb') as ifile:
      ifile.write(images[image].read())
    filenames[image] = url_for('static', filename = f)
  return render_template('result.html', hero_id = hero_id, hero = filenames)

@app.route("/")
def hello():
  return render_template('index.html')

@app.route("/", methods=['POST'])
def search():
  return redirect(url_for('say_hello', hero_id = request.form['text']))

@app.route("/<int:hero_id>/", methods=['POST'])
@app.route("/<int:hero_id>/<string:filter>"/, methods=['POST'])
def filter_hero(hero_id, filter=None):
  return redirect(url_for('filterPage', hero_id = hero_id, filter = request.form['text']))

# this is where the action is
@app.route("/<int:hero_id>/")
@app.route("/<int:hero_id>/<string:filter>/")
def filterPage(hero_id, filter=None):
  images = {}
  if filter:
    df_filter = df_hero.loc[df_hero[filter]==df_hero.iloc[int(hero_id)][filter]]
  else:
    df_filter = df_hero
  for stat in STAT_LIST:
    images[stat] = getBarChart(stat, hero_id, df_filter)
  return generatePage(hero_id, images)

def main():
  # remove lag from app, level all heroes in advance
  # leveled_hero_list = levelAllHeroes(hero_list)
  # then run the app
  app.run()

if __name__ == "__main__":
  main()

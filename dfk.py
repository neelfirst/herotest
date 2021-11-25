#!/usr/bin/env python3

import requests, json
from time import sleep
from querydfk import BATCH_QUERY
import numpy, pandas, io
import matplotlib.pyplot as plt

URL = 'https://graph2.defikingdoms.com/subgraphs/name/defikingdoms/apiv5'
N_HEROES = 45000 # would be lovely to retrieve this value from the api

def getHero():
  return

# use this function sparingly. this blasts the DFK API, sleep(1) is a keepalive
def getAllHeroes():
  results = []
  for i in range(0, N_HEROES, 100): # we're limited to 100 heroes at a time
    vars = {'I': i}
    r = requests.post(URL, json={'query': BATCH_QUERY, 'variables': vars}).json()['data']['heros']
    results.extend(r)
    sleep(1)
  return results

# input: a list of dicts, each dict is a hero object from DFK API
# output: tuple (mean, variance) for each of the 8 base stats + hp/mp
# going with binomial distribution here - so (np, np(1-p))
class LeveledHero:
  def __init__ (self, hero):
    self.level = 1

    self.str = (hero['strength'], 0)
    self.agi = (hero['agility'], 0)
    self.end = (hero['endurance'], 0)
    self.wis = (hero['wisdom'], 0)
    self.dex = (hero['dexterity'], 0)
    self.vit = (hero['vitality'], 0)
    self.int = (hero['intelligence'], 0)
    self.luc = (hero['luck'], 0)
    self.hp  = (hero['hp'], 0)
    self.mp  = (hero['mp'], 0)

def levelAllHeroes(hero_list):
  return

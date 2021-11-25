#!/usr/bin/env python3

import requests, json
from time import sleep
from querydfk import BATCH_QUERY

URL = 'https://graph2.defikingdoms.com/subgraphs/name/defikingdoms/apiv5'
N_HEROES = 45000 # would be lovely to retrieve this value from the api

def getHero():
  return

def getAllHeroes():
  results = []
  for i in range(0, N_HEROES, 100): # we're limited to 100 heroes at a time
    vars = {'I': i}
    r = requests.post(URL, json={'query': BATCH_QUERY, 'variables': vars}).json()['data']['heros']
    results.extend(r)
    sleep(1)
  return results

def levelAllHeroes():
  return

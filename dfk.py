#!/usr/bin/env python3

import requests, json

URL = 'https://graph2.defikingdoms.com/subgraphs/name/defikingdoms/apiv5'
N_HEROES = 45000 # would be lovely to retrieve this value from the api
QUERY = """query getHeroInfo($I: Int) {
  heros(skip: $I, orderBy: numberId) {
    id
    owner {
      id
      name
    }
  }
}"""

def getHero():
  return

def getAllHeroes():
  results = []
  for i in range(0, N_HEROES, 100): # we're limited to 100 heroes at a time
    vars = {'I': i}
    r = requests.post(URL, json={'query': QUERY, 'variables': vars}).json()['data']['heros']
    results.extend(r)
    print(i)
  return results

def levelAllHeroes():
  return

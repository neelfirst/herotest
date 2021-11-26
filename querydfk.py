#!/usr/bin/env python3

import json, requests
from time import sleep

# batch query of 100 heroes
BATCH_QUERY = """query getHeroInfo($I: Int) {
  heros(skip: $I, orderBy: numberId) {
    id
    numberId
    owner {
      id
      owner
      name
      created
      picId
      heroId
    }
    creator {
      id
      owner
      name
      created
      picId
      heroId
    }
    statGenes
    visualGenes
    rarity
    shiny
    generation
    firstName
    lastName
    shinyStyle
    mainClass
    subClass
    summonedTime
    nextSummonTime
    summonerId {
      id
    }
    assistantId {
      id
    }
    summons
    maxSummons
    staminaFullAt
    hpFullAt
    mpFullAt
    level
    xp
    currentQuest
    sp
    status
    strength
    intelligence
    wisdom
    luck
    agility
    vitality
    endurance
    dexterity
    hp
    mp
    stamina
    strengthGrowthP
    intelligenceGrowthP
    wisdomGrowthP
    luckGrowthP
    agilityGrowthP
    vitalityGrowthP
    enduranceGrowthP
    dexterityGrowthP
    strengthGrowthS
    intelligenceGrowthS
    wisdomGrowthS
    luckGrowthS
    agilityGrowthS
    vitalityGrowthS
    enduranceGrowthS
    dexterityGrowthS
    hpSmGrowth
    hpRgGrowth
    hpLgGrowth
    mpSmGrowth
    mpRgGrowth
    mpLgGrowth
    mining
    gardening
    foraging
    fishing
    profession
    passive1
    passive2
    active1
    active2
    statBoost1
    statBoost2
    statsUnknown1
    element
    statsUnknown2
    gender
    headAppendage
    backAppendage
    background
    hairStyle
    hairColor
    visualUnknown1
    eyeColor
    skinColor
    appendageColor
    backAppendageColor
    visualUnknown2
    assistingAuction {
      id
    }
    assistingPrice
    saleAuction {
      id
    }
    salePrice
    privateAuctionProfile {
      id
    }
  }
}"""

URL = 'https://graph2.defikingdoms.com/subgraphs/name/defikingdoms/apiv5'
N_HEROES = 45300 # would be lovely to retrieve this value from the api

# use this function sparingly. this blasts the DFK API, sleep(1) is a keepalive
def getAllHeroes(start):
  results = []
  for i in range(start, N_HEROES, 100): # we're limited to 100 heroes at a time
    vars = {'I': i}
    r = requests.post(URL, json={'query': BATCH_QUERY, 'variables': vars}).json()['data']['heros']
    results.extend(r)
    sleep(1)
  return results

# load json text, get count, update with new query, save
def main():
  with open('data.txt','r') as f:
    j = json.load(f)
  j.extend(getAllHeroes(len(j)))
  with open('data.txt','w') as f:
    f.write(json.dumps(j))

if __name__ == "__main__":
  main()

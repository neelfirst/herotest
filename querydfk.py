#!/usr/bin/env python3

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

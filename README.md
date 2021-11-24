# herotest
Herotest provides a standardized testing service for hero NFTs that exist in the Defi Kingdoms (DFK) metaverse.

This is not official DFK code and does not claim to be, etc etc.

# Standardized Testing Sucks
The original effort that inspired this project focused on the leveling aspect of hero NFTs and their suitability for various professions.[1] However it explicitly ignores two other key usages of hero NFTs: 1) their ability to generate new hero NFTs and 2) their ability to perform combat actions (against other heros or NPCs). This ranking algorithm is beginning to proliferate, most notably in kingdom.watch, a service for players to maintain their portfolios in the DFK metaverse.[2]

It would be ineffective to generate one all-consuming score to evaluate three distinct areas of expertise. Therefore three different scores are proposed here.

## Professionalism
How suitable is a hero at a given profession? This is largely addressed by [1,2] and it is used unchanged here.
* Mining - KWPS(STR, END)
* Gardening - KWPS(WIS, VIT)
* Fishing - KWPS(AGI, LUC)
* Foraging - KWPS(DEX, INT)
## Combat
How suitable is a hero at a particular combat expertise? This follows the leveling algorithms described in [2] but are applied across different combinations more appropriate for PVP.
* Tank - KWPS(STR, END, VIT, HP)
* Rogue - KWPS(AGI, DEX, VIT)
* Mage - KWPS(WIS, INT, MP)
* Support
## Summoning
How suitable is a hero for creating maximally beneficial new heroes? A ranking algorithm is proposed here based on summon cost and cooldown.
* Summons remaining
* Average cost per summon
* Level


# References
[1] https://www.reddit.com/r/DefiKingdoms/comments/qpotgf/analysis_on_profession/<br>
[2] https://kingdom.watch/about/heroranking<br>
[3] https://docs.defikingdoms.com/learn/gameplay/leveling<br>

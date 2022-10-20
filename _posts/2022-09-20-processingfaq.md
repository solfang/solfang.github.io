---
layout: post
title: BDO - Processing FAQ - 20 commonly asked questions answered
published: true
tags: BDO
---

# TODO: grammarly + proofread
# TODO: re-do numbering based on added questions and adapt title
Heya, I'm Summer and I made this post to answer commonly asked questions about processing.
It's essentially a processing guide but this format is a bit nicer to `ctrl+f` in case you are looking for a specific topic.

Enjoy :)

# Basics

## 1. how to process?
1. Open the processing window (L key)
2. Select a processing type 
3. Input the materials
4. Press 'Start' or 'Mass Process' (more on mass processing in question 5)

<video width="640" height="360" muted autoplay controls>
    <source src="/files/processing_faq/howtoprocess.mp4" type="video/mp4">
</video>

After a few seconds, one of three things will happen:
1) The craft succeeds
2) The message `Processing is not going as planned.` appears → Your character will re-try the craft (no materials are lost).
3) The message `It is not working at all.` appears → You input the wrong items (no materials are lost). the correct recipe to craft an item can usually be found in the item description of the input items or the produced item.

<img width="300" src="/files/processing_faq/process_outcomes.jpg">

## 2. How can I stop processing from failing?

Even if you input the right materials, the message `Processing is not going as planned.` can appear, which means your character has to re-try to the craft (no materials are lost).
The chance of this happening is tied to your processing success rate. The success rate starts out at 67%. With a success rate of 100% you'll never fail crafts. Here's how to increase your sucess rate:

- <!-- db_item-603044-0 --> / <!-- db_item-560024-0 --> (pearl shop costume) 3%  
- <!-- db_item-14026-0 --> 6%-40% (applied to the base success rate so actually 4%-27%)
- <!-- db_item-9691-0 --> 10% for 2 hours / <!-- db_item-9642-0 --> +15% for 10 hours
- <!-- db_item-791-0 --> 20% for 15 mins
- Alchemy stone: <!-- db_item-45280-0 --> or <!-- db_item-45302-0 --> 11% / <!-- db_item-45284-0 --> 14%
- Clang! Clang! Lightstone set: 20%   (<!-- db_item-764016-0 --> <!-- db_item-764008-0 --> <!-- db_item-762006-0 --> <!-- db_item-766101-0 -->)
- <!-- db_item-735354-0 --> 5% each

You may have heard that the success rate *can not* reach 100%. According to tests by the lifeskill community, it's almost certain that the success rate *can* reach 100%. However, certain items have different success rate than indicated in the item description. This potentially includes verdure draught and the Clang! Clang! set. So to get 100% it helps to overstack success rate buffs by a few percent.

# Mass Processing and Mastery

## 3. What is mass processing?
Mass processing lets you process mutltiple items at once but it takes 10x longer than regular processing.
For example, processing timber into planks takes 6 seconds with regular processing and 60 seconds with mass processing.
You need a processing stone to get access to the 'Mass Process' button in the processing menu.
Note that mass processing does not work with simple alchemy/cooking, imperial alchemy/cooking, guild processing and manufacturing.
Also, it only works on stackable items. For example, you can't mass heat weapons because they take up 1 inventory slot each.

## 4. Can I mass-process black gems/caphras stones/party elixirs/blue elixirs/draughts/cron meals/imperial boxes?

Not directly through the mass process system. But you can add specific items to the recipe that unlock alternative '10x' recipes:
- Caphras stones, black gems, concentrated magical black gems: <!-- db_item-4901-0 -->
- party and blue elxiris, draughts: <!-- db_item-4986-0 --> (buy at materials vendors)
- cron meals: <!-- db_item-820015-0 --> (buy at cooking NPCs)
- imperial cooking/alchemy boxes: <!-- db_item-8198-0 --> (buy at old moon managers. Using it requires having completed a [quest](https://youtu.be/x02GMajBFqU))

You can check these recipes in the in-game crafting notes (F2→Crafting notes in the top right or shift+LMB on any item in your inventory).

## 5. What does processing mastery do?

Processing mastery increases the number of items you can process at once through mass processing.
For example, with 1020 mastery you can process 90 items at once, which ends up being 9 times faster than regular processing.
Also note that at the lowest possible mastery bracket, you can process 10 items at once. Since you also take 10x longer than regular processing, it's the same seed at regular processing.
That means mass processing is *always at least as good or better than regular processing*.

| Mastery | Batches |
|:-------:|:-------:|
|    2    |    10   |
|    20   |    11   |
|    40   |    12   |
|    60   |    13   |
|    80   |    14   |
|   100   |    15   |
|   120   |    16   |
|   140   |    17   |
|   160   |    18   |
|   180   |    19   |
|   200   |    20   |
|   220   |    21   |
|   240   |    22   |
|   260   |    23   |
|   280   |    24   |
|   300   |    25   |
|   320   |    26   |
|   340   |    27   |
|   360   |    28   |
|   380   |    29   |
|   400   |    30   |
|   420   |    31   |
|   440   |    32   |
|   460   |    33   |
|   480   |    34   |
|   500   |    35   |
|   520   |    36   |
|   540   |    37   |
|   560   |    38   |
|   580   |    39   |
|   600   |    40   |
|   620   |    41   |
|   640   |    42   |
|   660   |    43   |
|   680   |    45   |
|   700   |    47   |
|   720   |    49   |
|   740   |    51   |
|   760   |    53   |
|   780   |    57   |
|   810   |    60   |
|   840   |    64   |
|   870   |    68   |
|   900   |    72   |
|   930   |    76   |
|   960   |    80   |
|   990   |    85   |
|   1020  |    90   |
|   1060  |    96   |
|   1100  |   112   |
|   1140  |   118   |
|   1180  |   124   |
|   1220  |   130   |
|   1260  |   137   |
|   1300  |   144   |
|   1350  |   154   |
|   1400  |   162   |
|   1450  |   170   |
|   1500  |   178   |
|   1550  |   186   |
|   1600  |   194   |
|   1650  |   203   |
|   1700  |   212   |
|   1800  |   222   |
|   1900  |   235   |
|   2000  |   250   |

Table: mastery brackets and mass processing batches

## 6. How much processing mastery do I need for processing?

In other lifskills, more mastery is always better. This applies to processing only to some extent.
Having higher processing mastery lets you process items at a faster rate. But you are still limited by weight. That means if your processing mastery is suffiently high, your character will run out of weight before you check back on your processing.  Increasing processing mastery further won't change that. So here's my advice: Get your processing mastery to a point where you barely run out of weight whenever you check back on your processing (on whateve recipe you commonly process).

# Recipes, Proc Rates and Process Times

## 7. How many items does a craft yield and what affects it?

### What affects the proc rate?
There are a few aspect:
- The following processing types have fixed rates and are not affected by processing level:  Simple alchemy, simple cooking, imperial cuisine, imperial alchemy, guild processing, manufacturing.
- Other recipes *cap out at a certain processing level*. For example, timber caps out at artisan 6 and ore at master 1. You can look up the maximum required level on bdocodex on the same page where you would look up the proc rate. Once you're master 1, you'll have the maximum proc rate on 99% of items (one exception I know of are jade coral ingots which require guru 1).
- **Proc rate is neither affected by mastery nor by whether you're regular or mass processing.**

### Info on common processing recipes

| Recipe                                   | Example                   | Process Type   | Proc Range | Proc Avg |    Level Req   |   EXP    |   Time  | Required Knowledge  |
|------------------------------------------|---------------------------|----------------|:----------:|:--------:|:--------------:|:--------:|:-------:|---------------------|
| Plank (T2)                               | Ash Plank                 | Chopping       |     1-4    |    2.5   |    Artisan 6   |  200/500 |   6/60  | -                   |
| Plywood (T3)                             | Ash Plywood               | Chopping       |     1-4    |    2.5   | Professional 6 |    500   |   6/60  | Chopping: Beginner  |
| Sturdy Plywood (T4)                      | Sturdy Ash Plywood        | Heating        |     1-3    |     2    |  Professonal 1 |   1000   |   6/60  | Heating: Skilled    |
| Melted Shard (T2)                        | Melted Iron Shard         | Heating        |     1-4    |    2.5   |    Master 1    |  200/500 |   9/90  |                     |
| Ingot (T3)                               | Iron Ingot                | Heating        |     1-4    |    2.5   |    Artisan 1   |    500   | varies* | Heating: Beginner   |
| Pure Crystal (T4)                        | Pure Iron Crystal         | Heating        |     1-3    |     2    |  Professonal 1 |   1000   |   6/60  | Heating: Skilled    |
| Hide (T2)                                | Tough Hide                | Drying         |     1-4    |    2.5   |    Skilled 1   |    200   |   9/90  | -                   |
| Fine Hide (T3)                           | Fine Tough Hide           | Drying         |     1-4    |    2.5   |    Skilled 1   |    500   |   9/80  | Drying: Beginner    |
| Supreme Hide (T4)                        | Supreme Tough Hide        | Shaking        |     1-3    |     2    |  Apprentice 1  |   1000   |   9/80  |   Shaking: Skilled  |
| Feather (T2)                             | Lightweight Plume         | Filtering      |     1-4    |    2.5   |  Professonal 6 |  200/500 |   6/60  | -                   |
| Fine Feather (T3)                        | Fine Lightweight Plume    | Filtering      |     1-4    |    2.5   |    Skilled 6   |    500   |   9/80  | Filtering: Beginner |
| Supreme Feather (T4)                     | Supreme Lightweight Plume | Shaking        |     1-3    |     2    |  Apprentice 1  |   1000   |   9/80  |   Shaking: Skilled  |
| Gem (T2)                                 | Ruby                      | Grinding       |     1-4    |    2.5   |    Artisan 1   | 500/1000 |   9/80  | -                   |
| Resplendent Gem (T3)                     | Resplendent Ruby          | Grinding       |     1-3    |     2    |    Skilled 1   |   1000   |   9/80  | Grinding: Beginner  |
| Special Gem (T4)                         | Blood Ruby                | Shaking        |     1-2    |    1.5   |  Apprentice 1  |   2000   |   6/80  |   Shaking: Skilled  |
| Cream                                    |                           | Shaking        |     1-4    |    2.5   |    Skilled 1   |    150   |   6/60  | -                   |
| Butter                                   |                           | Shaking        |     1-4    |    2.5   |    Skilled 1   |    150   |   6/60  | -                   |
| Cheese                                   |                           | Drying         |     1-4    |    2.5   |    Skilled 1   |    300   |   9/60  | -                   |
| Flour                                    |                           | Grinding       |     1-4    |    2.5   | Professional 1 |    70    |   6/60  | -                   |
| Dough                                    |                           | Shaking        |     1-4    |    2.5   |    Skilled 1   |    150   |   6/60  |                     |
| T2 Fabrics                               | Flax Thread               | Heating        |     1-4    |    2.5   |    Artisan 1   |    500   |   6/60  | -                   |
| T3 Fabrics                               | Flax Fabric               | Grinding       |     1-4    |    2.5   | Professional 1 |   1000   |   6/60  | -                   |
| Black Stone Powder (BSA)                 |                           | Grinding       |    40-60   |    50    |    Artisan 1   |    80    |   9/80  | -                   |
| Black Stone Powder (BSW)                 |                           | Grinding       |   60-100   |    80    |    Artisan 1   |    80    |   9/80  | -                   |
| Purified Water (from bag of muddy water) |                           | Filtering      |     1-4    |    2.5   |    Artisan 1   |    300   |   6/60  | -                   |
| Usable Scantling                         |                           | Chopping       |     1-4    |    2.5   |    Artisan 6   | 500/1000 |   6/60  | -                   |
| Standardized Timber Square               |                           | Chopping       |     1-3    |     2    | Professional 6 |   1000   |   6/60  | -                   |
| Sturdy Timber Square                     |                           | Heating        |     1-3    |     2    |    Artisan 1   |   1500   |   6/60  | Heating. Skilled    |
| Ship Repair Material                     |                           | Chopping       |     1-3    |     2    |    Artisan 1   |   1000   |   6/60  | -                   |
| Polished Stone                           |                           | Grinding       |     1-4    |    2.5   |    Artisan 1   |    500   |   6/60  | -                   |
| Cron Meals                               | Simple Cron Meal          | Simple Cooking |      1     |     1    |   Beginner 1   |     0    |    6    |                     |
| Draughts                                 | Verdure Draught           | Simple Alchemy |      1     |     1    |   Beginner 1   |     0    |    6    |                     |
| Party Elixirs                            | [Party] Defense Elixir    | Simple Alchemy |     1-2    |    1.8   |   Beginner 2   |     0    |    6    |                     |
| Blue Elixirs                             | Elixir of Steel Defense   | Simple Alchemy |      1     |     1    |   Beginner 3   |     0    |    6    |                     |
| Black Gem                                |                           | Simple Alchemy |      1     |     1    |   Beginner 4   |     0    |    9    |                     |
| Concentrated Black Gem                   |                           | Simple Alchemy |      1     |     1    |   Beginner 5   |     0    |    9    |                     |
| Caphras Stone                            |                           | Simple Alchemy |      1     |     1    |   Beginner 6   |     0    |    6    |                     |

Table: Average procs and level required for common processing recipes. To keep this list short I included only common recipes.

Level Req: Level required to gain the maximum proc rate

EXP: Processing EXP. when two values are shown, the first one indicates the regular proc (e.g. ash plank) and the second one the rare proc (e.g. ash plywood)

Time: regular processing / mass processing time in seconds

\* Metal times: Zinc, Brass, Bronze: 6/60 |  Gold, Plat, Silver, Mythril: 9/80 | Others: 9/90

Source for the data: Daz' sheets, Bdocodex, bdolytics, in-game testing for the times

# TODO: proofread this table

Since the table does not include all items, here's how to look up this info yourself:
1. go to the [recipe page](https://cdn.discordapp.com/attachments/589711952234676224/704015738180075680/unknown.png) for that item on <https://bdocodex.com/> (This page is different from the item's page!): 
2. Look at the product groups at the bottom of the page. Each product product group represents a certain proc rate and is tied to a certain processing level.
The example below shows that you need Art6+ to get max procs on ash [ash plank processing](https://cdn.discordapp.com/attachments/589711952234676224/704016039742013460/unknown.png): https://bdocodex.com/us/mrecipe/585/ -  
(note: the last bracket seems to be missing in the current version of bdocodex)

## 8. How long does it take to process materials?

The process time depends on the item you're procecssing and of course on whether you use regular or mass processing, which takes 10x longer than regular processing.
I listed the processing times of common items in the table above. A processing time of 6/60 reads: regular processing takes 6 seconds, mass processing takes 60 seonds.
Most recipes take 6/60 or 9/90 seconds but there are some obscurities, like zinc, brass and bronze taking 80 seconds when mass processed. Don't ask me why :)
I've personally tested the processing times in the table as we don't have access to the processing times via the game files. 

## 9. What can I process?

The main demand for processing products comes from three areas of the game:
- trading: plywoods and ingots
- cooking: flour, dough, cheese, cream, butter
- workshops (furniture, ships, fishing rods etc.): T4 plywood/metals/hides/feathers/gems
Also check out the table above for common recipes.

<https://bdolytics.com/processing/market> features a list of processing recipes.
If you are not processing for a specific purpose and just want to make silver, check out question !TODO where I got more into detail on moneymaking.
#TODO: adapt reference number

## 10. Why can't I chop plyoowd / heat pure crystals?
You are missing knowledge.

To chop planks into plywood (t4) you need `chopping: beginner`, to chop plywood into sturdy plywood (T4) you need `heating: skilled`. You'll need the corresponding knowledge for the T3 and T4 recipes of metal, hides, feathers and gemstones.
You can get the knowledge entries through a quest chain. 

### Beginner knowledge
- Starting quest: [[Processing] Learning Higher Processing Skills](https://bdocodex.com/us/quest/2100/28/)
- Starting NPC: Ficy in Heidel
- Requirements: apprentice 4 gathering 
- You can find the quest via the in-game quest menu in the 'Suggested tab' (1) under '[Life][Certificate] Training Paradigm'. Make sure that you fulfill the quest requirements (2) and have all quests enabled (3).

<img width="400" src="/files/processing_faq/questbeginner2.png">

[Video guide](https://www.youtube.com/watch?v=TvmMImSGl88)

### Skilled knowledge
- Starting quest: [Processing] Excellent Magnate
- Starting NPC: Villager next to the blacksmith in Keplan (the waypoint button in the quest menu will lead you there)
- Requirements: Gathering skilled 10 AND processing skilled 5 AND all 6 pieces of beginner knowledge (shaking, drying, filtering, grinding, heating, chopping) 
- You can find the quest via the in-game quest menu in the 'Suggested tab' (1) under '[Life][Certificate] Skilled Paradim'. Make sure that you fulfill the quest requirements (2) and have all quests enabled (3). 


<img width="400" src="/files/processing_faq/questskilled2.png">

[Video guide](https://youtu.be/TvmMImSGl88?t=168)

**If you struggled with these quests because you needed additional info not mentioned in the guide please let me know and I will update the guide**

# Gear

## 11. What gear do I need for processing?
You technically don't need any gear to process. Though gear massively helps with processing by giving you the ability to mass process, increase mastery and success rate:

- <!-- db_item-768088-0 --> / <!-- db_item-/768087-0 --> / <!-- db_item-768086-0 -->: mastery (there used to be one stone for each processing type but they were merged into a single stone)
- <!-- db_item-705514-0 --> / <!-- db_item-705516-0 --> / <!-- db_item-705518-0 -->: mastery / Silver embroidered clothes: processing EXP and success rate
- <!-- db_item-705503-0 --> / <!-- db_item-705507-0 --> / <!-- db_item-705511-0 -->: mastery
- Artifacts: <!-- db_item-735372-0 --> (10 mastery) / <!-- db_item-735354-0 --> (5% success rate) / <!-- db_item-735361-0 --> (5% EXP)
- Lightstones: <img width="400" src="/files/processing_faq/clangclang.png">

In terms of clothes and processing stone just get whatever your budget allows and what you need to reach sufficient processing mastery (see question 6).

## 12. How do I get processing artifacts?
You can get them by handing in imperial cooking boxes. Processing artifacts drop from imperial cooking turn-ins, together with cooking artifacts. The chance to get an artifact is quite low (expect one maybe every 5-10 turn-ins) so it might take a while until you get the artifact you want.
You don't need to worry about having perfect artifacts though. While working on getting processing artifacts, you can still go for a lightstone set by using general-purpose artifacts like <!-- db_item-735351-0 -->  or <!-- db_item-735352-0 --> as placeholders. Once you get the processing artifacts, you can then extract the lightstones at a blacksmith with a lightstone extraction tool.

## 13. Do I need the pearl shop costume (Venecil Dress/Karki Suit)?

<!-- db_item-603044-0 --> and <!-- db_item-560024-0 --> can only be bought from the pearl shop, give 3% success rate and will let you process from storage. Note that you can only process from storage keepers, not storage containers.

When using a processing costume, the processed materials will go into your character's inventory. That means your character will only stop processing once you go overweight. 
Effectively, the processing costume lets you stay afk for longer (~2 times longer as without the costume) before refreshing your processing. BUT the processing costume will not increase your afk time on some recipes where the output materials are heavier than the input, like  four, dough, cream, butter and cheese.

In the end, the processing costume is purely a convenience item.
It's up to you to decide whether the convenience of being able to stay afk for longer is worth spending pearls on.

## 14. Should I use mastery or silver embroidered clothes? 

TLDR: Just use mastery clothes :)

Mastery clothes and silver embroidered (SE) processing clothes have different beenfits:
- Mastery clothes increase processing mastery, which boosts the number of batches you can process at once, effectively letting you process at a faster rate.
- SE clothes give procesing EXP and increase the processing success rate, which also lets you process at a faster rate. Though you won't see any benefit if you success rate is already at 100%. It's very easy to reach 100% success rate with mastery clothes, for example base (67%) + seafood cron meal (10%) + 1 artifact (5%) + verdure draught (20%). That means in practice, the success rate is only useful when you don't have all buffs running.

<img align="left" src="/files/processing_faq/clothes_collage.png">

Therefore:
- **For profit:** Always use mastery clothes. The extra mastery brackets are more valuable than success rate 99% of the time.
- **For EXP:** You have to weigh the extra mastery brackets from mastery clothes against the extra sucess rate *and* the processing EXP from silver clothes. This of course depends on the grade of SE or mastery clothes in question. You can do an exact comparison using [this sheet](https://docs.google.com/spreadsheets/d/1Yv9-k7hShtmZ6oPZCmLu8C-eGJLgPkg7wvaIkJ_eres/edit#gid=268682067). As a rule of thumb, mastery clothes are preferred when going for EXP.

# Leveling and Moneymaking

## 15. How to level processing?

### Beginner to Professional
*Heat* <!-- db_item-5802-0 --> into <!-- db_item-5852-0 -->

### Professional to Artisan
*Grind* <!-- db_item-5852-0 -->d into <!-- db_item-5856-0 -->

### Artisan+ (to guru 50 if you want)
There are a few ways to level processing on a larger scale. One of these has becomethe 'go-to' method for leveling processing because it's effective, fairly straightforward and doesn't require selling materials on the market.
You may have already heard about it as the 'timber' or 'ship repair material' method. Here's how it works:

**The method:** 

1) Buy any cheap timber
2) Chop timber→planks→plywood→ship repair material (SRM) 
3) Sell the SRM to any NPC (vendors for 4k silver each)
 
**Why this works:** 

This method uses a 'feature' (you may call it a bug :) ) of mass processing. Chopping timber into planks has a 5% chance to directly proc plywood. Planks give 200 EXP when proced, which is each craft. Plywood gives 500 EXP when proced, which happens with a 5% chance. Here is where the 'feature' comes into play: When mass processing timber into planks and one of the crafts in the batch procs one plywood (which is extremely common with a decent number of batches), the game mistakenly adds the EXP from the plywood proc to the whole batch. That means you get the plank EXP (200) and the plywood EXP (500) for a total of 700 EXP for all crafts in the batch. It's technically a bug but the developers haven't bothered fixing it for years. [Full explanation](https://cdn.discordapp.com/attachments/589711952234676224/1022215657368080464/unknown.png) by Goroshi.
 
This leads to the following effective EXP rates:
- Timber→planks with the bug: 700 EXP (the same goes for ore→melted shards, raw hide→hide and plume→feather)
- Planks→plywood: 500 EXP (yes, this gives less than timber→planks)
- Plywood→SRM: 1000 EXP.
- Partial chain - Timber→plywood: 660 EXP 
- full chain - Timber→SRM: 728 EXP

The EXP bug is not specific to timber, it applies to all materials with a direct T3 proc on T1→T2 recipes, like ore, feathers and hide. It does *not* work for fabrics because the processing type switches from T1→T2 (heating) and T2→T3 (grinding) which means T1→T2 can not proc T3 materials.

**How much money does it cost?** You can break even on the costs when buying timber below 540 silver. But I wouldn't stress too much about the price. Timber bought below 1000 silver will lose you 'only' ~5-20 mil/H depending on your mastery.

**Can I level processing while profiting by processing?** You sure can. Consider processing ore into ingots and timber into plywood, which will be slightly less EXP/H than the timber→SRM route but can be profitable depending on market prices. You can check <https://bdolytics.com/processing/market> for processing profits.

For all your EXP needs, here is a link to [Bearist's Processing EXP Calculator](https://docs.google.com/spreadsheets/d/1KqP9lgTK0bDulLJ_JcILG4tn0iWrh5JkY1WHaitSxHo/edit?usp=sharing).

## 16. Which EXP buffs can I run while leveling processing?

Decide based on which buffs you have access to and which buffs are reasonable to use.

| Item                              | Life EXP  | Source                           |
|-----------------------------------|-----------|----------------------------------|
| Silver Embroidered Clothes        |   5%-40%  | MP (Marketplace)                 |
| Professional Clothes (Costume)    |    10%    | Equipment Tailoring Coupon       |
| Mastery Accessories               | up to 75% | MP / yoink from main             |
| Lightstone Combo (incl. stones)   | 20% / 25% | MP                               |
| Artifacts                         |   3%/5%   | Lifeskilling                     |
| Treant's Tear                     |    30%    | Season quest                     |
| Caphras Journal of Nature         |    10%    | Caphras Journal                  |
| Seafood Cron Meal (Food)          |    10%    | MP                               |
| Verdure Draught (Elixir)          |    20%    | MP                               |
| Perfume of Swiftness (Perfume)    |    20%    | MP                               |
| GMs Blessing (1/2/3)              |   10-15%  | Rewards                          |
| Secret Book of Old Moon           |    50%    | Pearl Shop / Loyalties / Rewards |
| Sealed Book of Life / Life Scroll |    50%    | Pearl Shop / Rewards             |
| Villa Buff (Turning Gates)        |    10%    | Villa / Tent (Pearl Shop)        |
| Cake Buff (2h)                    |    100%   | Anniversary                      |
| Cake Buff (24h)                   |    100%   | Account B-day                    |
| Secret Book of Florin             |    20%    | Lara / Events                    |
| Guild Buff                        | 10% / 20% | Guild                            |
| Guru’s Touch (Guild Drill)        |    40%    | Guild                            |
| Donkey Gear Buff (3-piece)        |    10%    | Donkey Krogdalo Set              |
| Pets                              | up to 50% | Pearl Shop / Rewards             |
| Value Pack                        |    30%    | Pearl Shop / Rewards             |
| Server-wide Event Buff or Olvia   |  50%-100% | Event / Olvia                    |
| Giovan Grolin's Support Scroll    |    20%    | Event                            |
| Six Leaf Clover                   |     8%    | Event                            |
| Hearty Grilled Turkey             |    10%    | Event                            |
| Lara's Warm Black Tea             |    30%    | Event                            |
| Special Coconut Juice             |    10%    | Event                            |

Table: EXP buffs as of October 2022

## 17. How to make money with processing?

Processing has two main marktets:
- Crate materials: plywood and ingots
- Cooking materials: flour/dough/cheese/cream/butter

Those recipes give stable profits. By far not all processing markets are like that. There is a set of sub-markets feeding into workshops, manos gear crafting that are characterized by rather low demand and fluctuating prices.

You can check processing profits on [bdolytics](https://bdolytics.com/processing/market). And make sure to enter your processing mastery in the settings.

**Pro tip**: Do yourself a favor and sort by `Daily Volume`. If you sort by `Silver/Hour`, you'll get a best-off parade of all items with exceptional profit but extreme downsides/bottlenecks, which require special attention (see the next question).

## 18. What about that 3 bil/H recipe on bdolytics?

<img width="300" src="/files/processing_faq/nichemarket2.png">

This is a screenshot from <https://bdolytics.com/processing/market>.

`Processing is 3 bil/H?? I have to get on that! Where's the catch?`

Let's look at three examples:

1. <!-- profit_processing-5865 -->: 3 bil/H looks pretty good, huh? But take a look at the daily volume. 220 units sold a day. In an hour of processing at 2k mastery, you could produce 25k dawn fallen silk, which is enough to fully supply the market for almost two weeks. Therefore you should take the 3 bil/H figure with a huge grain of salt. Effectively what it means is: any time spent on this recipe is very much worth it but this time is heavily limited. -> **Problem 1: Limited demand**

2. <!-- profit_processing-4264 -->: Mythril ingots, shards or ore needed to craft pure mythril crystals are extremely hard to come by. Pre-orders fill slowly and there is no way to gather them efficiently. The question now becomes whether the profit is still worth it considering the effort it takes to get the materials.  -> **Problem 2: Limited supply**

3. Since supply and/or demand for those items is so small, prices tend to fluctuate a lot. Unfortunately, a slight change in input material or product price can easily make these recipes go from +3 bil/H to -3 bil/H -> **Problem 3: Price fluctuations and razor-thin margins**

Niche market processing means researching recipes on your own dealing with the inherent difficulties of these recipes:
- Dealing with problem 1: Expand your profit avenues by crafting and selling multiple items at once to not oversupply the market.
- Dealing with problem 2: You can address supply problems by pre-ordering items or crafting/gathering them yourself.
- Dealing with problem 3: Forming product chains can be a good way to stabilize margins, for example turning metal solvent into pure crystal, where the saved tax on the metal solvent can be difference between turning a profit on the craft or not.

I hope this outlines why niche market processing is a lot more difficult to get into than processing for the common markets.
To get into niche market processing, you'll be spending initial time on research and then time each day checking prices and listing/re-listing items.
The time spent processing and managing your sales can far exceed what you could make through other activities. But I personally find it quite stressful.

That's why I tend to look at niche market processing not as `profit per hour` but `profit per headache`. Make of that what you will :)

# Other

## 19. Help, I can't equip a processing stone on my season character D:

Tough luck. We can only hope that PA fixes this in the future.

## 20. How do I increase my weight for processing?

- Pearl shop and loyalty weight
- <!-- db_item-9691-0 -->: 100 LT / <!-- db_item-9642-0 -->: 300 LT
- <!-- db_item-791-0 -->: 200 LT
- 4x <!-- db_item-15665-0 --> or <!-- db_item-15662-0 --> in mainhand and sub-weapon: 150 LT + 60 LT if you run HAN crystals
- Clang! Clang! lightstone set: 30 LT
- Alchemy stone: varies (spirit stone doesn't give weight!)

**Thanks for reading. If you have suggestions, corrections, please write a message to Summer#8727 or @ me in the Lifskill Discord.**

---
title: Processing FAQ - Answsers to 20 Common Questions
head:
  image: /guides/summer_processing_faq/thumbnail.png
author:
  name: Summer
  avatar: https://yt3.ggpht.com/5iMEYzZd9s2ey6I9BIffvTSnuO_4hc9VXU4VxPxTud4OOyu-0vX5Y-WWhL463Olk8zZmiGudrQ=s88-c-k-c0x00ffffff-no-rj
  link: https://www.youtube.com/channel/UCPCDg8Ib5VVrwCF0gGcqEmQ
date: 2022-11-13
lang: en
---

*Last updated: November 13, 2022*

Heya, I'm Summer and I made this post to help you out with any questions you may have about processing.
It's essentially a processing guide but the FAQ-style format is a bit nicer to `ctrl+f` in case you are looking for specific info.

Enjoy :)

## Preface - for very interested readers :) 

### What is processing?
Processing is about taking raw materials, for example produced by your worker empire, and refining them for use in further activities like trading, cooking and workshops. It's a low effort lifeskill and doesn't take a whole lot to get started. One of the coolest things about processing is that once you get further into it you can form elaborate recipe chains to craft valuable items, like <!-- db_item-4006-0 --> (gathering) -> <!-- db_item-4076-0 --> (alchemy) -> <!-- db_item-4053-0 --> (processing) -> <!-- db_item-16162-0 --> (workshops).

### The state of processing
Processing for profit has seen better times, partly because some of the activities it feeds into, like trading and workshops, have seen better times too. The moneymaking potential has noticeably fallen behind comparable lifskills like bartering and cooking. Nowadays, the main appeal of processing is being low effort and afk-able. 

On the bright side, leveling processing is fairly straight-forward ([question 14](#14-how-do-i-level-processing)). To earn money, you have a few recipes at your disposal ([question 16](#16-how-to-make-money-with-processing)). Processing markets these days are stable for the most part, which means I can share some for-profit recipes with you without negatively impacting the market. Beyond that, finding recipes has never been easier with tools like [bdolytics](/processing/market).

## Overview

| Topic                                 | Question                                                                                                                                          |
|---------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------|
| Basics                                | [1. How to process?](#1-how-to-process)                                                                                                           |
|                                       | [2. How can I stop processing from failing?](#2-how-can-i-stop-processing-from-failing)                                                           |
| Mass Processing and Mastery           | [3. What is mass processing?](#3-what-is-mass-processing)                                                                                         |
|                                       | [4. What does processing mastery do?](#4-what-does-processing-mastery-do)                                                                         |
|                                       | [5. How much processing mastery do I need?](#5-how-much-processing-mastery-do-i-need)                                                             |
|                                       | [6. Why can't I mass process this item?](#6-why-cant-i-mass-process-this-item)                                                                    |
| Recipes, Proc Rates and Process Times | [7. How many items does a craft yield and what affects it?](#7-how-many-items-does-a-craft-yield-and-what-affects-it)                             |
|                                       | [8. How long can I afk process for?](#8-how-long-can-i-afk-process-for)                                                                           |
|                                       | [9. Why can't I chop plyoowd / heat pure crystals?](#9-why-cant-i-chop-plyoowd--heat-pure-crystals)                                               |
| Gear                                  | [10. What gear do I need?](#10-what-gear-do-i-need)                                                                                               |
|                                       | [11. How can I get processing artifacts?](#11-how-can-i-get-processing-artifacts)                                                                 |
|                                       | [12. Do I need the pearl shop costume?](#12-do-i-need-the-pearl-shop-costume)                                                                     |
|                                       | [13. Should I use mastery or silver embroidered clothes? ](#13-should-i-use-mastery-or-silver-embroidered-clothes)                                |
| Leveling and Moneymaking              | [14. How do I level processing?](#14-how-do-i-level-processing)                                                                                   |
|                                       | [15. Which EXP buffs can I run while leveling processing?](#15-which-exp-buffs-can-i-run-while-leveling-processing)                               |
|                                       | [16. How to make money with processing?](#16-how-to-make-money-with-processing)                                                                   |
|                                       | [17. Do I have to combine processing with trading to make it profitable?](#17-do-i-have-to-combine-processing-with-trading-to-make-it-profitable) |
|                                       | [18. What about that 3 bil/H recipe on bdolytics?](#18-what-about-that-3-bilh-recipe-on-bdolytics)                                                |
| Misc                                  | [19. Help, I can't equip a processing stone on my season character D:](#19-help-i-cant-equip-a-processing-stone-on-my-season-character-d)         |
|                                       | [20. How do I increase my weight for processing?](#20-how-do-i-increase-my-weight-for-processing)                                                 |


## 1. How to process?
1. Open the processing window (L key)
2. Select a processing type 
3. Input the materials
4. Press 'Start' or 'Mass Process' (more on mass processing in [question 4](#4-what-does-processing-mastery-do))

<video width="640" height="360" muted autoplay controls>
    <source src="/guides/files/summer_processing_faq/howtoprocess.mp4" type="video/mp4">
</video>

Processing can have the follow outcomes:
| Message                                           | Meaning                                                                                                             |
|---------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| `Processing has succeeded`                        | The craft succeeds.                                                                                                 |
| `Processing is not going as planned`              | The craft has 'missed' and will be re-tried. ([question 2](#2-how-can-i-stop-processing-from-failing))          |
| `It is not working at all`                        | You input the wrong recipe or are missing knowledge ([question 9](#9-why-cant-i-chop-plyoowd--heat-pure-crystals)). |
| `Insufficient ingredients to continue processing` | You got the recipe right but don't have enough materials for a full craft.                                          |

Don't worry, materials will only be consumed if the craft succeeds.

## 2. How can I stop processing from failing?

Even if you meet all conditions to succeed the craft, the message `Processing is not going as planned` can appear and your character has to re-try the craft.
The chance of this happening depends on your **processing success rate**, which is 70%* at base and goes up to 100%.

Here's how to increase your success rate:
| Category           | Item                                                  | Success Rate |
|--------------------|-------------------------------------------------------|--------------|
| Pearl Shop Costume | <!-- db_item-603044-0 --> / <!-- db_item-560024-0 --> |      3%      |
| Clothes            | <!-- db_item-14026-0 -->                              |    6%-40%    |
| Food               | <!-- db_item-9691-0 --> (2 hours)                     |      10%     |
|                    | <!-- db_item-9642-0 --> (10 hours)                    |      15%     |
| Elixir/Draught     | <!-- db_item-791-0 --> (15 mins)                      |      20%     |
| Alchemy Stone      | <!-- db_item-45302-0 -->                              |      11%     |
|                    | <!-- db_item-45280-0 -->                              |      11%     |
|                    | <!-- db_item-45284-0 -->                              |      14%     |
| Artifcats          | <!-- db_item-735354-0 -->                             | 5%, up to 2x |
| Lightstone Set     | <!-- db_lightstoneset-167-0 -->                       |      20%     |

Items in the same category don't stack.

You may have heard that the success rate *cannot* reach 100%. According to tests by the lifeskill community, we're almost certain that the success rate **can** reach 100%. However, some items seem to have a different success rate than indicated in the item description. This includes <!-- db_item-14026-0 -->, the <!-- db_lightstoneset-167-0 --> set and potentially <!-- db_item-791-0 -->. So to get 100% it helps to overstack success rate buffs by a few percent.

\**We used to think that the base success rate is 67% but a recent source shows it to be 70%. Unfortunately, testing success rate is extremely tedious so we have no definite way of telling which is correct.*

## 3. What is mass processing?

### What it does

Mass processing lets you process **mutltiple batches of items** at once. It also **takes 10x longer** than regular processing.
Example: processing *timber* into *planks*:
- Regular processing: 6 second craft time, 1 craft at a time
- Mass processing: 60 seconds craft time, 10+ crafts at a time

<img src="/guides/files/summer_processing_faq/mass_proc.png">

The number of mass processing crafts depends on your mastery ([question 4](#4-what-does-processing-mastery-do)).

You need a <!-- db_item-768088-0 --> / <!-- db_item-768087-0 --> / <!-- db_item-768086-0 --> to get access to the 'Mass Process' button in the processing menu.

### What you can mass process

Mass processing only works on stackable items. You can't mass dry for example *fish* because they take up 1 inventory slot each.

Also, it only works on *Shaking, Grinding, Chopping, Drying, Filtering, Heating*.

There is no mass processing for *Simple Alchemy, Simple Cooking, Imperial Cuisine, Imperial Alchemy, Guild Processing, Manufacturing*.

### Use mass processing or regular processing?

There is no downside to mass processing. At worst, it's as fast as regular processing and gets faster the more mastery you have (fast as in crafts per hour, not craft time).

Therefore:

<span style="color:green;font-weight:bold">If a recipe can be mass processed you should mass process it</span>

## 4. What does processing mastery do?

Processing mastery increases the number of crafts ('batches') you can perform at once through mass processing.
For example, with `1020 mastery` you can perform `90 crafts` at once. 

It does *not* affect how many items you get each craft.

| Mastery | Batches | Mastery | Batches | Mastery | Batches |
|:-------:|:-------:|:-------:|:-------:|:-------:|:-------:|
|    2    |    10   |   440   |    32   |   930   |    76   |
|    20   |    11   |   460   |    33   |   960   |    80   |
|    40   |    12   |   480   |    34   |   990   |    85   |
|    60   |    13   |   500   |    35   |   1020  |    90   |
|    80   |    14   |   520   |    36   |   1060  |    96   |
|   100   |    15   |   540   |    37   |   1100  |   112   |
|   120   |    16   |   560   |    38   |   1140  |   118   |
|   140   |    17   |   580   |    39   |   1180  |   124   |
|   160   |    18   |   600   |    40   |   1220  |   130   |
|   180   |    19   |   620   |    41   |   1260  |   137   |
|   200   |    20   |   640   |    42   |   1300  |   144   |
|   220   |    21   |   660   |    43   |   1350  |   154   |
|   240   |    22   |   680   |    45   |   1400  |   162   |
|   260   |    23   |   700   |    47   |   1450  |   170   |
|   280   |    24   |   720   |    49   |   1500  |   178   |
|   300   |    25   |   740   |    51   |   1550  |   186   |
|   320   |    26   |   760   |    53   |   1600  |   194   |
|   340   |    27   |   780   |    57   |   1650  |   203   |
|   360   |    28   |   810   |    60   |   1700  |   212   |
|   380   |    29   |   840   |    64   |   1800  |   222   |
|   400   |    30   |   870   |    68   |   1900  |   235   |
|   420   |    31   |   900   |    72   |   2000  |   250   |

*Table: mastery brackets and mass processing batches. Note that processing mastery brackets are not evenly spaced out at every 50 mastery like in other lifeskills but they vary from 20 to 100 mastery.*


## 5. How much processing mastery do I need?

In other lifeskills, more mastery is always better. That only applies to processing to a certain point.
Having higher processing mastery lets you process items at a faster rate but weight is still a limiting factor. With high enough mastery it's possible that your character will run out of weight before checking back on your processing. Increasing processing mastery beyond that point won't increase the number of materials you can process in one afk session. Also processing mastery scales fairly linear. There are no major breakpoints.

So here's my advice: 

<span style="color:green;font-weight:bold">Get your processing mastery to a point where you will barely run out of weight whenever you check back on your processing (on whichever recipe you commonly process).</span>

## 6. Why can't I mass process this item?

The is no mass processing for *Simple Alchemy, Simple Cooking, Imperial Cuisine, Imperial Alchemy, Guild Processing, Manufacturing*.

Though some recipes have alternative '10x' versions which let you do 10 crafts at once by adding a certain item:
| Processing Type  | Recipe                                                                      | Item                      | How to obtain    | Requirement                                                           |
|------------------|-----------------------------------------------------------------------------|---------------------------|------------------|-----------------------------------------------------------------------|
| Simple Alchemy   | <!-- db_item-721003-0 -->, <!-- db_item-5000-0 -->, <!-- db_item-4987-0 --> | <!-- db_item-4901-0 -->   | Central Market   | -                                                                     |
| Simple Alchemy   | Party Elixirs, Blue Elixirs, Draughts                                       | <!-- db_item-4986-0 -->   | Material Vendor  | Alchemy skilled 1                                                     |
| Simple Cooking   | Cron Meals                                                                  | <!-- db_item-820015-0 --> | Cooking Vendor   | Cooking skilled 1                                                     |
| Imperial Cuisine | Cooking Boxes                                                               | <!-- db_item-8198-0 -->   | Old Moon Manager | Cooking artisan 1, <!-- db_quest-2062-1 --> 							|
| Imperial Alchemy | Medicine Boxes                                                              | <!-- db_item-8198-0 -->   | Old Moon Manager | Alchemy artisan 1, <!-- db_quest-2062-2 --> 							|

<img src="/guides/files/summer_processing_faq/caphras_recipe.png">

*Top: '10x' recipe*
*Bottom: regular recipe*

## 7. How many items does a craft yield and what affects it?

### Craft yield

Most recipes yield `1-4 items (~2.5 on average)` but proc rates can vary between recipes. The table below shows proc rates as well as other info for common processing recipes.
You can also check proc rates by going to a [specific recipe](/processing/market/4651) on bdolytics and comparing the output materials to the number of crafts.

### What affects the proc rate?
`Proc rate is fixed and neither affected by mastery nor by whether you're regular or mass processing, with one exception: Getting maximum procs requires a certain processing level for some recipes.`

- *Shaking, Grinding, Chopping, Drying, Diltering, Heating* cap out at a certain processing level. For example, timber caps out at artisan 6 and ore at master 1. Once you're master 1, you'll have the maximum proc rate on 99% of recipes. A few recipes, like <!-- db_item-4269-0 --> require guru 1 for maximum procs.
- *Simple Alchemy, Simple Cooking, Imperial Cuisine, Imperial Alchemy, Guild Processing, Manufacturing* recipes have fixed rates and are not affected by processing level. You can let your beginner 1 alt do these recipes without worrying about losing out on procs :)

### Common processing recipes

| Recipe                                    | Example                                                                                                       | Process Type   | Proc Range | Proc Avg |   Level Req.   |    EXP   |  Time  | Required Knowledge       |
|-------------------------------------------|---------------------------------------------------------------------------------------------------------------|----------------|:----------:|:--------:|:--------------:|:--------:|:------:|--------------------------|
| Plank (T2)                                | <!-- db_processing-recipe-1159-0 -->                                                                          | Chopping       |     1-4    |    2.5   |    Artisan 6   |  200/500 |  6/60  | -                        |
| Plywood (T3)                              | <!-- db_processing-recipe-1160-0 -->                                                                          | Chopping       |     1-4    |    2.5   | Professional 6 |    500   |  6/60  | <!-- db_knowledge--0 --> |
| Sturdy Plywood (T4)                       | <!-- db_processing-recipe-1161-0 -->                                                                          | Heating        |     1-3    |     2    |  Professonal 1 |   1000   |  6/60  | <!-- db_knowledge--0 --> |
| Melted Shard (T2)                         | <!-- db_processing-recipe-803-0 -->                                                                           | Heating        |     1-4    |    2.5   |    Master 1    |  200/500 |  9/90* | -                        |
| Ingot (T3)                                | <!-- db_processing-recipe-923-0 -->, <!-- db_processing-recipe-995-0 -->                                      | Heating        |     1-4    |    2.5   |    Artisan 1   |    500   |  9/90* | <!-- db_knowledge--0 --> |
| Precious Ingot (T3)                       | <!-- db_processing-recipe-1061-0 -->, <!-- db_processing-recipe-1080-0 -->                                    | Heating        |     1-4    |    2.5   |    Artisan 1   |    800   | 9/80** | <!-- db_knowledge--0 --> |
| Mixed Ingot (T3)                          | <!-- db_processing-recipe-984-0 -->, <!-- db_processing-recipe-988-0 -->, <!-- db_processing-recipe-985-0 --> | Heating        |     1-4    |    2.5   |    Artisan 1   |    800   |  6/60  | <!-- db_knowledge--0 --> |
| Pure Crystal (T4)                         | <!-- db_processing-recipe-934-0 -->                                                                           | Heating        |     1-3    |     2    |  Professonal 1 |   1000   |  6/60  | <!-- db_knowledge--0 --> |
| Precious Pure Crystal (T4)                | <!-- db_processing-recipe-1062-0 -->, <!-- db_processing-recipe-1081-0 -->                                    | Heating        |     1-3    |     2    |  Professonal 1 |   1500   |  6/60  | <!-- db_knowledge--0 --> |
| Hide (T2)                                 | <!-- db_processing-recipe-1603-0 -->                                                                          | Drying         |     1-4    |    2.5   |  Professonal 1 |  200/500 |  9/90  | -                        |
| Fine Hide (T3)                            | <!-- db_processing-recipe-1629-0 -->                                                                          | Drying         |     1-4    |    2.5   |    Skilled 1   |    500   |  9/80  | <!-- db_knowledge--0 --> |
| Supreme Hide (T4)                         | <!-- db_processing-recipe-1637-0 -->                                                                          | Shaking        |     1-3    |     2    |  Apprentice 1  |   1000   |  9/80  | <!-- db_knowledge--0 --> |
| Feather (T2)                              | <!-- db_processing-recipe-1623-0 -->                                                                          | Filtering      |     1-4    |    2.5   |  Professonal 6 |  200/500 |  6/60  | -                        |
| Fine Feather (T3)                         | <!-- db_processing-recipe-1634-0 -->                                                                          | Filtering      |     1-4    |    2.5   |    Skilled 6   |    500   |  9/80  | <!-- db_knowledge--0 --> |
| Supreme Feather (T4)                      | <!-- db_processing-recipe-1644-0 -->                                                                          | Shaking        |     1-3    |     2    |  Apprentice 1  |   1000   |  9/80  | <!-- db_knowledge--0 --> |
| Gem (T2)                                  | <!-- db_processing-recipe-1111-0 -->                                                                          | Grinding       |     1-4    |    2.5   |    Artisan 1   | 500/1000 |  9/80  | -                        |
| Resplendent Gem (T3)                      | <!-- db_processing-recipe-1112-0 -->                                                                          | Grinding       |     1-3    |     2    |    Skilled 1   |   1000   |  9/80  | <!-- db_knowledge--0 --> |
| Special Gem (T4)                          | <!-- db_processing-recipe-1113-0 -->                                                                          | Shaking        |     1-2    |    1.5   |  Apprentice 1  |   2000   |  6/80  | <!-- db_knowledge--0 --> |
| <!-- db_processing-recipe-4669-0 --> (T2) |                                                                                                               | Chopping       |     1-4    |    2.5   |    Artisan 6   | 500/1000 |  6/60  | -                        |
| <!-- db_processing-recipe-1190-0 --> (T3) |                                                                                                               | Chopping       |     1-3    |     2    | Professional 6 |   1000   |  6/60  | <!-- db_knowledge--0 --> |
| <!-- db_processing-recipe-1191-0 --> (T4) |                                                                                                               | Heating        |     1-3    |     2    |    Artisan 1   |   1500   |  6/60  | <!-- db_knowledge--0 --> |
| <!-- db_processing-recipe-2869-0 -->      |                                                                                                               | Shaking        |     1-4    |    2.5   |    Skilled 1   |    150   |  6/60  | -                        |
| <!-- db_processing-recipe-2871-0 -->      |                                                                                                               | Shaking        |     1-4    |    2.5   |    Skilled 1   |    150   |  6/60  | -                        |
| <!-- db_processing-recipe-2870-0 -->      |                                                                                                               | Drying         |     1-4    |    2.5   |    Skilled 1   |    300   |  9/60  | -                        |
| <!-- db_processing-recipe-1867-0 -->      |                                                                                                               | Grinding       |     1-4    |    2.5   | Professional 1 |    70    |  6/60  | -                        |
| <!-- db_processing-recipe-1894-0 -->      |                                                                                                               | Shaking        |     1-4    |    2.5   |    Skilled 1   |    150   |  6/60  | -                        |
| Thread/Yarn (T2)                          | <!-- db_processing-recipe-1548-0 -->                                                                          | Heating        |     1-4    |    2.5   |    Artisan 1   |    500   |  6/60  | -                        |
| Fabric/Wool/Silk (T3)                     | <!-- db_processing-recipe-1552-0 -->                                                                          | Grinding       |     1-4    |    2.5   | Professional 1 |   1000   |  6/60  | -                        |
| <!-- db_processing-recipe-1259-0 -->      |                                                                                                               | Grinding       |    40-60   |    50    |    Artisan 1   |    80    |  9/80  | -                        |
| <!-- db_processing-recipe-1230-0 -->      |                                                                                                               | Grinding       |   60-100   |    80    |    Artisan 1   |    80    |  9/80  | -                        |
| <!-- db_processing-recipe-1776-0 -->      |                                                                                                               | Filtering      |     1-4    |    2.5   |    Artisan 1   |    300   |  6/60  | -                        |
| <!-- db_processing-recipe-1193-0 -->      |                                                                                                               | Chopping       |     1-3    |     2    |    Artisan 1   |   1000   |  6/60  | -                        |
| <!-- db_processing-recipe-986-0 -->       |                                                                                                               | Grinding       |     1-4    |    2.5   |    Artisan 1   |    500   |  6/60  | -                        |
| Cron Meal                                 | <!-- db_processing-recipe-9692-0 -->                                                                          | Simple Cooking |      1     |     1    |   Beginner 1   |     0    |    6   | -                        |
| Draught                                   | <!-- db_processing-recipe-2008-0 -->                                                                          | Simple Alchemy |      1     |     1    |   Beginner 1   |     0    |    6   | -                        |
| Party Elixir                              | <!-- db_processing-recipe-1730-0 -->                                                                          | Simple Alchemy |     1-2    |    1.8   |   Beginner 1   |     0    |    6   | -                        |
| Blue Elixir                               | <!-- db_processing-recipe-1883-0 -->                                                                          | Simple Alchemy |      1     |     1    |   Beginner 1   |     0    |    6   | -                        |
| <!-- db_processing-recipe-1439-0 -->      |                                                                                                               | Simple Alchemy |      1     |     1    |   Beginner 1   |     0    |    9   | -                        |
| <!-- db_processing-recipe-1426-0 -->      |                                                                                                               | Simple Alchemy |      1     |     1    |   Beginner 1   |     0    |    9   | -                        |
| <!-- db_processing-recipe-1901-0 -->      |                                                                                                               | Simple Alchemy |      1     |     1    |   Beginner 1   |     0    |    6   | -                        |

**Notes about this table**

- **Level Req.**: Level required to gain the maximum proc rate
- **EXP**: Processing EXP. when two values are shown, the first one indicates the regular proc (e.g. ash plank: 200 EXP) and the second one the rare proc (e.g. ash plywood: 500 EXP)
- **Time**: regular processing / mass processing time in seconds

\* Zinc shards/ingots take 6/60 seconds. Ores are a huge mess in general.

\*\* Some 9s recipes seem to take 80 seconds when mass processed. Don't ask me why.

*Source for the data: Daz' sheets, Bdocodex, bdolytics, in-game testing for the times.*

## 8. How long can I afk process for?

It depends on the **materials** you're processing and your **max weight**. This list shows the weight of common materials:

| Item                                 | Weight (LT) |
|--------------------------------------|-------------|
| Timber                               |         0.5 |
| Ore, Gems, Stone                     |         0.3 |
| Hide, Fabric, Feathers, Flour, Dough |         0.1 |
| Cheese, Cream, Butter                |        0.01 |

On bdolytics, you can check how long you can process for before running out of weight:

<video width="640" height="360" muted autoplay controls>
    <source src="/guides/files/summer_processing_faq/howto_weight.mp4" type="video/mp4">
</video>

1. Open the **settings** and enter your *weight*, *fairy feathery steps level*, *processing mastery*, *success rate* and whether you have the *processing costume* (more on the processing costume in [question 13](#12-do-i-need-the-pearl-shop-costume))
2. Go to the **recipe page** of the item you want to process.
3. Go to the **WEIGHT** tab.
4. Read the **Max. Crafts** and input it as the **Craft Quantity**.
5. Go back to the **INPUT&OUTPUT** tab and check the **time**.

### Overnight Processing

Some items are so light that you can process them for multiple hours or even overnight. 

Common recipes for **overnight processing** are <!-- profit_processing-9061 -->, <!-- profit_processing-9062 --> and <!-- profit_processing-9063 -->.

## 9. Why can't I chop plyoowd / heat pure crystals?

<span style="color:green;font-weight:bold">You are missing knowledge</span>

To chop planks into plywood (T3) you need `Chopping: Beginner`. To heat ingots into pure crystals (T4) you need `Heating: Skilled` and so on. You can get the knowledge entries through a quest chain, which is outlined below.

### Beginner Knowledge Quest Chain

|                    |                                                                                                                                                                                    |
|--------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Rewarded knowledge | <!-- db_knowledge-6554-0 -->, <!-- db_knowledge-6557-0 -->, <!-- db_knowledge-6560-0 -->, <!-- db_knowledge-6555-0 -->, <!-- db_knowledge-6556-0 -->, <!-- db_knowledge-6559-0 --> |
| Starting quest     | <!-- db_quest-2100-28 -->                                                                                                                                                          |
| Starting NPC       | <!-- db_npc-50210-1 --> in Heidel                                                                                                                                                  |
| Requirements       | Apprentice 4 gathering OR have completed <!-- db_quest-2100-22 -->                                                                                                                 |

[Video guide](https://www.youtube.com/watch?v=TvmMImSGl88)

You can track the quest in-game via the quest menu:
1. In the quest menu (*O key*), go to the 'Suggested' tab and look for *[Life][Certificate] Skilled Paradim*.
2. Make sure that you fulfill the quest requirements.
3. Enable all quests at the bottom of the tab.

<img width="1000" src="/guides/files/summer_processing_faq/questbeginner2.png">

### Skilled Knowledge Quest Chain

|                    |                                                                                                                                                                                    |
|--------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Rewarded knowledge | <!-- db_knowledge-6561-0 -->, <!-- db_knowledge-6564-0 -->, <!-- db_knowledge-6566-0 -->, <!-- db_knowledge-6562-0 -->, <!-- db_knowledge-6563-0 -->, <!-- db_knowledge-6565-0 --> |
| Starting quest     | <!-- db_quest-3208-1 -->                                                                                                                                                           |
| Starting NPC       | !-- db_npc-578-432 --> next to the blacksmith in Keplan                                                                                                                            |
| Requirements       | Gathering skilled 10 AND processing skilled 5 AND all 6 pieces of beginner knowledge            
                                                                                   |   |
[Video guide](https://youtu.be/TvmMImSGl88?t=168)

## Help, I can't see the starting quest!
Possible Reasons:
- You don't fulfill the quest requirements
- You don't have all quests enabled
- You already have the knowledge: check the knowledge tab (H key) -> *Life Skill* -> *Certificates*
- You have already accepted the quest: check your quest tab (O key)

<span style="color:green;font-weight:bold">If you are struggling with any of the quests despite reading through this section, feel free to message me on Discord at Summer#8727 and I'll walk you through the questline.</span>

## 10. What gear do I need?

You technically don't need any gear to process. A processing stone is needed if you want to mass process recipes. Beyond that, increasing your mastery and processing success rate can massively speed up the rate at which your process items.



Here are my <span style="color:green;">personal gear recommendations</span> based on silver efficiency. Feel free to go for a different setup where you see fit.

### Beginner

| Slot             | Recommended Gear           |
|------------------|----------------------------|
| Processing Stone | <!-- db_item-768088-18 --> |
| Clothes          | <!-- db_item-705514-18 --> |

Total cost: `~300 mil`

This gear will give a total of 260 processing mastery, which lets you process 23 batches at once. This does not include any additional mastery you may have from levels or from accessories.

### Intermediate

| Slot             | Recommended Gear                                                                													        |	
|------------------|--------------------------------------------------------------------------------------------------------------------------------------------|
| Processing Stone | <!-- db_item-768087-19 -->                                                                                                                 |
| Clothes          | <!-- db_item-705514-19 --> / <!-- db_item-705516-19 -->                                                                                    |
| Artifacts        | <!-- db_item-735372-0 --> / <!-- db_item-735361-0 --> / <!-- db_item-735354-0 --> / <!-- db_item-735351-0 --> / <!-- db_item-735352-0 -->  |
| Lighstones       | <!-- db_lightstoneset-167-0 -->                                                                                                            |

Total cost: `~1.5b - 3b`

<!-- db_item-768087-19 --> is good bang for your buck. Depending on your budget, you can go for <!-- db_item-705514-19 --> or <!-- db_item-705516-19 -->. If you can snipe <!-- db_item-705516-19 --> from the market it's a great option. Enhancing it yourself will cost `~1.5b` on average. For artifacts, it's fine to run whichever ones you have at the moment. The *Clang!Clang!* lighstone combo is great value and makes reaching 100% success rate a piece of cake.

### Advanced

| Slot             | Recommended Gear                                                                   |
|------------------|------------------------------------------------------------------------------------|
| Processing Stone | <!-- db_item-768086-19 -->                                                         |
| Clothes          | <!-- db_item-705516-19 --> / <!-- db_item-705518-19 -->                            |
| Artifacts        | <!-- db_item-735372-0 --> / <!-- db_item-735361-0 --> / <!-- db_item-735354-0 -->  |
| Lighstones       | <!-- db_lightstoneset-167-0 -->                                                    |

Total cost: `~4b - 10b`

The endgame setup will let you reach between 1000 and 2000 mastery depending on your processing level and accessories. <!-- db_item-705518-19 --> are the heavy weight when it comes to cost, which is why <!-- db_item-705516-19 --> can be a great value option even for an endgame setup. If you have multipe artifacts to choose from, you'll be able to optimize based on which stat is needed (see question below).

### Which artifacts should I use?

In theory, the *Clang!Clang!* set (20%) and seafood cron meal (10%) together with the base success rate (70%) should get you to 100%. But as the *Clang!Clang!* set seems to give less success rate than indicated, you will need to add a verdure draught or one success rate artifact to reach 100%.

In general, I would prioritize **mastery artifacts** (if it makes you hit a bracket) **>** **success rate artifacts** (if you don't have 100%) **>** **EXP artifacts**.

### Buy or enhance gear?

Lifeskill gear is generally cheaper to buy than to enhance yourself on average. You can check mastery gear enhance costs using [this sheet](https://docs.google.com/spreadsheets/d/1Me9wRktno6DDB4-of9tUx-SoaA-ezHK_w1BhwvXRrmA/edit?usp=sharing).

## 11. How can I get processing artifacts?
Processing artifacts drop from **imperial cooking turn-ins**, together with cooking artifacts. The chance to get an artifact is quite low (you can expect one to drop maybe every 5-10 turn-ins) so it might take a while until you get the artifact you want.

You don't need to worry about having perfect artifacts. While working on getting processing artifacts, you can still run a lightstone set by using general-purpose artifacts like <!-- db_item-735351-0 -->  or <!-- db_item-735352-0 --> as placeholders. Once you get the processing artifacts, you can then extract the lightstones at a blacksmith with a <!-- db_item-757561-0 --> (bought at blacksmiths) and slot them into the new artifacts.

## 12. Do I need the pearl shop costume?

<!-- db_item-603044-0 --> and <!-- db_item-560024-0 --> can only be bought from the pearl shop, give 3% success rate and will let you **process from storage**. Note that you can only process from storage keepers, not storage containers.

When using a processing costume, the processed materials will go into your character's inventory. That means your character will only stop processing once you go overweight. 
Effectively, the processing costume lets you **stay afk for longer** (about 2 times longer as without the costume) before refreshing your processing. 
BUT the processing costume will not increase the afk time on recipes where the output materials are heavier than the input, like flour, dough, cream, butter and cheese. So the usefulness of the processing costume depends on what you are processing.

In the end, the processing costume is purely a **convenience item**.
It's up to you to decide whether the convenience of being able to stay afk for longer is worth spending pearls on.

## 13. Should I use mastery or silver embroidered clothes? 

<span style="color:green;font-weight:bold">TL;DR: Just use mastery clothes :)</span>

Mastery clothes and silver embroidered (SE) processing clothes have different benefits:
- **Mastery clothes:** Processing mastery -> higher batch processing -> processing at a faster rate
- **SE clothes:** Processing success rate -> processing at a faster rate. Additionally, processing EXP.

However, the success rate from SE clothes won't have any benefit if your success rate is already at 100%. It's very easy to reach 100% success rate with mastery clothes, for example base (70%) + seafood cron meal (10%) + *Clang!Clang!* set (20%) + verdure draught (20%). In practice, the success rate is only useful when you don't have all buffs running.

Therefore:
- **For profit:** Always use mastery clothes. The extra mastery brackets are more valuable than success rate 99% of the time.
- **For EXP:** You have to weigh the extra mastery brackets from mastery clothes against the extra success rate *and* the processing EXP from silver clothes. Depending on your mastery and grade of clothes available to you, either one can be better. You can do an exact comparison using [this sheet](https://docs.google.com/spreadsheets/d/1Yv9-k7hShtmZ6oPZCmLu8C-eGJLgPkg7wvaIkJ_eres/edit#gid=268682067). Though based on this chart, mastery clothes are preferred when going for EXP in most cases.

<img width="600" src="/guides/files/summer_processing_faq/clothes_collage.png">

## 14. How do I level processing?

### Beginner to Professional

Chances are, you have <!-- db_item-5802-0 --> or <!-- db_item-5804-0 --> from workers in your Heidel storage. Otherwise you can buy them quite cheaply on the market. You can *heat* <!-- db_item-5802-0 --> -> <!-- db_item-5852-0 --> (500 EXP) or <!-- db_item-5804-0 --> -> <!-- db_item-5854-0 --> (500 EXP).

### Professional to Artisan

You can take the materials from leveling to professional and *grind* <!-- db_item-5852-0 --> -> <!-- db_item-5856-0 --> (1000 EXP) or <!-- db_item-5854-0 --> -> <!-- db_item-5858-0 --> (1000 EXP).

To liquidate the materials you can either try to sell them on the market or turn them into life clothes (e.g. <!-- db_item-14020-0 --> or <!-- db_item-7423-0 -->)

### Artisan to the moon (guru 50)
There are a few ways to level processing on a larger scale. I want to highlight one specific method that is easy, effective and doesn't require selling materials on the market.
You may have already heard about it as the 'timber' or 'ship repair material' method. Here's how it works:

#### The method

1. **Buy any cheap timber, for example <!-- db_item-4601-0 --> or <!-- db_item-4610-0 -->**
2. **Chop timber -> planks -> plywood -> <!-- db_item-4688-0 --> (SRM)**
3. **Sell the <!-- db_item-4688-0 --> to any NPC (sell price: 4k silver)**
    
#### Why it works

This method uses a 'feature' of mass processing. Chopping timber into planks (`200` EXP) has a `5%` chance to directly proc plywood (`500` EXP). When mass processing timber into planks and one of the crafts in the batch procs plywood, the game mistakenly adds the EXP from the plywood proc to the whole batch. That means you get the plank EXP of `200` and the plywood EXP of `500` for a total of `700` EXP for *all* crafts in the batch. 

The EXP bug doesn't happen when you don't proc any plywood. Though with a decent number of batches, getting no plywood proc is extremely unlikely. It's technically a bug but the developers haven't bothered fixing it for years. [Full explanation](https://cdn.discordapp.com/attachments/589711952234676224/1022215657368080464/unknown.png) by Goroshi.
 
This leads to the following effective EXP rates:
- Timber -> Planks with the bug: `700` EXP
- Planks -> Plywood: `500` EXP (yes, this gives less EXP than timber -> planks)
- Plywood -> SRM: `1000` EXP.
- *Partial chain* - Timber -> Plywood: `660` EXP 
- *Full chain* - Timber -> SRM: `728` EXP

The EXP bug is not limited to timber processing, it applies to all materials with a direct T3 proc on T1->T2 recipes, like ore, feathers and hide. It does *not* work for fabrics because the processing type switches from T1->T2 (heating) to T2->T3 (grinding), which means T1->T2 can not proc T3 materials.

#### How expensive is this method?

You can break even on the costs when buying timber below **540 silver**. 
Though I wouldn't stress too much about the price. Timber bought below 1000 silver will lose you 'only' ~5-20 mil/H depending on your mastery.

#### Any downsides?

Timber is heavy, which leads to extremely **low afk times**. Even with a maxed out weight setup, you're looking at no more than 15 minutes of afk time.

#### Can I level processing and profit?

You sure can. Consider processing ore into ingots and timber into plywood, which will be slightly less EXP/H than the timber->SRM route but can be profitable depending on market prices. 

You can check the [bdolytics processing table](/processing/market) for processing profits and EXP values.

Also, here is a link to [Bearist's Processing EXP Calculator](https://docs.google.com/spreadsheets/d/1KqP9lgTK0bDulLJ_JcILG4tn0iWrh5JkY1WHaitSxHo/edit?usp=sharing).

## 15. Which EXP buffs can I run while leveling processing?

I would pick buffs based on which ones you have access to and which buffs are reasonable to use.

| Item                                                  | Life EXP    | Source                                                                                                 |
|-------------------------------------------------------|-------------|--------------------------------------------------------------------------------------------------------|
| <!-- db_item-14026-0 -->                              |    5%-40%   | Marketplace                                                                                            |
| <!-- db_item-14318-0 -->                              |     10%     | <!-- db_item-17611-0 -->                                                                               |
| Mastery Accessories                                   |  up to 75%  | Marketplace / Enhance                                                                                  |
| Lightstone Combo (incl. stones)                       |  20% / 25%  | Marketplace                                                                                            |
| <!-- db_item-735351-0 --> / <!-- db_item-735361-0 --> |    3%/5%    | Lifeskilling                                                                                           |
| <!-- db_item-721092-0 -->                             |     30%     | [Season quest](https://youtu.be/EIicdmajxGo)                                                           |
| <!-- db_item-12811-0 -->                              |     10%     | [Caphras Journal](https://youtu.be/wSxSf9blmOg)                                                        |
| <!-- db_item-9691-0 --> (Food)                        |     10%     | Marketplace                                                                                            |
| <!-- db_item-791-0 --> (Elixir)                       |     20%     | Marketplace                                                                                            |
| <!-- db_item-735-0 --> (Perfume)                      |     20%     | Marketplace                                                                                            |
| <!-- db_item-16086-0 --> - <!-- db_item-16096-0 -->   |    10-15%   | Rewards                                                                                                |
| <!-- db_item-47006-0 -->                              |     50%     | Pearl Shop / Loyalties / Rewards                                                                       |
| <!-- db_item-18933-0 --> / <!-- db_item-300001-0 -->  |     50%     | Pearl Shop / Rewards                                                                                   |
| <!-- db_item-43704-0 -->                              |     10%     | Villa / Tent (Pearl Shop)                                                                              |
| <!-- db_item-110137-0 -->                             |     100%    | Game Anniversary                                                                                       |
| <!-- db_item-110124-0 -->                             |     100%    | Account B-day                                                                                          |
| <!-- db_item-768064-0 -->                             |     20%     | [Liana](https://grumpygreen.cricket/liana/#:~:text=Liana%E2%80%99s%20Weekly%20Quest%20Rewards)/ Events |
| <!-- db_skill-65034-0 --> / <!-- db_skill-65087-0 --> |  10% / 20%  | Guild                                                                                                  |
| <!-- db_skill-65120-0 -->                             |     40%     | Guild                                                                                                  |
| Donkey Gear Buff                                      | 3% / 5/ 10% | <!-- db_item-52622-0 -->                                                                               |
| Pets                                                  |  up to 50%  | Pearl Shop / Rewards                                                                                   |
| <!-- db_item-601259-0 -->                             |     30%     | Pearl Shop / Rewards                                                                                   |
| Server-wide Event Buff or Olvia                       |   50%-100%  | Event / Olvia                                                                                          |
| <!-- db_item-750589-0 -->                             |     20%     | Event                                                                                                  |
| <!-- db_item-750052-0 -->                             |      8%     | Event                                                                                                  |
| <!-- db_item-16295-0 -->                              |     10%     | Event                                                                                                  |
| <!-- db_item-750490-0 -->                             |     30%     | Event                                                                                                  |
| <!-- db_item-750397-0 -->                             |     10%     | Event                                                                                                  |


## 16. How to make money with processing?

### Where to start?

To get your foot into processing, you can start by crafting materials your workers brought in into materials used for other lifeskills. For example, you can process <!-- db_item-4001-0 --> into <!-- db_item-4051-0 --> to produce <!-- db_item-3719-0 --> or <!-- db_item-3703-0 -->. You could also process your own <!-- db_item-6656-0 --> for alchemy	or <!-- db_item-7105-0 --> / <!-- db_item-7205-0 --> for cooking (side note: try to avoid processing wheat dough for your own usage, as it's less valuable than other doughs). It's usually profitable to process materials brought in by workers but I still recommend checking the profit for yourself.

Note that if you process a lot, you will need to buy materials off the market. If you intend to process items for the market, you'll want to gain a basic understanding of which materials are in demand and what they go into, as shown below.

### The processing market

The processing market can be broadly divided into three groups based on what is generating the demand for materials.

| Demand from                  | Materials                                                                    | Info                                                              |
|------------------------------|------------------------------------------------------------------------------|-------------------------------------------------------------------|
| Crates / Alch stone upgrades | Plywood, ingots                                                              | High supply, high demand, stable profits                          |
| Cooking                      | Flour, dough, cheese, cream, butter                                          | High supply, high demand, stable profits                          |
| Workshops                    | Sturdy plywood, pure crystals, special gems, supreme hides, supreme feathers | Low supply and/or low demand, high but unstable profit potential  |

The first two groups are where you'll find consistent profit. Recipes from the third group can be much more profitable but are not beginner friendly at all. I'll go into more detail on those markets in [question 18](#18-what-about-that-3-bilh-recipe-on-bdolytics).


### The bdolytics market processing table

You can check processing profits and additional info with the [bdolytics processing table](/processing/market).

<img src="/guides/files/summer_processing_faq/processingmarket.png">

The table can be a bit overwhelming at first, so I'll explain the info it shows.
- **Name**: Name of the recipe
- **Favourite**: Lets you *bookmark* recipes by clicking on the heart icon
- **Silver/Hour**: Profit for one hour of processing when buying the materials and selling the product to the market (will adapt based on how you customized the recipe)
- **Market Price**: Market price of the product
- **Price Change**: *Current Market Price* compared to the *Market Price 7 days before*
- **Daily Volume**: Number of items sold per day, averaged over the past 7 days
- **Volume Change**: *Current Daily Volume* compared to the *Daily Volume 7 days before*
- **Experience**: Experience per craft. If two numbers are given, e.g. 200/500 it refers to the main result and rare proc
 
**Sort and Filter**
 
Additionally, you can **sort** the table by one or more columns and **search** for specific items through the search bar. For example, if you search for <!-- db_item-4651-0 -->, bdolytics will show the entry for <!-- db_item-4651-0 --> as well as all items it can be processed into, like <!-- db_item-4652-0 --> or <!-- db_item-4688-0 -->, and further recipes based on those items.

<img src="/guides/files/summer_processing_faq/processingmarket_search.png">

### Pitfalls

There are a few pitfalls you want to avoid when choosing items to process for the market:

**1. Picking a recipe with low daily volume.** 

While it can make sense to process low-volume items, those usually require special attention ([question 18](#18-what-about-that-3-bilh-recipe-on-bdolytics)). I recommend sticking to high-volume items such as materials for crates/alchemy stones and cooking. To make this easier, I first sort the processing table by *Daily Volume* before going through the *Silver/Hour* of the recipes.

**2. Not checking the input material availability.** 

<!-- profit_processing-6656 --> looks profitable on paper. Though <!-- db_item-6653-0 --> has a red mark next to it indicating that it's not available on the market. In this case, you can swap the <!-- db_item-6653-0 --> for <!-- db_item-6657-0 -->, which has a much higher supply. Though swapping input materials isn't possible for all recipes and some recipes will always have bottlenecks that you'll need to work around.

<img src="/guides/files/summer_processing_faq/purifiedwater.png">

<img src="/guides/files/summer_processing_faq/water_swap.png">

## 17. Do I have to combine processing with trading to make it profitable?

**Short answer**: No. 

It can make sense to pack processed materials into crates for certain playstyles, for example when you process a lot or have no <!-- db_item-601259-0 -->. Turning in a big stack of crates for billions of silver is satisfying but trading in itself is not a huge moneymaker. Realistically, trading is an optional step on top of processing, which gives a bit of extra profit and requires a fair bit of work.

**Long answer**: See my [post](/guides/tradingded) on this topic.

## 18. What about that 3 bil/H recipe on bdolytics?

<img src="/guides/files/summer_processing_faq/nichemarket2.png">

This is a screenshot from [the processing overview](/processing/market).

`Processing is 3 bil/H?? I have to get on that! Where's the catch?`

### Problems

**Problem #1: Limited demand** 

<!-- db_item-5865-0 --> `3 bil/H` looks pretty good, huh? But take a look at the daily volume. `220` units sold a day. In an hour of processing at 2k mastery, you could produce `25k` dawn fallen silk, which is enough to fully supply the market for almost two weeks. Therefore you should take the `3 bil/H` figure with a huge grain of salt. Effectively what it means is: any time spent on this recipe is very much worth it but this time is heavily limited.

**Problem #2: Limited supply**

<!-- db_item-4264-0 --> requires <!-- db_item-4263-0 --> / <!-- db_item-4262-0 --> / <!-- db_item-10151-0 -->, which are extremely hard to come by. Pre-orders fill slowly and there is no way to gather them efficiently. So while the recipe is profitable, the real question is whether the profit is worth the effort of getting the materials.

**Problem #3: Price fluctuations and razor-thin margins**

Since supply and/or demand for those items is so small, prices tend to fluctuate a lot. Unfortunately, a slight change in input material or product price can easily make these recipes go from `+3 bil/H` to `-3 bil/H`

### Solutions

Niche market processing means researching recipes on your own and dealing with the inherent difficulties of these recipes. Here are possible solutions to these problems:

**Solution to Problem #1** 

Expand your profit avenues by crafting and selling multiple items at once not to oversupply the market.

**Solution to Problem #2** 

You can address supply problems by pre-ordering items or crafting/gathering them yourself.

**Solution to Problem #3** 

Forming product chains can stabilize margins, for example turning self-made <!-- db_item-4076-0 --> into <!-- db_item-4053-0 -->. By using the <!-- db_item-4076-0 --> you get to save on the market tax compared to selling it. The tax savings can massively widen the margin and let you turn a profit where the recipe would otherwise not be profitable when buying the solvent.

I hope this outlines why niche market processing is a lot more difficult to get into than processing for the common markets.
To get into niche market processing, you'll be spending initial time on research and then time each day checking prices and listing/re-listing items.
The return on the time spent processing and managing your sales can far exceed the income on other activities. But I personally find it quite stressful.

That's why I like to look at niche market processing not as `profit per hour` but `profit per headache`. Make of that what you will :)

## 19. Help, I can't equip a processing stone on my season character D:

Season characters can't equip any gear that gives mastery, processing stones included. That means season characters cannot use mass processing. We can only hope that PA implements a solution for this in a future patch.

## 20. How do I increase my weight for processing?

| Source                                                                              | Weight                               |
|-------------------------------------------------------------------------------------|--------------------------------------|
| <!-- db_item-791-0 -->                                                              | 200 LT                               |
| <!-- db_item-9691-0 --> (2H) / <!-- db_item-9642-0 --> (10H)                        | 100 LT / 300 LT                      |
| Alchemy stone of life (spirit stones don't give weight)                             | 15 - 120 LT                          |
| <!-- db_lightstoneset-167-0 -->                                                     | 30 LT                                |
| 4x <!-- db_item-15665-0 --> or <!-- db_item-15662-0 -->  in mainhand and sub-weapon | 150 LT + 60 LT if using HAN crystals |
| <!-- db_item-18401-0 -->                                                            | up to 50 LT (tier 4) per pet         |
| Strength level                                                                      | up to 40 LT at lvl. 30               |
| Loyalty weight                                                                      | 50 LT, up to 4x                      |
| Pearl shop weight                                                                   | Up to 1050 LT                        |

## Resources

- [Lifeskill Discord](https://discord.gg/GUsNAYT)
- [Mastery gear cost sheet](https://docs.google.com/spreadsheets/d/1Me9wRktno6DDB4-of9tUx-SoaA-ezHK_w1BhwvXRrmA/edit?usp=sharing)
- [SE vs. manos clothes sheet](https://docs.google.com/spreadsheets/d/1Yv9-k7hShtmZ6oPZCmLu8C-eGJLgPkg7wvaIkJ_eres/edit#gid=268682067)
- [Bearist's Processing EXP Calculator](https://docs.google.com/spreadsheets/d/1KqP9lgTK0bDulLJ_JcILG4tn0iWrh5JkY1WHaitSxHo/edit?usp=sharing)

## Feedback is always welcome!

Thanks for reading :) 

If you have questions, corrections or suggestions, here are some ways in which you can reach out to me:
- Leave a comment below this guide.
- Leave an (anonymous) response on the [feedback form](https://forms.gle/ea2RZ6DvXAHQLnv76)
- Write a message to Summer#8727 or @ me in the [Lifeskill Discord](https://discord.gg/GUsNAYT).

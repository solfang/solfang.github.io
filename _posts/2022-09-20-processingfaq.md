---
layout: post
title: BDO - Processing FAQ - 20 Commonly Asked Questions Answered
description: The ultimate processing FAQ
published: false
tags: BDO
---

*Last updated: 23/10/2022*

Heya, I'm Summer and I made this post to help you out with any questions you may have about processing.
It's essentially a processing guide but the FAQ-style format is a bit nicer to `ctrl+f` in case you are looking for specific info.

Enjoy :)

## Preface - for very interested readers :) 

### What is processing?
Processing is about taking raw materials, for example produced by your worker empire, and refining them for use in further activities like trading, cooking and workshops. Processing is also fairly low effort and doesn't take a whole lot to get started. One of the coolest things about processing is that once you get further into it you can form elaborate recipe chains together with other lifeskills, like <!-- db_item-4006-0 --> -> <!-- db_item-4076-0 --> (alchemy) -> <!-- db_item-4053-0 --> (processing) -> <!-- db_item-16162-0 --> (workshops).

### The state of processing
Processing for profit has seen better times, partly because some of the activities it feeds into, like trading and workshops, have seen better times too. The moneymaking potential has noticeably fallen behind comparable lifskills like bartering and cooking. Nowadays, the main appeal of processing is being low effort and afk-able. 

On the bright side, leveling processing is fairly straight-forward ([question 14](#14-how-do-i-level-processing)). To earn money, you have a few recipes at your disposal ([question 16](#16-how-to-make-money-with-processing)). Processing markets these days are stable for the most part, which means I can share some for-profit recipes with you without negatively impacting the market. Beyond that, finding recipes has never been easier with tools like [bdolytics](https://bdolytics.com/en/EU/processing/market).

# Basics

## 1. How to process?
1. Open the processing window (L key)
2. Select a processing type 
3. Input the materials
4. Press 'Start' or 'Mass Process' (more on mass processing in [question 5](#5-what-does-processing-mastery-do))

<video width="640" height="360" muted autoplay controls>
    <source src="/files/processing_faq/howtoprocess.mp4" type="video/mp4">
</video>

After a few seconds, one of flour things will happen:
1) The craft succeeds
2) The message `Processing is not going as planned` appears → Your character will re-try the craft and no materials are lost.
3) The message `It is not working at all` appears → Either you input the wrong materials or something else went wrong, for example you're missing knowledge. No materials are lost when this happens. You can find the correct recipe to craft an item via the in-game crafting nodes (F2→Crafting notes) or [bdolytics](https://bdolytics.com/).
4) The message `Insufficient ingredients to continue processing` appears: You got the recipe right but don't have enough materials for a full craft.

<img width="450" src="/files/processing_faq/process_outcomes.jpg">

## 2. How can I stop processing from failing?

Even if you input the right materials, the message `Processing is not going as planned` can appear, which means your character has to re-try the craft.
The chance of this happening depends on your **processing success rate**, which is 70%* at base and goes up to 100%.

Here's how to increase your success rate:
- <!-- db_item-603044-0 --> / <!-- db_item-560024-0 --> (pearl shop costume): 3%  
- <!-- db_item-14026-0 --> 6%-40% (applied to the base success rate so actually 4%-28%)
- <!-- db_item-9691-0 --> 10% for 2 hours / <!-- db_item-9642-0 --> +15% for 10 hours
- <!-- db_item-791-0 --> 20% for 15 mins
- Alchemy stone: <!-- db_item-45280-0 --> or <!-- db_item-45302-0 --> 11% / <!-- db_item-45284-0 --> 14%
- [[Clang!Clang!]](https://bdolytics.com/db/lightstoneset/167) Lightstone set: 20% 
- <!-- db_item-735354-0 --> 5% each

You may have heard that the success rate *cannot* reach 100%. According to tests by the lifeskill community, we're almost certain that the success rate *can* reach 100%. However, some items seem to have a different success rate than indicated in the item description. This includes <!-- db_item-14026-0 --> and potentially <!-- db_item-791-0 --> and the [[Clang!Clang!]](https://bdolytics.com/db/lightstoneset/167) set. So to get 100% it helps to overstack success rate buffs by a few percent.

\*\*We used to think that the base success rate is 67% but a recent source shows it to be 70%. Unfortunately, testing success rate is extremely tedious so we have no definite way of telling which is correct.

# Mass Processing and Mastery

## 3. What is mass processing?
Mass processing lets you process **mutltiple batches of items** at once. On the flipside, that mass processing **takes 10x longer** than regular processing.
Example: processing *timber* into *planks*:
- Regular processing: 6 second craft time, 1 craft at a time
- Mass processing: 60 seconds craft time, 10+ crafts at a time

As you can see, mass processing has higher throughput than regular processing when processing more than 10 batches at once. Processing mastery increases the number of batches (see [question 5](#5-what-does-processing-mastery-do)).

You need a **processing stone** to get access to the 'Mass Process' button in the processing menu.

Note that mass processing only works with *Shaking, Grinding, Chopping, Drying, Filtering, Heating*.
Also, it only works on stackable items. For example, you can't mass dry fish because they take up 1 inventory slot each.

## 4. Can I mass-process black gems/caphras stones/party elixirs/blue elixirs/draughts/cron meals/imperial boxes?

Since those recipes require simple cooking, simple alchemy etc. mass processing does not work. But you can add specific items to the recipe that unlock alternative `10x` recipes:
- Caphras stones, black gems, concentrated magical black gems: <!-- db_item-4901-0 -->
- Party and blue elixirs, draughts: <!-- db_item-4986-0 --> (buy at materials vendors, requires skilled 1 processing)
- Cron meals: <!-- db_item-820015-0 --> (buy at cooking NPCs)
- Imperial cooking/alchemy boxes: <!-- db_item-8198-0 --> (buy at old moon managers. Using it requires having completed a [quest](https://youtu.be/x02GMajBFqU))

You can check these recipes in the in-game crafting notes (F2→Crafting notes in the top right or shift+LMB on any item in your inventory).

<img src="/files/processing_faq/caphras_recipe.png">

## 5. What does processing mastery do?

Processing mastery increases the number of crafts ('batches') you can perform at once through mass processing.
For example, with `1020 mastery` you can perform `90 crafts` at once, which at 10x higher craft time ends up being `90/10=9` times faster than regular processing.

Also note that at the lowest possible mastery bracket you can process 10 items at once, which has to the same throughput as regular processing. The more mastery you have, the more mass processing starts to outperform regular processing.

We conclude:

**If a recipe can be mass processed you should mass process it**

| Mastery | Batches | Mastery | Batches |
|:-------:|:-------:|:-------:|:-------:|
|    2    |    10   |   660   |    43   |
|    20   |    11   |   680   |    45   |
|    40   |    12   |   700   |    47   |
|    60   |    13   |   720   |    49   |
|    80   |    14   |   740   |    51   |
|   100   |    15   |   760   |    53   |
|   120   |    16   |   780   |    57   |
|   140   |    17   |   810   |    60   |
|   160   |    18   |   840   |    64   |
|   180   |    19   |   870   |    68   |
|   200   |    20   |   900   |    72   |
|   220   |    21   |   930   |    76   |
|   240   |    22   |   960   |    80   |
|   260   |    23   |   990   |    85   |
|   280   |    24   |   1020  |    90   |
|   300   |    25   |   1060  |    96   |
|   320   |    26   |   1100  |   112   |
|   340   |    27   |   1140  |   118   |
|   360   |    28   |   1180  |   124   |
|   380   |    29   |   1220  |   130   |
|   400   |    30   |   1260  |   137   |
|   420   |    31   |   1300  |   144   |
|   440   |    32   |   1350  |   154   |
|   460   |    33   |   1400  |   162   |
|   480   |    34   |   1450  |   170   |
|   500   |    35   |   1500  |   178   |
|   520   |    36   |   1550  |   186   |
|   540   |    37   |   1600  |   194   |
|   560   |    38   |   1650  |   203   |
|   580   |    39   |   1700  |   212   |
|   600   |    40   |   1800  |   222   |
|   620   |    41   |   1900  |   235   |
|   640   |    42   |   2000  |   250   |

*Table: mastery brackets and mass processing batches. Note that processing mastery brackets are not evenly spaced out at every 50 mastery like in other lifeskills but they vary from 20 to 100 mastery.*

## 6. How much processing mastery do I need for processing?

In other lifeskills, more mastery is always better. That only applies to processing to a certain point.
Having higher processing mastery lets you process items at a faster rate but weight is still a limiting factor. With high enough mastery your character will run out of weight before you check back on your processing. Increasing processing mastery beyond that point will let you be done faster but it won't increase the number of materials you can process in one afk session. On top of that, processing mastery scales fairly linear and there are no major breakpoints.

So here's my advice: 

**Get your processing mastery to a point where you will barely run out of weight whenever you check back on your processing (on whichever recipe you commonly process).**

# Recipes, Proc Rates and Process Times

## 7. How many items does a craft yield and what affects it?

### Craft yield

Most recipes yield **1-4 items** (2.5 on average). Exceptions to that tend to occur for high-tier recipes like T4 crafts as well as simple alchemy/processing, manufacturing etc., where recipes often yield 1 item per craft. 
The table below shows proc rates as well as other info for common processing recipes.
You can also check proc rates by going to a [specific recipe](https://bdolytics.com/processing/market/4651) on bdolytics and comparing the output materials to the number of crafts.

### What affects the proc rate?
**Proc rate is fixed and neither affected by mastery nor by whether you're regular or mass processing, with one exception: Getting maximum procs requires a certain processing level for some recipes.**
- *Shaking, Grinding, Chopping, Drying, Diltering, Heating* cap out at a certain processing level. For example, timber caps out at artisan 6 and ore at master 1. Once you're master 1, you'll have the maximum proc rate on 99% of recipes. A few recipes, like <!-- db_item-4269-0 --> require guru 1 for maximum procs.
- *Simple Alchemy, Simple Cooking, Imperial Cuisine, Imperial Alchemy, Guild Processing, Manufacturing* recipes have fixed rates and are not affected by processing level. You can let your beginner 1 alt do these recipes without worrying about losing out on procs :)

### Common processing recipes and basic info about them

| Recipe                                   | Example                     | Process Type   | Proc Range | Proc Avg |   Level Req.   |    EXP   |  Time  | Required Knowledge  |
|------------------------------------------|-----------------------------|----------------|:----------:|:--------:|:--------------:|:--------:|:------:|---------------------|
| Plank (T2)                               | Ash Plank                   | Chopping       |     1-4    |    2.5   |    Artisan 6   |  200/500 |  6/60  | -                   |
| Plywood (T3)                             | Ash Plywood                 | Chopping       |     1-4    |    2.5   | Professional 6 |    500   |  6/60  | Chopping: Beginner  |
| Sturdy Plywood (T4)                      | Sturdy Ash Plywood          | Heating        |     1-3    |     2    |  Professonal 1 |   1000   |  6/60  | Heating: Skilled    |
| Melted Shard (T2)                        | Melted Iron Shard           | Heating        |     1-4    |    2.5   |    Master 1    |  200/500 |  9/90* | -                   |
| Ingot (T3)                               | Iron Ingot, Vanadium Ingot  | Heating        |     1-4    |    2.5   |    Artisan 1   |    500   |  9/90* | Heating: Beginner   |
| Precious Ingot (T3)                      | Gold, Plat, Silver, Mythril | Heating        |     1-4    |    2.5   |    Artisan 1   |    800   | 9/80** | Heating: Beginner   |
| Mixed Ingot (T3)                         | Brass, Bronze, Steel        | Heating        |     1-4    |    2.5   |    Artisan 1   |    800   |  6/60  | Heating: Beginner   |
| Pure Crystal (T4)                        | Pure Iron Crystal           | Heating        |     1-3    |     2    |  Professonal 1 |   1000   |  6/60  | Heating: Skilled    |
| Precious Pure Crystal (T4)               | Gold, Plat, Silver, Mythril | Heating        |     1-3    |     2    |  Professonal 1 |   1500   |  6/60  | Heating: Skilled    |
| Hide (T2)                                | Tough Hide                  | Drying         |     1-4    |    2.5   |  Professonal 1 |  200/500 |  9/90  | -                   |
| Fine Hide (T3)                           | Fine Tough Hide             | Drying         |     1-4    |    2.5   |    Skilled 1   |    500   |  9/80  | Drying: Beginner    |
| Supreme Hide (T4)                        | Supreme Tough Hide          | Shaking        |     1-3    |     2    |  Apprentice 1  |   1000   |  9/80  |   Shaking: Skilled  |
| Feather (T2)                             | Lightweight Plume           | Filtering      |     1-4    |    2.5   |  Professonal 6 |  200/500 |  6/60  | -                   |
| Fine Feather (T3)                        | Fine Lightweight Plume      | Filtering      |     1-4    |    2.5   |    Skilled 6   |    500   |  9/80  | Filtering: Beginner |
| Supreme Feather (T4)                     | Supreme Lightweight Plume   | Shaking        |     1-3    |     2    |  Apprentice 1  |   1000   |  9/80  |   Shaking: Skilled  |
| Gem (T2)                                 | Ruby                        | Grinding       |     1-4    |    2.5   |    Artisan 1   | 500/1000 |  9/80  | -                   |
| Resplendent Gem (T3)                     | Resplendent Ruby            | Grinding       |     1-3    |     2    |    Skilled 1   |   1000   |  9/80  | Grinding: Beginner  |
| Special Gem (T4)                         | Blood Ruby                  | Shaking        |     1-2    |    1.5   |  Apprentice 1  |   2000   |  6/80  |   Shaking: Skilled  |
| Usable Scantling (T2)                    |                             | Chopping       |     1-4    |    2.5   |    Artisan 6   | 500/1000 |  6/60  | -                   |
| Standardized Timber Square (T3)          |                             | Chopping       |     1-3    |     2    | Professional 6 |   1000   |  6/60  | Chopping: Beginner  |
| Sturdy Timber Square (T4)                |                             | Heating        |     1-3    |     2    |    Artisan 1   |   1500   |  6/60  | Heating. Skilled    |
| Cream                                    |                             | Shaking        |     1-4    |    2.5   |    Skilled 1   |    150   |  6/60  | -                   |
| Butter                                   |                             | Shaking        |     1-4    |    2.5   |    Skilled 1   |    150   |  6/60  | -                   |
| Cheese                                   |                             | Drying         |     1-4    |    2.5   |    Skilled 1   |    300   |  9/60  | -                   |
| Flour                                    |                             | Grinding       |     1-4    |    2.5   | Professional 1 |    70    |  6/60  | -                   |
| Dough                                    |                             | Shaking        |     1-4    |    2.5   |    Skilled 1   |    150   |  6/60  | -                   |
| Thread/Yarn (T2)                         | Flax Thread                 | Heating        |     1-4    |    2.5   |    Artisan 1   |    500   |  6/60  | -                   |
| Fabric/Wool/Silk (T3)                    | Flax Fabric                 | Grinding       |     1-4    |    2.5   | Professional 1 |   1000   |  6/60  | -                   |
| Black Stone Powder (BSA)                 |                             | Grinding       |    40-60   |    50    |    Artisan 1   |    80    |  9/80  | -                   |
| Black Stone Powder (BSW)                 |                             | Grinding       |   60-100   |    80    |    Artisan 1   |    80    |  9/80  | -                   |
| Purified Water (from bag of muddy water) |                             | Filtering      |     1-4    |    2.5   |    Artisan 1   |    300   |  6/60  | -                   |
| Ship Repair Material                     |                             | Chopping       |     1-3    |     2    |    Artisan 1   |   1000   |  6/60  | -                   |
| Polished Stone                           |                             | Grinding       |     1-4    |    2.5   |    Artisan 1   |    500   |  6/60  | -                   |
| Cron Meal                                | Simple Cron Meal            | Simple Cooking |      1     |     1    |   Beginner 1   |     0    |    6   | -                   |
| Draught                                  | Verdure Draught             | Simple Alchemy |      1     |     1    |   Beginner 1   |     0    |    6   | -                   |
| Party Elixir                             | [Party] Defense Elixir      | Simple Alchemy |     1-2    |    1.8   |   Beginner 1   |     0    |    6   | -                   |
| Blue Elixir                              | Elixir of Steel Defense     | Simple Alchemy |      1     |     1    |   Beginner 1   |     0    |    6   | -                   |
| Black Gem                                |                             | Simple Alchemy |      1     |     1    |   Beginner 1   |     0    |    9   | -                   |
| Concentrated Magical Black Gem           |                             | Simple Alchemy |      1     |     1    |   Beginner 1   |     0    |    9   | -                   |
| Caphras Stone                            |                             | Simple Alchemy |      1     |     1    |   Beginner 1   |     0    |    6   | -                   |

**Notes about the table**

- **Level Req.**: Level required to gain the maximum proc rate
- **EXP**: Processing EXP. when two values are shown, the first one indicates the regular proc (e.g. ash plank: 200 EXP) and the second one the rare proc (e.g. ash plywood: 500 EXP)
- **Time**: regular processing / mass processing time in seconds

\* Zinc shards/ingots take 6/60 seconds. Ores are a huge mess in general.

\*\* Some 9s recipes seem to take 80 seconds when mass processed. Don't ask me why.

Source for the data: Daz' sheets, Bdocodex, bdolytics, in-game testing for the times

Since the table does not include all items, here's how to look up this info yourself:
1. Go to the [recipe page](https://cdn.discordapp.com/attachments/589711952234676224/704015738180075680/unknown.png) for that item on [bdocodex](https://bdocodex.com/) (This page is different from the item's page!): 
2. Look at the product groups at the bottom of the page. Each product product group represents a certain proc rate and is tied to a certain processing level.
The example below shows that you need [Art6+](https://cdn.discordapp.com/attachments/589711952234676224/704016039742013460/unknown.png) to get max procs on ash [ash plank processing](https://bdocodex.com/us/mrecipe/585/ ) .
(note: the last bracket seems to be missing in the current version of bdocodex)


## 8. How long can I afk process for?

It depends on the materials you're processing. This list shows the weight of common materials:

| Item                                 | Weight (LT) |
|--------------------------------------|-------------|
| Timber                               |         0.5 |
| Ore, Gems, Stone                     |         0.3 |
| Hide, Fabric, Feathers, Flour, Dough |         0.1 |
| Cheese, Cream, Butter                |        0.01 |

On bdolytics you can check how long you can process for before running out of weight:
1. Open the **settings** and enter your `weight`, `fairy feathery steps level`, `processing mastery`, `success rate` and whether you have the `processing costume` (more on the processing costume in [question 13](#12-do-i-need-the-pearl-shop-costume))
2. Go to the **recipe page** of the item you want to process.
3. Go to the **WEIGHT** tab.
4. Read the **Max. Crafts** and input it as the **craft quantity**.
5. Go back to the **INPUT&OUTPUT** tab and check the **time**.

<video width="640" height="360" muted autoplay controls>
    <source src="/files/processing_faq/howto_weight.mp4" type="video/mp4">
</video>

Some items are so light that you can process them for multiple hours or even overnight. 
Common recipes for **overnight processing** are <!-- profit_processing-9061-0 -->, <!-- profit_processing-9062-0 --> and <!-- profit_processing-9063-0 -->.

## 9. Why can't I chop plyoowd / heat pure crystals?

**You are missing knowledge.**

To chop planks into plywood (T3) you need `chopping: beginner`. To heat ingots into pure crystals (T4) you need `heating: skilled` and so on. You can get the knowledge entries through a quest chain. 

### Beginner Knowledge
- **Rewarded knowledge**: `Shaking: Beginner, Grinding: Beginner, Chopping: Beginner, Drying: Beginner, Filtering: Beginner, Heating: Beginner`
- **Starting quest**: [[Processing] Learning Higher Processing Skills](https://bdolytics.com/db/quest/2100/28)
- **Starting NPC**: [Ficy](https://bdolytics.com/en/EU/db/npc/50210/1) in Heidel
- **Requirements**: `apprentice 4 gathering` OR have completed [[Processing] In Search of Higher Processing Knowledge...](https://bdolytics.com/db/quest/2100/22)

[Video guide](https://www.youtube.com/watch?v=TvmMImSGl88)

You can find the quest via the in-game quest menu in the 'Suggested' tab (1) under `[Life][Certificate] Training Paradigm`. 
Make sure that you fulfill the quest requirements (2) and have all quests enabled (3).

<img width="1000" src="/files/processing_faq/questbeginner2.png">

### Skilled Knowledge
- **Rewarded knowledge**: `Shaking: Skilled, Grinding: Skilled, Chopping: Skilled, Drying: Skilled, Filtering: Skilled, Heating: Skilled`
- **Starting quest**: [[Processing] Excellent Magnate](https://bdolytics.com/db/quest/3208/1)
- **Starting NPC**: [Villager](https://bdolytics.com/db/npc/578/432) next to the blacksmith in Keplan (the waypoint button in the 'Suggested' tab will lead you there)
- **Requirements**: `Gathering skilled 10` AND `processing skilled 5` AND `all 6 pieces of beginner knowledge`

[Video guide](https://youtu.be/TvmMImSGl88?t=168)

You can find the quest via the in-game quest menu in the 'Suggested tab' under `[Life][Certificate] Skilled Paradim`. 
Make sure that you fulfill the quest requirements and have all quests enabled. 

## Help, I can't see the starting quest!
Possible Reasons:
- You don't have all quests enabled: see the image above
- You already have the knowledge: check the knowledge tab (H) -> `Life Skill` -> `Certificates`
- You have already accepted the quest: check your quest tab (O)

**If you are struggling with any of the quests despite reading through this section, feel free to message me on Discord at Summer#8727 and I'll walk you through the questline.**

# Gear

## 10. What gear do I need?
You technically don't need any gear to process. Though if you're processing on a larger scale, gear will massively speed up your processing.

Here are my *personal* gear recommendations, aimed at silver efficiency. Feel free to go for a different setup as you see fit.

### Beginner
- <!-- db_item-768088-18 -->
- <!-- db_item-705514-18 -->

### Intermediate
- <!-- db_item-768087-19 -->
- <!-- db_item-705514-19 --> / <!-- db_item-705516-19 --> (buy/pre-order on the market)
- any of  <!-- db_item-735372-0 --> / <!-- db_item-735361-0 -->  / <!-- db_item-735354-0 --> / <!-- db_item-735351-0 --> / <!-- db_item-735352-0 -->
- [[Clang!Clang!]](https://bdolytics.com/db/lightstoneset/167) Lightstone set: 20% success rate, 13% EXP, +25 processing mastery, +50 LT - including the lightstone effects

### Advanced
- <!-- db_item-768086-19 -->
- <!-- db_item-705516-19 --> / <!-- db_item-705518-19 --> (depending on your budget)
- <!-- db_item-735372-0 --> / <!-- db_item-735361-0 --> / <!-- db_item-735354-0 --> 
- [[Clang!Clang!]](https://bdolytics.com/db/lightstoneset/167) Lightstone set

### Which artifacts should I use?

In theory, the [[Clang!Clang!]](https://bdolytics.com/db/lightstoneset/167) set (20%) and seafood cron meal (10%) together with the base success rate (70%) should get you to 100%. But as the [[Clang!Clang!]](https://bdolytics.com/db/lightstoneset/167) set seems to give less success rate than indicated, you will need to add a verdure draught or success rate artifact to reach 100%.
In general, I would prioritize **mastery artifacts** (if it makes you hit a bracket) **>** **success rate** (if you don't have 100%) **>** **EXP**.

### Buy or enhance gear?

Lifeskill gear is usually cheaper to buy than to enhance yourself. You can check mastery gear enhance costs using [this sheet](https://docs.google.com/spreadsheets/d/1Me9wRktno6DDB4-of9tUx-SoaA-ezHK_w1BhwvXRrmA/edit?usp=sharing).

### How much mastery is enough?

Refer to [question 6](#6-how-much-processing-mastery-do-i-need-for-processing)

## 11. How can I get processing artifacts?
Processing artifacts drop from **imperial cooking turn-ins**, together with cooking artifacts. The chance to get an artifact is quite low (expect one maybe every 5-10 turn-ins) so it might take a while until you get the artifact you want.

You don't need to worry about having perfect artifacts. While working on getting processing artifacts, you can still run a lightstone set by using general-purpose artifacts like <!-- db_item-735351-0 -->  or <!-- db_item-735352-0 --> as placeholders. Once you get the processing artifacts, you can then extract the lightstones at a blacksmith with a <!-- db_item-757561-0 --> (bought at blacksmiths) and slot them into the new artifacts.

## 12. Do I need the pearl shop costume?

<!-- db_item-603044-0 --> and <!-- db_item-560024-0 --> can only be bought from the pearl shop, give 3% success rate and will let you **process from storage**. Note that you can only process from storage keepers, not storage containers.

When using a processing costume, the processed materials will go into your character's inventory. That means your character will only stop processing once you go overweight. 
Effectively, the processing costume lets you **stay afk for longer** (about 2 times longer as without the costume) before refreshing your processing. 
BUT the processing costume will not increase the afk time on recipes where the output materials are heavier than the input, like flour, dough, cream, butter and cheese. So the usefulness of the processing costume depends on what you are processing.

In the end, the processing costume is purely a **convenience item**.
It's up to you to decide whether the convenience of being able to stay afk for longer is worth spending pearls on.

## 13. Should I use mastery or silver embroidered clothes? 

**TLDR: Just use mastery clothes :)**

Mastery clothes and silver embroidered (SE) processing clothes have different benefits:
- **Mastery clothes** increase processing mastery, which boosts the number of batches you can process at once. This effectively lets you process at a faster rate.
- **SE clothes** give processing EXP and increase the processing success rate, which also lets you process at a faster rate. However, you won't see any benefit if you success rate is already at 100%. It's very easy to reach 100% success rate with mastery clothes, for example base (70%) + seafood cron meal (10%) + [[Clang!Clang!] Lightstone set](https://bdolytics.com/db/lightstoneset/167) (20%) + verdure draught (20%). In practice, the success rate is only useful when you don't have all buffs running.

<img width="600" src="/files/processing_faq/clothes_collage.png">

Therefore:
- **For profit:** Always use mastery clothes. The extra mastery brackets are more valuable than success rate 99% of the time.
- **For EXP:** You have to weigh the extra mastery brackets from mastery clothes against the extra success rate *and* the processing EXP from silver clothes. Depending on your mastery and grade of clothes available to you, either one can be better. You can do an exact comparison using [this sheet](https://docs.google.com/spreadsheets/d/1Yv9-k7hShtmZ6oPZCmLu8C-eGJLgPkg7wvaIkJ_eres/edit#gid=268682067). Though based on this chart, mastery clothes are preferred when going for EXP  for most setups.

# Leveling and Moneymaking

## 14. How do I level processing?

### Beginner to Professional

Based on what you have available, *heat* <!-- db_item-5802-0 --> into <!-- db_item-5852-0 --> or <!-- db_item-5804-0 --> into <!-- db_item-5854-0 -->


### Professional to Artisan
*Grind* <!-- db_item-5852-0 --> into <!-- db_item-5856-0 --> or <!-- db_item-5854-0 --> into <!-- db_item-5858-0 -->

### Artisan+ (all the way to guru 50)
There are a few ways to level processing on a larger scale. I want to highlight one specific method that is easy, effective and doesn't require selling materials on the market.
You may have already heard about it as the 'timber' or 'ship repair material' method. Here's how it works:

#### The method

1. Buy any cheap timber
2. Chop timber→planks→plywood→ship repair material (SRM) 
3. Sell the SRM to any NPC (vendors for 4k silver each)
 
#### Why it works

This method uses a 'feature' of mass processing. Chopping timber into planks has a 5% chance to directly proc plywood. Planks give `200` EXP and since they are a guaranteed product of the craft, you get this EXP every craft. Plywood gives `500` EXP when proced, which happens with a 5% chance. Here is where the 'feature' comes into play: when mass processing timber into planks and one of the crafts in the batch procs plywood, the game mistakenly adds the EXP from the plywood proc to the whole batch. That means you get the plank EXP of `200` and the plywood EXP of `500` for a total of `700` EXP for *all* crafts in the batch. The EXP bug doesn't happen when you don't proc any plywood but with a decent number of batches, getting no plywood proc is extremely unlikely. It's technically a bug but the developers haven't bothered fixing it for years. [Full explanation](https://cdn.discordapp.com/attachments/589711952234676224/1022215657368080464/unknown.png) by Goroshi.
 
This leads to the following effective EXP rates:
- Timber→Planks with the bug: `700` EXP
- Planks→Plywood: `500` EXP (yes, this gives less EXP than timber→planks)
- Plywood→SRM: `1000` EXP.
- *Partial chain* - Timber→Plywood: `660` EXP 
- *Full chain* - Timber→SRM: `728` EXP

The EXP bug is not limited to timber processing, it applies to all materials with a direct T3 proc on T1→T2 recipes, like ore, feathers and hide. It does *not* work for fabrics because the processing type switches from T1→T2 (heating) to T2→T3 (grinding), which means T1→T2 can not proc T3 materials.

#### How much money does it cost?

You can break even on the costs when buying timber below **540 silver**. 
But I wouldn't stress too much about the price. Timber bought below 1000 silver will lose you 'only' ~5-20 mil/H depending on your mastery.

#### Any downsides?

Timber is heavy, which leads to extremely **low afk times**. Even with a maxed out weight setup, you're looking at no more than 15 minutes of afk time.

#### Can I level processing and profit?

You sure can. Consider processing ore into ingots and timber into plywood, which will be slightly less EXP/H than the timber→SRM route but can be profitable depending on market prices. 

You can check [bdolytics](https://bdolytics.com/processing/market) for processing profits and EXP values.

Also here is a link to [Bearist's Processing EXP Calculator](https://docs.google.com/spreadsheets/d/1KqP9lgTK0bDulLJ_JcILG4tn0iWrh5JkY1WHaitSxHo/edit?usp=sharing).

## 15. Which EXP buffs can I run while leveling processing?

Here is a list of all buffs as of October 2022.
I would pick buffs based on which ones you have access to and which buffs are reasonable to use.

| Item                              | Life EXP  | Source                           |
|-----------------------------------|-----------|----------------------------------|
| Silver Embroidered Clothes        |   5%-40%  | Marketplace	                   |
| Professional Clothes (Costume)    |    10%    | [Equipment Tailoring Coupon](https://youtu.be/uoLLDrEMYjY)       |
| Mastery Accessories               | up to 75% | Marketplace	                   |
| Lightstone Combo (incl. stones)   | 13% / 20% / 25% | MP                         |
| Artifacts                         |   3%/5%   | Lifeskilling                     |
| Treant's Tear                     |    30%    | [Season quest](https://youtu.be/EIicdmajxGo)                     |
| Caphras Journal of Nature         |    10%    | [Caphras Journal](https://youtu.be/wSxSf9blmOg)                  |
| Seafood Cron Meal (Food)          |    10%    | Marketplace	                   |
| Verdure Draught (Elixir)          |    20%    | Marketplace	                   |
| Perfume of Swiftness (Perfume)    |    20%    | Marketplace	                   |
| GMs Blessing (1/2/3)              |   10-15%  | Rewards                          |
| Secret Book of Old Moon           |    50%    | Pearl Shop / Loyalties / Rewards |
| Sealed Book of Life / Life Scroll |    50%    | Pearl Shop / Rewards             |
| Villa Buff (Turning Gates)        |    10%    | Villa / Tent (Pearl Shop)        |
| Cake Buff (2h)                    |    100%   | Anniversary                      |
| Cake Buff (24h)                   |    100%   | Account B-day                    |
| Secret Book of Florin             |    20%    | [Liana](https://grumpygreen.cricket/liana/#:~:text=Liana%E2%80%99s%20Weekly%20Quest%20Rewards)/ Events                    |
| Guild Buff                        | 10% / 20% | Guild                            |
| Guru’s Touch (Guild Drill)        |    40%    | Guild                            |
| Donkey Gear Buff			         | 3% / 5/ 10% | Donkey Krogdalo Set              |
| Pets                              | up to 50% | Pearl Shop / Rewards             |
| Value Pack                        |    30%    | Pearl Shop / Rewards             |
| Server-wide Event Buff or Olvia   |  50%-100% | Event / Olvia                    |
| Giovan Grolin's Support Scroll    |    20%    | Event                            |
| Six Leaf Clover                   |     8%    | Event                            |
| Hearty Grilled Turkey             |    10%    | Event                            |
| Lara's Warm Black Tea             |    30%    | Event                            |
| Special Coconut Juice             |    10%    | Event                            |


## 16. How to make money with processing?

### Where to start?

It's usually not a bad idea to process materials your workers brought in. For example, you can process <!-- db_item-4001-0 --> into <!-- db_item-4051-0 --> to produce <!-- db_item-3719-0 --> or <!-- db_item-3703-0 -->. You could also process your own	<!-- db_item-6656-0 --> for alchemy	or <!-- db_item-7105-0 --> or <!-- db_item-7205-0 --> for cooking (side note: try to avoid processing wheat dough for your own usage, as it's less valuable than other doughs). It's usually profitable to process materials brought in by workers but I still recommend checking the profit on bdolytics. 

Note that if you process a lot, you will need to buy materials off the market. If you intend to process items for the market, you'll want to gain a basic understanding of which materials are in demand and what they go into, as shown below :)

### The processing market

The processing market can roughly be divided into three groups based on what creates demand for materials.

| Demand from                  | Materials                                                                    | Info                                                              |
|------------------------------|------------------------------------------------------------------------------|-------------------------------------------------------------------|
| Crates / Alch stone upgrades | Plywood, ingots                                                              | High supply, high demand, stable profits                          |
| Cooking                      | Flour, dough, cheese, cream, butter                                          | High supply, high demand, stable profits                          |
| Workshops                    | Sturdy plywood, pure crystals, special gems, supreme hides, supreme feathers | Low supply and/or low demand, high profit potential but unstable  |

The first two groups, crates/alch stone mats and cooking, are where you'll find consistent profit. The various materials for workshops (for example for ship, wagon and fishing rod workshops) can be much more profitable but are not beginner friendly at all. I'll go into more detail on those markets in [question 18](#18-what-about-that-3-bilh-recipe-on-bdolytics).


### The market processing table

You can check processing profits and additional info with the [bdolytics processing table](https://bdolytics.com/processing/market).

<img src="/files/processing_faq/processingmarket.png">

The table can be a bit overwhelming at first, so I'll explain the info it shows.
- **Name**: Name of the recipe
- **Favourite**: Lets you *bookmark* recipes by clicking on the heart icon
- **Silver/Hour**: Profit for one hour of processing when buying the materials and selling the product to the market (will adapt based on how you customized the recipe)
- **Market Price**: Market price of the product
- **Price Change**: `Current Market Price` compared to the `Market Price 7 days before` 
- **Daily Volume**: Number of items sold per day, averaged over the past 7 days
- **Volume Change**: `Current Daily Volume` compared to the `Daily Volume 7 days before`
- **Experience**: Experience per craft. If two numbers are given, e.g. 200/500 it refers to the main result and rare proc
 
Additionally, you can **sort** the table by one or more columns and **search** for specific items through the search bar. For example, if you search for <!-- db_item-4651-0 -->, bdolytics will show the entry for <!-- db_item-4651-0 --> as well as all items it can be processed into, like <!-- db_item-4652-0 --> and <!-- db_item-4688-0 -->

<img src="/files/processing_faq/processingmarket_search.png">

### Pitfalls

There are a few pitfalls when choosing recipes:

1. **Picking a recipe with low daily volume:** While it can make sense to process low-volume items, those usually require special attention (see [question 18](#18-what-about-that-3-bilh-recipe-on-bdolytics)). I recommend sticking to high-volume items such as materials for crates/alchemy stones and cooking. To make this easier, I first sort the processing table by `Daily Volume` before going through the `Silver/Hour` of the recipes.

2. **Not checking the input materials:** Processing <!-- db_item-6656-0 --> looks very profitable on paper. Though <!-- db_item-6653-0 --> has a red mark next to it indicating that it's not available on the market. In this case, you can swap the <!-- db_item-6653-0 --> for <!-- db_item-6657-0 -->, which has a much higher supply. Though swapping input materials isn't possible for all recipes and some recipes will always have bottlenecks.

<img src="/files/processing_faq/purifiedwater.png">

<img src="/files/processing_faq/water_swap.png">

## 17. Do I have to combine processing with trading to make it profitable?

**Short answer**: No. It can make sense to pack processed materials into crates for certain playstyles, for example when you process a lot or have no Value Pack. Turning in a big stack of crates for billions of silver is satisfying but trading in itself is not a huge moneymaker. Realistically, trading is an optional step on top of processing, which gives a bit of extra profit and requires a fair bit of work.

**Long answer**: See my [post](TODO: insert link to trading guide) on this topic.

## 18. What about that 3 bil/H recipe on bdolytics?

<img src="/files/processing_faq/nichemarket2.png">

This is a screenshot from <https://bdolytics.com/processing/market>.

`Processing is 3 bil/H?? I have to get on that! Where's the catch?`

Let's look at three examples:

1. <!-- profit_processing-5865 -->: `3 bil/H` looks pretty good, huh? But take a look at the daily volume. `220` units sold a day. In an hour of processing at 2k mastery, you could produce `25k` dawn fallen silk, which is enough to fully supply the market for almost two weeks. Therefore you should take the `3 bil/H` figure with a huge grain of salt. Effectively what it means is: any time spent on this recipe is very much worth it but this time is heavily limited. -> **Problem 1: Limited demand**

2. <!-- profit_processing-4264 -->: Mythril ingots, mythril shards and mythril ore are needed to craft pure mythril crystals and are extremely hard to come by. Pre-orders fill slowly and there is no way to gather them efficiently. To while the recipe is profitable, the real question is whether the profit is worth the effort of getting the materials.  -> **Problem 2: Limited supply**

3. Since supply and/or demand for those items is so small, prices tend to fluctuate a lot. Unfortunately, a slight change in input material or product price can easily make these recipes go from `+3 bil/H` to `-3 bil/H` -> **Problem 3: Price fluctuations and razor-thin margins**

Niche market processing means researching recipes on your own and dealing with the inherent difficulties of these recipes:
- Dealing with problem 1: Expand your profit avenues by crafting and selling multiple items at once not to oversupply the market.
- Dealing with problem 2: You can address supply problems by pre-ordering items or crafting/gathering them yourself.
- Dealing with problem 3: Forming product chains can be a good way to stabilize margins, for example turning metal solvent into pure crystals, where the saved tax on the metal solvent can be the difference between turning a profit on the craft or not.

I hope this outlines why niche market processing is a lot more difficult to get into than processing for the common markets.
To get into niche market processing, you'll be spending initial time on research and then time each day checking prices and listing/re-listing items.
The return on the time spent processing and managing your sales can far exceed what you could make through other activities. But I personally find it quite stressful.

That's why I like to look at niche market processing not as `profit per hour` but `profit per headache`. Make of that what you will :)

# Other

## 19. Help, I can't equip a processing stone on my season character D:

Season characters can't equip any gear that gives mastery, processing stones included. We can only hope that PA implements a solution for this in a future patch.

## 20. How do I increase my weight for processing?

- Pearl shop and loyalty weight
- <!-- db_item-9691-0 -->: 100 LT / <!-- db_item-9642-0 -->: 300 LT
- <!-- db_item-791-0 -->: 200 LT
- 4x <!-- db_item-15665-0 --> or <!-- db_item-15662-0 --> in mainhand and sub-weapon: 150 LT + 60 LT if you run HAN crystals
- [[Clang!Clang!] Lightstone set]: 30 LT
- Alchemy stone: varies (spirit stones don't give weight!)

## Feedback is always welcome!

Thanks for reading :) 

If you have questions, corrections or suggestions, here are some ways in which you can reach out to me:
- Leave a comment below this guide.
- Leave an (anonymous) response on the [feedback form](https://forms.gle/ea2RZ6DvXAHQLnv76) (If you want me to get back to you please leave contact information)
- Write a message to Summer#8727 or @ me in the Lifeskill Discord.

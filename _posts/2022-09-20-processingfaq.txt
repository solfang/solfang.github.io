---
layout: post
title: BDO - Processing Helpdesk: 15 questions, 6 answers
published: false
tags: BDO
---

# TODO: images and square brackets
# TODO: grammarly + proofread
Heya,
I made this post to answer commonly asked questions about processing
It's essentially a processing guide but this format is a bit nicer to `ctrl+f` in case you are looking for a specific topic.
Enjoy :)

## 1. how to process? (General)
- a. Open the processing window (L key)
- b. Select a processing type 
- c. Input the materials
- d. Press 'Start' or 'Mass Process' (more on mass processing in question 5)

<iframe width="420" height="315" src="/files/processing_faq/howtoprocess.mp4" frameborder="0" allowfullscreen></iframe>

After a few seconds, one of three things will happen:
- 1) The craft succeeds
- 2) The message `Processing is not going as planned.` appears → Your character will re-try the craft (no materials are lost).
- 3) The message `It is not working at all.` appears → You input the wrong items (no materials are lost). the correct recipe to craft an item can usually be found in the item description of the input items or the produced item.

[](/files/processing_faq/process_outcomes.jpg)

## 2. What does processing success rate do and how do I increase it? (General)

Processing success rate prevents crafts from 'missing' (`Processing is not going as planned.`). The success rate starts out at 67% and can be increased with the following items:
- <!-- db_item-603044-0 --> / <!-- db_item-560024-0 --> (pearl shop costume) 3%  
- <!-- db_item-14026-0 --> 6%-40% (applied to the base success rate so actually 4%-27%)
- <!-- db_item-9691-0 --> 10% for 2 hours / <!-- db_item-9642-0 --> +15% for 10 hours
- <!-- db_item-791-0 --> 20% for 15 mins
- Alchemy stone: <!-- db_item-45280-0 --> or <!-- db_item-45302-0 --> 11% / <!-- db_item-45284-0 --> 14%
- Clang! Clang! Lightstone set: 20%   (<!-- db_item-764016-0 --> <!-- db_item-764008-0 --> <!-- db_item-762006-0 --> <!-- db_item-766101-0 -->
- <!-- db_item-735354-0 --> 5% each



You may have heard that the success rate *can not* reach 100%. As far as we know, the success rate *can* reach 100% but certain items have different success rate than indicated in the item description. This potentially includes verdure draught and the Clang! Clang! set. So to get 100% it helps to overstack success rate buffs by a few percent.

## 3. What is mass processing? (Mastery)
Mass processing lets you process mutltiple items at once but it takes 10x longer thn regular processing. 
If you have a processing stone, the 'Mass Process' button will appear in the processing menu.
Mass processing only works on stackable items. For example, you can't mass heat weapons because they take up 1 inventory slot each.

## 4. What does processing mastery do? (Mastery)
Processing mastery increases the number of batches you can process through mass processing.
[chart]
For example, at [] mastery, mass processing takes 10x longer but also does 10 crafts at once, so it's the same speed as regular processing.
At [] mastery, you can do [] crafts at once, meaning you process [] times faster.
That also means you should mass process any recipe that allows mass procesing. There is no drawback to mass processing.

I sometimes see the question "How much processing mastery do I need?". 
Processing mastery lets you process items at a faster rate. But you are still limited by weight. That means it's sufficient to get enough mastery so that you barely run out of weight whenever you check back on your processing.


## 5. How many items does a craft yield and what affects it? (General)

**Processing proc rate*
- Lower-tier recipes usually yield **1-4 items** (2.5 on average). This includes: planks, plywood, polished stone, usable scantling,  melted shards, ingots, flour, dough, cheese.
- Higher-tier recipes tend ot have different proc rates. The following items proc **1-3 items** (2 on average): sturdy timber square, sturdy plywoods, resplendent gems, pure crystals, supreme hides.
- Everything that includes simples alchemy or simple cooking plays by its own rules.
- Simple alching green into blue elixirs (with <!-- db_item-4916-0 -->) procs 1. 

You can look up the proc rate of items on bdocodex: 
!TODO: can do this on bdolytics? -> recipe pages on bdolytics don't include required level from what it seems
- 1. go to the *recipe* page for that item on <https://bdocodex.com/> (This page is different from the item's page!): https://cdn.discordapp.com/attachments/589711952234676224/704015738180075680/unknown.png
- 2. Look at the product groups at the bottom of the page. Each product product group represents a certain proc rate and is tied to a certain processing level.
The example below shows that you need Art6+ to get max procs on ash plank processing: https://bdocodex.com/us/mrecipe/585/ -  https://cdn.discordapp.com/attachments/589711952234676224/704016039742013460/unknown.png

**What affects it**
There are a few aspect:
- The following processing types have fixed rates and are not affected by processing level:  Simple alchemy, simple cooking, imperial cuisine, imperial alchemy, guild processing, manufacturing.
- Other recipes *cap out at a certain processing level*. For example, timber caps out at artisan 6 and ore at master 1. You can look up the maximum required level on bdocodex on the same page where you would look up the proc rate. Once you're master 1, you'll have the maximum proc rate on 99% of items (one exception I know of are jade coral ingots which require guru 1).
- Proc rate is neither affected by mastery nor by whether you're regular or mass processing.

!TODO: insert the table

## 6. How long does it take to process materials? (General)

The process time depends on the item you're procecssing and of course on whether you use regular or mass processing, which takes 10x longer than regular processing.
I listed the processing times of common items in the table above. A processing time of 6/60 reads: regular processing takes 6 seconds, mass processing takes 60 seonds.
Most recipes take 6/60 or 9/90 seconds but there are some obscurities, like zinc, brass and bronze taking 80 seconds when mass processed. Don't ask me why :)
I've personally tested the processing times in the table as we don't have access to the processing times via the game files. 

## 7. What can I process? (General)

The main demand for processing products comes from three areas of the game:
- trading: plywoods and ingots
- cooking: flour, dough, cheese, cream, butter
- workshops (furniture, ships, fishing rods etc.): T4 plywood/metals/hides/feathers/gems

<https://bdolytics.com/processing/market> features a list of processing recipes.
If you just want to make money with processin,, check out question 14 where I got more into detail on moneymaking.

## 8. Why can't I chop plyoowd / heat pure crystals? (General)
You are missing knowledge.
For example, to chop planks into plywood you need `chopping: beginner` and to chop plywood into sturdy plywood you need `heating: skilled`
You can get the knowledge entries through a quest chain:

**Beginner knowledge**
Starting quest: [[Processing] Learning Higher Processing Skills](https://bdocodex.com/us/quest/2100/28/)
Starting NPC: Ficy in Heidel
Requirements: apprentice 4 gathering 
You can find the quest via the in-game quest menu in the 'Suggested tab' (1) under '[Life][Certificate] Training Paradigm'. 
*Note: Make sure that you fulfill the quest requirements (2) and have all quests enabled (3).*

[](/files/processing_faq/questbeginner2.png]

[Video guide](https://www.youtube.com/watch?v=TvmMImSGl88)

**Skilled knowledge**
Starting quest: [Processing] Excellent Magnate
Starting NPC: Villager next to the blacksmith in Keplan (the waypoint button in the quest menu will lead you there)
Requirements: Gathering skilled 10 AND processing skilled 5 AND all 6 pieces of beginner knowledge (shaking, drying, filtering, grinding, heating, chopping) 
You can find the quest via the in-game quest menu in the 'Suggested tab' (1) under '[Life][Certificate] Skilled Paradim'. 
*Note: Make sure that you fulfill the quest requirements (2) and have all quests enabled (3).*

[](/files/processing_faq/questskilled2.png]

[Video guide](https://youtu.be/TvmMImSGl88?t=168)

**If you struggled with these quests because you needed additional info not mentioned in the guide please let me know and I will update the guide**

## 9. What gear do I need for processing?
You technically don't need any gear to process. Gear can still massively help with processing through giving you the ability to mass process and increase mastery and success rate:

768088














<!-- db_item-560024-0 -->

- <!-- db_item-768088-0 --> / <!-- db_item-/768087-0 --> / <!-- db_item-768086-0 -->: mastery (there used to be one stone for each processing type but they merged them into a single stone)
- <!-- db_item-705514-0 --> / <!-- db_item-705516-0 --> / <!-- db_item-705518-0 -->: mastery / Silver embroidered clothes: processing EXP and success rate
- <!-- db_item-705503-0 --> / <!-- db_item-705507-0 --> / <!-- db_item-705511-0 -->: mastery
- Artifacts: <!-- db_item-735372-0 --> (10 mastery) / <!-- db_item-735354-0 --> (5% success rate) / <!-- db_item-735361-0 --> (5% EXP)
- Lightstones: [](/files/processing_faq/clangclang.png]

## 10. How do I get processing artifacts?
Hand in imperial cooking boxes. Processing artifacts drop at a low chance from imperial cooking turn-ins, together with cooking artifacts. So it might take a while until you get the artifact you want.
You don't need to worry about having perfect artifacts though. While working on your processing artifacts you can slot lightstones into general-purpose artifacts like <!-- db_item-735351-0 -->  or <!-- db_item-735352-0 -->  and extract the lightstones at a blacksmith once you get the processing artifacts.

## 11. Do I need the pearl shop costume (Venecil Dress/Karki Suit)?

<!-- db_item-603044-0 --> and <!-- db_item-560024-0 --> can only be bought from the pearl shop, gives 3% success rate and will let you process from storage. Note you can only process from storage keeper, not storage containers.

[](/files/processing_faq/venecilbutton.png]

The processed materials will go into your character's inventory. That means your character will only stop processing once you go overweight. 
Effectively, the processing costume lets you stay afk for longer before refreshing your processing. You stay afk longer for 2 times (planks, melted shards) to 4 times (timber, ingots) than without the costume.
But one some recipes where the output materials are heavier than the input,  like  four, dough, cream, butter and cheese, the processing costume will not increase your afk time!
In the end, the processing costume is purely a convenience item
It's up to you to decide whether the convenience of being able to stay afk for longer is worth spending pearls on.

# left off here

## 12. Should I use mastery or silver embroidered (SE) clothes? 

Mastery clothes and silver embroidered processing clothes have different beenfits:
- Mastery clothes increase processing mastery, which increases the number of batches you can process at once, effectively letting you process at a faster rate.
- SE clothes give procesing EXP and increase the processing success rate, which also lets you process at a faster rate. But only if your processing succes rate is not already 100%.
And this is the catch. It's very easy to reach 100% success rate with mastery clothes, for example base (67%) + seafood cron meal (10%) + 1 artifact (5%) + verdure draught (20%) will get you there.

[](/files/processing_faq/clothes_collage.png)

Therefore:
- **For profit:** Always use mastery clothes. The extra mastery brackets are more valuable than success rate 99% of the time.
- **For EXP:**: We have to weigh the extra mastery brackets against the extra sucess rate *and* the processing EXP from silver clothes. This of course depends on the grade of SE or mastery clothes you would consider. You can do an exact comparison using [this sheet](https://docs.google.com/spreadsheets/d/1Yv9-k7hShtmZ6oPZCmLu8C-eGJLgPkg7wvaIkJ_eres/edit#gid=268682067). As a rule of thumb, mastery clothes are preferred when going for EXP.

## 13. How to level processing?  (Leveling)

**Beginner to Professional:**
*Heat* <!-- db_item-5802-0 --> into <!-- db_item-5852-0 -->

**Professional to Artisan**
*Grind* <!-- db_item-5852-0 -->d into <!-- db_item-5856-0 -->

**Artisan+ (to guru 50 if you want)**
There are a few ways to level processing on a larger scale. One of these has becomethe 'go-to' method for leveling processing because it's effective, fairly straightforward and doesn't require selling materials on the market.
You may have already heard about it as the 'timber' or 'ship repair material' method. Here's how it works:

- **The method:** 
 1) Buy cheap timber (any timber works)
 2) Chop timber→planks→plywood→ship repair material (SRM) 
 3) Sell the SRM to any NPC (4k silver each).
- **Why this works:** This method uses a 'feature' (you may call it a bug :) ) of mass processing. Chopping timber into planks has a 5% chance to directly proc plywood. Planks give 200 EXP when proced, which is each craft. Plywood gives 500 EXP when proced, which happens with a 5% chance. Here is where the 'feature' comes into play: When mass processing timber into planks and one of the crafts in the batch procs one plywood (which is extremely common with a decent number of batches), the game mistakenly adds the EXP from the plywood proc to the whole batch. That means you get the plank EXP (200) and the plywood EXP (500) for a total of 700 EXP for all crafts in the batch. It's technically a bug but the developers haven't bothered fixing it for years. Full explanation by Goroshi: https://cdn.discordapp.com/attachments/589711952234676224/1022215657368080464/unknown.png
 
This leads to the following effective EXP rates:
- Timber→planks with the bug: 700 EXP (the same goes for ore→melted shards, raw hide→hide and plume→feather)
- Planks→plywood: 500 EXP (yes, this gives less than timber→planks)
- Plywood→SRM: 1000 EXP.
- Partial chain - Timber→plywood: 660 EXP 
- full chain - Timber→SRM: 728 EXP

The EXP bug is not specific to timber, it applies to all materials with a direct T3 proc on T1→T2 recipes, like ore, feathers and hide. It does *not* work for fabrics because the processing type switches from T1→T2 (heating) and T2→T3 (grinding) which means T1→T2 can not proc T3 materials.

- **How much money does it cost?** You can break even on the costs when buying timber below 540 silver. But I wouldn't stress too much about the price. Timber bought below 1000 silver will lose you 'only' ~5-20 mil/H depending on your mastery.
- **Can I level processing while profiting by processing?** You sure can. Consider processing ore into ingots and timber into plywood, which will be slightly less EXP/H than the timber→SRM route but can be profitable depending on market prices. You can check <https://bdolytics.com/processing/market> for processing profits.

For all your EXP needs, here is a link to [Bearist's Processing EXP Calculator](https://docs.google.com/spreadsheets/d/1KqP9lgTK0bDulLJ_JcILG4tn0iWrh5JkY1WHaitSxHo/edit?usp=sharing).

While we're at it, here's a list of EXP buffs:

!TODO: add list as table and if not possible as as screenshot + if screenshot note date created


## 14. How to make money with processing? (Moneymaking)
The two sub-markets with high demand are:
- crate materials: plywood and ingots
- cooking materials: flour/dough/cheese/cream/butter

You can check processing profits on [bdolytics](https://bdolytics.com/processing/market).

Those recipes give solid and stable profits. By far not all processing markets are like that. There is a set of sub-markets feeding into workshops, manos gear crafting that are characterized by rather low demand and fluctuating prices.

**Pro tip**: Do yourself a favor and sort by `Daily Volume`. If you sort by `Silver/Hour`, you'll get a best-off parade of all items with exceptional profit but extreme downsides/bottlenecks, which require special attention (see the next question).

## 15. What about that 3 bil/H recipe on bdolytics? (Moneymaking)

[nichemarket2.png]

This is a screenshot from <https://bdolytics.com/processing/market>.

`Processing is 3 bil/H?? I have to get on that! Where's the catch?`

Let's look at three examples:

1. Dawn Fallen Silk: 3 bil/H looks pretty good, huh? But take a look at the daily volume. 220 units sold a day. In an hour of processing at 2k mastery, you could produce 25k dawn fallen silk, which is enough to fully supply the market for almost two weeks. Therefore you should take the 3 bil/H figure with a huge grain of salt. Effectively what it means is: any time spent on this recipe is very much worth it but this time is heavily limited. -> **Problem 1: Limited demand**

2. Pure Mythril Crystal: Mythril ingots, shards or ore needed to craft pure mythril crystals are extremely hard to come by. Pre-orders fill slowly and there is no way to gather them efficiently. The question now becomes whether the profit is still worth it considering the effort it takes to get the materials.  -> **Problem 2: Limited supply**

3. A slight change in input material or product price can easily make these recipes go from +3 bil/H to -3 bil/H -> **Problem 3: Razor-thin margins**

Niche market processing means researching recipes on your own dealing with the inherent difficulties of these recipes:
- Dealing with problem 1: Expand your profit avenues by crafting and selling multiple items at once to not oversupply the market.
- Dealing with problem 2: You can address supply problems by pre-ordering items or crafting/gathering them yourself.
- Dealing with problem 3: Forming product chains can be a good way to stabilize margins, for example turning metal solvent into pure crystal, where the saved tax on the metal solvent can be difference between turning a profit on the craft or not.

I hope this outlines why niche market processing is completely different from processing for the common markets like crate materials or cooking.
To get into niche market processing you'll be spending initial time on research and then time each day checking prices and listing an re-listing items.
The time spent processing and managing your sales can far exceed what you could make through other activities. But I personally find it quite stressful.
That's why I tend to look at niche market processing not as `profit per hour` but `profit per headache`. Make of that what you will :)

## 16 Help, I can't equip a processing stone on my season character.

Tough luck. Can only hope that PA fixes this in the future.

## 17 How do I increase my weight for processing?

|Name   |Columns             |
|-------|--------------------|
|a      | b |
|c      | d |

<!-- db_item-9691-0 -->: 100 LT / <!-- db_item-9642-0 -->: 300 LT
<!-- db_item-791-0 -->: 200 LT
4x <!-- db_item-15665-0 --> or <!-- db_item-15662-0 --> in mainhand and sub-weapon: 150 LT + 60 LT if you run HAN crystals
Clang! Clang! lightstone set: 30 LT
Alchemy stone: varies (spirit stone doesn't give weight!)

!TODO: this as table
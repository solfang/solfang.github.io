---
layout: post
title: Black Desert Online - How to Calculate the True Value of Materials
published: true
type: writeup
tags: cooking
image: /files/cooktldr_2022/bdolytics_pen.png
excerpt: We'll take a deep dive into item valuation
post-date: 2021-02-06
updated-date: 2022-02-23
direct-link: 
---


Last updated: 23.02.2021

**Heads-up:**
Parts of this post are fairly outdated now, i.e. bdodae has been replaced by bdolytics and the price cap on many items such as milk, eggs and rough stone has been lifted which no longer makes them a bottleneck. There are only a handful of items left where it's useful to calculate the true value because the market price is not sufficient, e.g. Snake/scorp/lion meat, bracken, rainbow mushrooms, fruits for alchemy and traces. Having said that, the key concepts shown in this post are still very much valid (and I think true values are still one of the most interesting concepts  when it comes to profit min-maxing since they're the natural conclusion of other concepts like profit separation and valuing your time properly). Maybe I'll get around to updating this guide someday. Am working on other things like YouTube and more beginner-oriented written guides. So read at your own risk :)

This post is aimed at:  
Established players who are interested in item valuation, not so much at beginners. I'll try to break down the concepts in an easy-to-grasp manner but it definitely helps if you have thought about the topic of item valuation before.

In this post we'll do a deep dive into **material valuation in BDO**. Most of the worthwhile recipes in cooking/alchemy/processing involve rare materials. Therefore being able to calculate the true value of a material is an important skill and immensely helpful when comparing the profit of different recipes.

I'll first explain what a rare material is and then go over how to calculate its true value. Lastly, we'll take a look at popular recipes from cooking and processing, including cheese, advanced utensils and organic feed and see how to calculate the true value of rare materials in those recipes.

**TLDR:**  
Rare materials have a higher value than the market price due to scarcity. To compare different recipes which contain rare materials, it can be helpful to calculate the true value of those materials. The true value of a rare material is the profit created by using that material in a recipe. Calculate as: `Price of the rare material where the craft profit is 0.` If the time spent crafting is valuable to you, aim for X profit instead of 0, where X is the minimum acceptable profit based on the value of your time.

# 1) What is a rare material and why is knowing its true value important?

Rare materials are mats that can't be bought on the market in reasonable quantity. This often means that their value is higher than the market price. 
Some potential rare mats are:   
<img align="left" src="/files/bdo_truevalue/milk.png" height="20"> &thinsp; milk    
<img align="left" src="/files/bdo_truevalue/redmeat.png" height="20"> &thinsp; meat      
<img align="left" src="/files/bdo_truevalue/egg.png" height="20"> &thinsp; eggs     
<img align="left" src="/files/bdo_truevalue/coconut.png" height="20"> &thinsp; coconuts  
<img align="left" src="/files/bdo_truevalue/onion.png" height="20"> &thinsp; white onions

Knowing the true value of rare materials becomes important once you're comparing different recipes. There are two scenarios where calculating the true value can prove useful:

1) What is the most profit I can get out of this material?  
2) Which route of gathering->crafting different materials is the most profitable?

As you can see, calculating the true value only has merit when comparing different recipes which all have at least one rare material. For anything else (say comparing grain->flour to flour->dough processing profits), a simple side-by-side profit comparison will do.

Below, I'll go over an example for each of the two scenarios.

## Scenario 1: Best profit per material

<img src="/files/bdo_truevalue/coconuts_meme2.png">

We have collected a moderate number of coconuts from the Arehaza storage and want to know the most profitable way to liquidate them. Potential recipes are coconut cocktails, coconut dried fish and coconut pasta. After calculating the profit, coconut dried fish turns out to be the most profit per hour. But it also takes three coconuts per craft while the other two recipes take two. So with coconut fried fish we'd be making more silver per hour but couldn't cook for as long. Now it would be interesting to know which recipes create the most profit **per coconut** to get a measure that doesn't depend on the time it takes to cook the coconuts. 

By calculating the **true value** per coconut across the three recipes we then can decide which recipe is the most worthwhile. Of course, completely ignoring the time it takes to cook the coconuts would be disingenuous. But if we calculate the true value using the method outlined in section 3, the time spent cooking will also be factored in. The cool thing is that if we also wanted to consider other methods than cooking, like processing the coconuts into pine coated plywood, that wouldn't be hard to calculate either.

## Scenario 2: Comparing different activities

We have acquired two shiny new Manos tools: a Tet pickaxe and a Tet butchering knive. Now we want to know what is more profitable:

A) Gathering rough stone, turning them into advanced cooking utensils and selling the utensils.   
B) Gathering lion mean, cooking it into hamburgs which we sell to the market. 

A possible way to compare both options would be to gather rough stone for an hour and then count the time it takes to turn it into utensils. Say, 1 hour of gathering rough stone, 5 hours of workshop crafting (I'm glossing over the processing time to turn rough stone into polished stone here cause it's so short), total: 6 hours. Afterward, we'd gather lions for an hour and count the time it takes to cook the meat into hamburgs. Say, 1 hour of gathering and 1 hour of cooking, total: 2 hours. We could now divide the total silver made from the utensil crafts by the invested time (6 hours) and the profit from the hamburg crafts also by the invested time (2 hours) to calculate the average profit per hour on the two activities. The activity with the higher profit per hour would be better then, right? A huge flaw with this approach is that it values the gathering time the same as workshop and also the cooking time. Gathering is fully active while cooking is semi-afk and workshops are very low effort, basically passive. So in reality, the 6 hours running the utensil workshop should not weight as much as 1 hour of cooking. The gathering time is 1 hour in both cases so that one's a fair comparison.

One solution would be to factor out the time spent cooking and the workshop time by assigning a static cost to them. Say you'd expect to make 10 mil/h from cooking and 1 mil/h from workshops. We could now subtract the cost of cooking for 1 hour (10 mil) from the hamburg profit and the cost of running the utensil workshop for 6 hours (6 mil) from the utensil profit. Figuratively speaking, this is the same as paying an NPC at a flat rate to process the materials for us. So after paying the NPC we have a bunch of silver left (created by the cooking and workshop) that we would like to feed back into the gathering calculation. Assume that the gathering spreadsheet we use asks for a price on each material. So, which value do we input for the lion meat and rough stone? We take the profit generated by cooking / the utensil workshop that's left after (figuratively) paying the NPC to process the materials for us and divide it evenly among the lion meat / rough stone. For the lion meat that would be: (silver from cooking) / (number of lion meat used) = the **true value** of one lion meat. Similar for the rough stone. We can take this value and plug it back into the gathering profit calculation. Now we can cleanly compare the profit of one hour gathering lion meat to that of one hour gathering rough stone.

What I described above is the main idea behind calculating the true value of a material: Factor out any processing time, then divide the profit generated by the number of mats used.

It may sound a little complicated now but it's pretty easy once you got the hang of it: Calculate the true value of a rare material, then plug it into a gathering calculator and note down the profit/h. Do the same with a different rare material and compare the profit/h to that of the first material. Takes like 2 minutes with a cooking/alch/processing plus a gathering spreadsheet.

# 2) What is the true value of a rare material? 

I'll start this by presenting a hypothetical scenario.
Think of a rare item, for example milk or lion meat. The scenario is:
 
> Assume there was a vendor who sells the rare item and is only available to you.  
> The true value of a rare material is the maximum price you would pay for that item at the vendor.

Having an unlimited supply of the item would enable us to craft all of the recipes which take the rare item. But the profit on those recipes depends on how much we paid for the rare item at the vendor. Overpaying for the item would mean that those recipes may only turn a little profit or none at all. And at that point, we could just craft any other recipe and make more money. 

So in order to find out the maximum price we would pay for the item at the rare material vendor we need to find the price at which a recipe that uses the rare mat isn't any better or worse than another recipe that doesn't use the rare mat.  
This leads to a 'formal' definition for the true value of a rare item:

<p align=center>
<span style="color:#005cc2">
 <b>Definition:<br/>     
The true value of a rare mat is the value created by using the rare mat in a recipe compared to the next-best option that doesn't use the rare mat.</b>
</span>
 </p>

&nbsp;

**Example:**  
We want to figure out the true value of *lion meat* when cooked into jungle hamburgs. Also, say the recipe consumes 10k lion meat an hour.   
1) If we cooked hamburgs and **ignored the cost of lion meat**, we would make `210 mil/h`.  
2) The baseline for profit is cooking vinegar at `10 mil/h`, which one can buy all the mats for.  
3) The additional `210m - 10m = 200m` per hour were created by using the rare material *lion meat*. Therefore the true value of lion meat is `200m/10k = 20k`.  
Going back to the vendor scenario, `20k` is the maximum price we would pay for *lion meat* at the vendor. If we paid any more, there would be no point in cooking hamburgs over vinegar (cooking EXP aside). I'll explain the process of calculating the true value in the next section in more detail.

Keep in mind that this way of calculating the true value is only valid for mats that aren't available on the market in sufficient quantity. Items that can be bought on the market have their value capped at the market price.

Also note that the true value of rare mats is subjective. It depends on your mastery, the recipes you can make and market prices.

# 3) How to calculate the true value of a rare mat in a recipe?

The process of calculating the true value of an item can be broken down into four steps:

__Step 1)__ Think about which rare materials the recipe has, which one to solve for and what the next-best option to craft without rare mats is.  
__Step 2)__ If the recipe has more than one rare mat, find the true values of the rare mats you aren't solving for.  
__Step 3)__ Calculate the profit from crafting the next best recipe that doesn't take rare materials. In some cases, where the baseline profit is really low, it's also fine to set it to 0 and effectively skip this step.  
__Step 4)__ Calculate the profit from crafting the recipe that takes rare mats. In the calculation, price the rare mat so that profits of Step 3) and this step match. A simple way to do this is to first calculate the profit with the rare material valued at 0, subtract the profit from step 3) and then divide the resulting profit by the number of rare mats used.
See section 4 for examples.

In a more technical sense, we're solving an equation with multiple unknowns (the price of one or more rare mats and the time spent crafting) by factoring out all unknowns except the price of a chosen rare marerial and then solving for that price.

As you can see, we need to know two things beforehand:  
- The profit per hour of a 'filler' recipe, which doesn't take any rare mats and can always be crafted. This recipe determines the value of our time (be it cooking/alch/processing). If you have used the 'Time Cost' field in any of my sheets you should already be familiar with this concept.
- If the recipe requires multiple rare mats, we need to know or at least have a rough idea of the value of the other rare mats in the recipe.

# 4) Examples

I'll use my  [imperial sheet](http://bit.ly/ImperialSheet) and [Bdodae](https://www.bdodae.com/) to show how to apply the steps from above. 
Once you get familiar with the method, it'll be easy to apply it to other profit calculators as well.


## 4.1) Processing

### Processing Milk into Cheese

__Step 1)__ Which rare mats does cheese take? **Milk.**  

__Step 2)__ Nothing to do here since the only rare mat in the recipe is milk \:)  

__Step 3)__ Next-best recipe? We'll skip this step for now and assume the baseline profit is 0.

__Step 4)__ Profit created by processing milk into cheese?    
We assume cheese is priced at `5,950` silver. One milk turns into 2.5 cheese.   
The profit per craft is `2.5 * CheesePrice  * Tax = 2.5 * 5,950 * 0.845 = 12.5k`.   
Since we used one milk, the true value of milk when turned into cheese is `12.5k / 1 = 12.5k`.

I omitted **step 3)** for the sake of simplicity before. We'll now repeat the calculation with it included.    
<span style="color:#828282">Side note: I'll also assume that our drying mastery (for cheese) is the same as our shaking mastery (for dough). If it was not, we'd have to calculate on a per-hour basis instead of a per-craft basis to include the difference in processing speed. But who has time for that? :)  </span>

Step 3:   
Next-best recipe? Processing dough at `20 mil/h`. At 10k crafts per hour that's `20m / 10k = 2k` profit per craft.    
After subtracting the cost of the processing time from the profit, we're left with `12.5k - 2k = 10.5k` and therefore `10.5k` value per milk. Compare that to the `12.5k` before factoring in processing time. You'll notice that the new value is actually slightly below the maximum market price of milk (`10.5k` < `10.8k`). In this case, buying milk, processing it into cheese and selling the cheese would be a loss, given that we could process dough for `20 mil/h` instead. In other words, processing milk into cheese makes less than `20 mil/h` (our baseline profit) and you should ask yourself if that's a good use of milk. To be fair, the cheese price is rather low in this example.

<img src="/files/bdo_truevalue/notstonks.jpg" height="200">

Also, since processing cheese can be done overnight, the 'next-best' thing to do in that time would be a full afk activity like fishing or horse training. In general, the next-best thing doesn't have to involve crafting. Anything that gives an opportunity cost for the time spent crafting the rare material works.   
Full afk activities aren't all that profitable so the resulting opportunity cost of the time spent processing cheese is rather low.

Therefore, calculating the value of milk when turned into cheese as `2.5 * CheesePrice * Tax` is an alright approximation and saves you from the headache of valuing the processing time.

## 4.2) Workshops

### Rough Stone into Cooking Utensils

Here's the basic idea:

<img  src="/files/bdo_truevalue/utensils.png">

Now let's see how that fits into our 4-step process:

__Step 1)__ Rare mats? **Rough stone** and possibly **Logs**. At the time of writing this, usable scantling is readily available on the market so usable scantling or logs are not a rare material.

__Step 2)__ Can be skipped atm. If logs/scantling were not available on the market, we'd have to figure out a true value for logs. Since there's really not much worthwhile stuff to do with logs, it's a bit of a challenge. The easiest would be to treat logs and rough stone as the same material and then calculate the true value for both of them at the same time.

__Step 3)__ Can be skipped if you don't want to be 100% exact. If we wanted to though, we'd have to include the cost of running the workshop, for example by valuing the CP that went into renting it. We assume 40 utensils produced per day with a workshop that takes 4 CP (in O'draxxia). We also assume `200k` value per CP per day. That would result in a cost of `4 * 200k / 40 = 20k` silver per utensil. Basically negligible. Also technically, we'd have to include the time spent processing rough stone into polished stone. Again, this cost is negligible.

__Step 4)__ Using Bdodae, the profit from one utensil craft **without valuing rough stone** comes out to be `632,150`. The craft takes 80 rough stone, which leads to a value of `7,902` silver per rough stone as can be seen in the image below.  

<img  src="/files/bdo_truevalue/dae_utensil.png">

## 4.3) Cooking Imperials

### Milk into Milk Tea Master Boxes

__Step 1)__ Which rare mats does Milk Tea have? __Milk__. The next-best box that doesn't use rare mats? __Pickled Vegs__.  

__Step 2)__ Skiiip.  

__Step 3)__ the next-best recipe are pickled vegetable boxes at `~310k` profit per box.  

__Step 4)__ The goal is to find a price for milk at which the profits on the Milk Tea box and Pickled Vegs box match.    
Here's how that would look like on the imp sheet. I'm using 600 cooking mastery and 780 turn-in mastery in the clip. In the clip you'll see me gradually adjusting the price of milk until the profit of the two boxes match.

{% include youtube.html id="oMUZf7gtdYU" %}

In this example, milk has a true value of `14,900` when making milk tea boxes compared to Pickled Veg boxes.
It's important to take the milk-less alternative (Pickled Vegs here) into account because we could make `310k` per box on those without using any milk - this is an example where omitting step 3) would lead to a vast overestimation of the true value.

## 4.4) Market Cooking

### Milk into Organic Feed

__Step 1)__ Which rare mats does Organic Feed take? __Milk__ and __Meat__. Which one are we solving for? __Meat__ (this choice is up to you). Next best recipe that doesn't use rare mats? __Vinegar__ .

__Step 2)__ Now we need to figure out the true value of milk. There are several cooking recipes that milk can be used in and very few where it's the only rare ingredient, which makes things complicated. Luckily we have already calculated the true value of milk to be `12,500` when processed into cheese (without considering the cost of processing time). Alternatively, if milk tea was our most profitable imperial box, we could use the value/milk of `14.9k` we calculated earlier.

__Step 3)__ Our next best option is vinegar. For simplicity, I'll say the profit on vinegar is +-0 mil/h + byproducts. Since both vinegar and organic feed produce the same number of byproducts/h we'll ignore byproducts in the calculation and treat the profit of vinegar as 0 mil/h.

__Step 4)__ We calculate the profit on cooking Organic Feed using Bdodae, using the true value of milk from Step 2).
The goal is to find the price of meat at which the profit of Organic Feed and vinegar (0 mil/h here) match.
Here's how this would look like on Bdodae. I'm using 600 cooking mastery in the clip, which slightly increases the proc rate on Organic Feed (See the Mastery tab in the [imperial sheet](https://docs.google.com/spreadsheets/d/1D7mFcXYFm4BUS_MKxTvgBY2lXkGtwWqn2AW91ntUvzE/edit#gid=1519713712) for details on proc rates with mastery).
On 1k crafts, we used 5k meat and created a profit of 81.8m. This leads to a true value of `81.8m / 5k = 16.3k`.

{% include youtube.html id="NW7y-5O5Dqs" %}

If the profit on the alternative activity (vinegar) was more than 0 mil/h, we'd have to subtract the profit of 1428 vinegar crafts from the 81.8m before dividing by the number of meat (1428 is the total main+sub crafts for needed for the 81.8mil - displayed to the left of the cooking utensil cost). Say that vinegar was `10 mil/h` (or roughly 1.1k profit per craft at 9k crafts per hour). Now the true value of meat would be `(81.8m - 1428 * 1.1k) / 5k = 80.2mil / 5k = 16k`. The cost of time is not a huge deal here but for players who value their cooking time at `100+ mil/h` it's definitely something to keep in mind.

# 6) Recommendations
Finding recipes to base the true value of materials on is not always easy. That's partly because profitable recipes usually take multiple rare materials. Recipes that only take one rare mat are usually not profitable to sell due to low price caps (e.g. lean meat salad, boiled bird eggs).
Here's a list of potential recipes for calculating the true value of rare mats. Rare mats other than the one in question are in (brackets).
- **Meat**: Red Sauce, Organic Feed (dried fish), Cheese Gratin (onion)
- **Milk**: Cheese/Cream/Butter, White Sauce, Milk Tea, Sute Tea, Organic Feed (meat)
- **Eggs**: Dressing, Coconut Fried Fish (eggs, coconut)
- **Coconuts**: Coconut Cocktail, Coconut Pasta
- **Snake Meat**: Couscous
- **Scorpion Meat:** Teff Sandwich (snake meat)
- **Lion Meat**: Hamburgs, Valencia Meal (snake meat, scorpion meat)

Note that for instance, cheese in Cheese Gratin and White Sauce in Coconut Pasta don't count towards rare mats cause they can be bought on the market (at the time of writing this).

&nbsp;

## Closing Remarks

If you have questions or comments on this post, feel free to pm me on Discord at Summer#8727 :)

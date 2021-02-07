---
layout: post
title: Black Desert Online - How to Figure out the True Value of Materials
published: true
tags: BDO
---

Last updated: 07.02.2021

This post is aimed at:  
Established players who are interested in item valuation, not so much at beginners. I'll try to break down the concepts in an easy-to-grasp manner but it definitely helps if you have thought about the topic of item valuation before.

In this post we'll do a deep dive into into **material valuation in BDO**. Most of the worthwhile recipes in cooking/alchemy/processing involve rare materials. Therefore being able to calculate the true value of a material is an important skill and immensely helpful when comparing the profit of different recipes.

I'll first explain what a rare material and its value is, then go over how to calculate the true value. Lastly, we'll take a look at popular recipes from cooking and processing, including cheese, advanced utensils and organic feed and see how to calculate the true value of their rare materials.

# 1) What is a rare material? 

Rare materials are mats that can't be bought on the market in reasonable quantity. This often means that their value is higher than the market price. 
Some potential rare mats are:   
<img align="left" src="/files/bdo_truevalue/milk.png" height="20"> &thinsp; milk,  
<img align="left" src="/files/bdo_truevalue/redmeat.png" height="20"> &thinsp; meat,    
<img align="left" src="/files/bdo_truevalue/egg.png" height="20"> &thinsp; eggs,   
<img align="left" src="/files/bdo_truevalue/coconut.png" height="20"> &thinsp; coconuts  
<img align="left" src="/files/bdo_truevalue/onion.png" height="20"> &thinsp; white onions.


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
2) The baseline for profit is cooking vinegar at 10 mil/h, which one can buy all the mats for.  
3) The additional `210m - 10m = 200m` per hour were created by using the rare material *lion meat*. Therefore the true value of lion meat is `200m/10k = 20k`.  
Going back to the vendor scenario, 20k is the maximum price we would pay for *lion meat* at the vendor. If we paid any more, there would be no point in cooking hamburgs over vinegar (cooking EXP aside). I'll explain the process of calculating the true value in the next section in more detail.

Also note that the true value of rare mats is subjective. It depends on your mastery, the recipes you can make and market prices.

# 3) How to calculate the true value of a rare mat in a recipe?

The process of calculating the true value of an item can be broken down into four steps:

__Step 1)__ Think about which rare materials the recipe has, which one to solve for and what the next-best option to craft without rare mats is.  
__Step 2)__ If the recipe has more than one rare mat, find the true values of the rare mats you aren't solving for.  
__Step 3)__ Calculate the profit from crafting the next best recipe that doesn't take rare materials. In some cases, where the baseline profit is really low, it's also fine to set it to 0 and effectively skip this step.  
__Step 4)__ Calculate the profit from crafting the recipe that takes rare mats. In the calculation, price the rare mat so that profits of Step 1) and this step match. A simple way to do this is to calculate the profit with the rare material valued at 0, subtract the profit from step 3) and then divide the resulting profit by the number of rare mats used.
See [Section 4](#examples) for examples.

As you can see, we need to know two things beforehand:  
- The profit per hour of a 'filler' recipe, which doesn't take any rare mats and always be crafted. This recipe determines the value of our time (be it cooking/alch/processing). If you have used the 'Time Cost' field in any of my sheets you should already be familiar with this concept.
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
We assume cheese is priced at `5,950` silver. One milk turns into 2.5 cheese. The profit per craft is `2.5*5950(*0.845) = 12.5k` and since we used one milk that's also the true value of milk when turned into cheese.   
If we are using the cheese to cook, the tax can be omitted. Although, taxing the cheese even when using it to cook is also fine as long as it's also taxed (as an input cost) in the cooking calculation.

I omitted **step 3)** for the sake of simplicity before. We'll now repeat the calculation with it included.  
I'll also assume that our heating mastery (for cheese) is the same as our shaking mastery (for dough). If it was not, we'd have to calculate on a per-hour basis instead of a per-craft basis to be 100% exact. But who has time for that? :)  
Step 3): Next-best recipe? Processing dough at `20 mil/h` at 10k crafts per hour, which results in `20m / 10k = 2k` profit per craft.
This leaves `12.5k - 2k = 10.5k` profit per craft and therefore `10.5k` value per milk. You'll notice that the value is actually slightly below the market price for milk.  

In this case, buying milk, processing it into cheese and selling the cheese would be a loss, given that we could process dough for `20 mil/h` instead. In other words, processing milk into cheese makes less than `20 mil/h` (our baseline profit) and you should ask yourself if that's a good use of milk. To be fair, the cheese price is rather low in this example.

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
It's important to take the milk-less alternative (Pickled Vegs here) into account because we could make `310k` per box on those without using any milk - this is an example where omitting step 3) would lead to a vast overestimation of the true value. The difference in profit is created by using milk.

## 4.4) Market Cooking

### Milk into Organic Feed

__Step 1)__ Which rare mats does Organic Feed take? __Milk and Meat__. Which one are we solving for? __Meat__ (this choice is up to you). Next best recipe that doesn't use rare mats? __Vinegar__ .

__Step 2)__ Now we need to figure out the true value of milk. There are several cooking recipes that milk can be used in and very few where it's the only rare ingredient, which makes things complicated. Luckily we have already calculated the true value of milk to be `12,500` when processed into cheese (without considering the cost of processing time). Alternatively, if milk tea was our most profitable imperial box, we could use the value/milk of `14.9k` we calculated earlier.

__Step 3)__ Our next best option is vinegar. For simplicity, I'll say the profit on vinegar is +-0 mil/h + byproducts. Since both vinegar and organic feed produce the same number of byproducts/h we'll ignore byproducts in the calculation and treat the profit of vinegar as 0 mil/h.

__Step 4)__ We calculate the profit on cooking Organic Feed using Bdodae, using the true value of milk from Prep 2).
The goal is to find the price of milk at which Organic Feed and vinegar profit (0 mil/h here) match.
Here's how this would look like on Bdodae. I'm using 600 cooking mastery in the clip, which slightly increases the proc rate on Organic Feed (See the Mastery tab in the [imperial sheet](https://docs.google.com/spreadsheets/d/1D7mFcXYFm4BUS_MKxTvgBY2lXkGtwWqn2AW91ntUvzE/edit#gid=1519713712) for details on proc rates with mastery).
On 1k crafts, we used 5k meat and created a profit of 81.8m. This leads to a true value of `81.8m / 5k = 16.3k`.
If the profit on the alternative activity (vinegar) was more than 0 mil/h, we'd have to subtract the profit of 1428 vinegar crafts from the 81.8m before dividing by the number of meat (1428 is the total main+sub crafts for needed for the 81.8mil - displayed to the left of the cooking utensil cost).

{% include youtube.html id="NW7y-5O5Dqs" %}


# 6) Recommendations
Finding recipes to base the true value of materials on is not always easy. That's partly because profitable recipes usually take multiple rare materials. Recipes that only take one rare mat are usually not profitable to sell due to low price caps (e.g. lean meat salad, boiled bird eggs).
Here's a list of potential recipes for calculating the true value of rare mats. Rare mats other than the one in question are in (brackets).
- **Meat**: Red Sauce, Organic Feed (dried fish), Cheese Gratin (onion)
- **Milk**: Cheese/Cream/Butter, White Sauce, Milk Tea, Sute Tea, Organic Feed (meat)
- **Eggs**: Dressing, Coconut Fried Fish (eggs, coconut)
- **Coconuts**: Coconut Cocktail, Coconut Pasta
- **Snake Meat**: Couscous
- **Scorpion Meat:** Teff Sandwiches (snake meat)
- **Lion Meat**: Hamburgs, Valencia Meal (snake meat, scorpion meat)

Note that for instance, cheese in Cheese Gratin and White Sauce in Coconut Pasta don't count towards rare mats cause they can be bought on the market (at the time of writing this).

&nbsp;

## Closing Remarks

If you have questions or comments on this post, feel free to pm me on Discord at Summer#8727 :)

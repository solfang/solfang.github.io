---
layout: post
title: Black Desert Online - How to Figure out the True Value of Materials
published: true
tags: BDO
youtubeId: oMUZf7gtdYU
---

In this post we'll do a deep dive into into material valuation in BDO. Most of the worthwhile recipes in cooking/alchemy/processing involve rare materials so being able to calculate the true value of a material is an important skill in order to compare the profit of different recipes.

This post is aimed at established players who are interested in item valuation, not so much at beginners. I'll try to break down the concepts in an easy-to-grasp manner but it definitely helps if you have thought about the topic before.

# 1) What is a rare material? 

Rare materials are mats that can't be bought on the market in reasonable quantity. Therefore their value is higher than the market price. 
Examples for potential rare mats are: milk, meat, eggs, coconuts, white onions/garlic/pepper/hot pepper.

# 2) What is the true value of a rare material? 

I'll start this by presenting a hypothetical scenario:
Think of a rare item, for example milk or lion meat. The scenario:
 
> Assume there was a vendor who sells the rare item and is only available to you.  
> The true value of a rare material is the maximum price you would pay for that item at the vendor.





Having an unlimited supply of the item would enable you to craft all of the recipes which take the rare item. But the profit on those recipes depends on how much you paid for the rare item at the vendor. Overpaying for the item would mean that those recipes may only turn a little profit or none at all. And at that point, you could just craft any other recipe and make more money, no? 
So, in order to find out how much we would pay for the item at the rare material vendor we need to find the maximum price at which a recipe that uses the rare mat isn't any better or worse than another recipe that doesn't use the rare mat.
This leads to a 'formal' definition for the true value of a rare item:


**Definition**  
<span style="color:#242323">
**The true value of a rare mat is the value created by using the rare mat in a recipe...  
 compared to the next-best option that doesn't use the rare mat.**
</span>.

**Definition**  
<span style="color:#2e2e2e">
**The true value of a rare mat is the value created by using the rare mat in a recipe...  
 compared to the next-best option that doesn't use the rare mat.**
</span>.

**Definition**  
<span style="color:#474747">
**The true value of a rare mat is the value created by using the rare mat in a recipe...  
 compared to the next-best option that doesn't use the rare mat.**
</span>.


`The true value of a rare mat is the value created by using the rare mat in a recipe...`   
`... compared to the next-best option that doesn't use the rare mat.`  


**An example**  
We want to figure out the true value of *lion meat* when cooked into jungle hamburgs. Also, say the recipe consumes 10k lion meat an hour. 
1) If we cooked hamburgs and ignored the cost of lion meat, we would make 210 mil/h.  
2) Our baseline for profit is cooking vinegar at 10 mil/h, which one can buy all the mats for.  
3) The additional `210m - 10m = 200m` per hour were created by using the rare material lion meat. Therefore the true value of lion meat is `200mil/10k = 20k`.  
Going back to the vendor scenario, 20k is the maximum price we would pay for lion meat at the vendor. If we paid any more, there would be no point in cooking hamburgs over vinegar (EXP aside).

`Note`: The true value of rare mats is subjective. It depends on your mastery, the recipes you can make and market prices.
`Note`: This method translates into any lifeskill. Here's an example for gathering and finding the true value of rough stone when crafted into utensils:
<img  src="/files/bdo_truevalue/utensils.png">

# 3) How to calculate the true value of a rare mat in a recipe?

__Prep 1)__ Think about which rare materials the recipe has, which one to solve for and what the next-best option to cook without rare mats is.
__Prep 2)__ If the recipe has more than one rare mat, find the true values of the rare mats you aren't solving for.
__Step 1)__ Calculate the profit from cooking the next best recipe that doesn't take rare materials.
__Step 2)__ Calculate the profit from cooking the recipe that takes rare mats. In the calculation, price the rare mat so that profits of Step 1) and this step match. 
See below for examples.

# 4) What to do when a recipe has multiple rare mats?

Multiple variables are not helpful. We need to factor out all rare mats but the one in question. This requires knowing or at least having a rough idea about the true value of the other rare mats. More on this below.

# 5) Examples

I'll use my  [imperial sheet](http://bit.ly/ImperialSheet) and [Bdodae](https://www.bdodae.com/) to show how to apply the steps from above. 
Once you get familiar with the method, it'll be easy to apply it to other profit calculators/sheets as well.

**5.1) Imperials**
**Example: Milk Tea Boxes with the Imperial sheet**
__Prep 1)__ Which rare mats does Milk Tea have? __Milk__. Next-best box that doesn't use rare mats? __Pickled Vegs__.
__Prep 2)__ Nothing to do here since the only rare mat in the recipe is milk \:)
__Step 1)+2)__ The goal is to find a price for milk at which the profits on the Milk Tea box and Pickled Vegs box match.
Here's how it would look like on the imp sheet. I'm using 600 cooking mastery and 780 turn-in mastery in the clip.

{% include youtube.html id="oMUZf7gtdYU" %}

In this example, milk has a true value of 14900 when making milk tea boxes compared to Pickled Veg boxes.
It's important to take the milk-less alternative (Pickled Vegs here) into account because we could make 310k/box on those without using any milk. The difference in profit is created by using milk.

## 5.2) Market Cooking

**Example: Organic Feed with Bdodae**

__Prep 1)__ Which rare mats does Organic Feed take? __Milk and Meat__. Which one are we solving for? __Meat__ (this choice is up to you). Next best recipe that doesn't use rare mats? __Vinegar__ .

__Prep 2)__ Now we need to figure out the true value of milk. There are several recipes that milk can be used in and very few where it's the only rare ingredient, which makes things complicated. Luckily, milk can also turn a profit via processing it into cheese, cream or butter and selling it to the market. We choose cheese cause it has steady demand.
One milk turns into 2.5 cheese. Cheese is priced at 5950 silver. So the true value/milk for making cheese is `2.5*5950(*0.845) = 12.5k`. If we are using the cheese to cook, the tax can be omitted.
Alternatively, if turning in milk tea boxes was our most profitable option for imperials, we could use the value/milk of 14.9k we calculated earlier.

__Step 1)__ Our next best option is vinegar. For simplicity, I'll say the profit on vinegar is +-0 mil/h + byproducts. Since both vinegar and organic feed produce the same number of byproducts/h we'll ignore byproducts in the calculation and treat the profit of vinegar as 0 mil/h.

__Step 2)__ We calculate the profit on cooking Organic Feed using Bdodae, using the true value of milk from Prep 2).
The goal is to find the price of milk at which Organic Feed and vinegar profit (0 mil/h here) match.
Here's how this would look like on Bdodae. I'm using 600 cooking mastery in the clip, which slightly increases the proc rate on Organic Feed (see Mastery tab in the imperial sheet for details).
link3
On 1k crafts, we used 5k meat and created a profit of 81.8m. This leads to a true value of `81.8m / 5k = 16.3k`.
If the profit on the alternative activity (vinegar) was more than 0 mil/h, we'd have to subtract the profit of 1428 vinegar crafts from the 81.8m before dividing by the number of meat (1428 is the total main+sub crafts for needed for the 81.8mil - displayed to the left of the cooking utensil cost).

{% include youtube.html id="NW7y-5O5Dqs" %}

# 6) Recommendations
Finding recipes to base the true value of materials on is not always easy. That's partly because profitable recipes usually take multiple rare materials. Recipes that only take one rare mat are usually not profitable to sell due to low price caps (e.g. lean meat salad, boiled bird eggs).
Here's a list of potential recipes for calculating the true value of rare mats. Rare mats other than the one in question are in (brackets).
- __Meat__: Red Sauce, Organic Feed (dried fish), Cheese Gratin (onion)
- __Milk__: Cheese/Cream/Butter, White Sauce, Milk Tea, Sute Tea, Organic Feed (meat)
- __Eggs__: Dressing, Coconut Fried Fish (eggs, coconut)
- __Coconuts__: Coconut Cocktail, Coconut Pasta
Note that for instance, cheese in Cheese Gratin and White Sauce in Coconut Pasta don't count towards rare mats cause they can be bought on the market (at the time of writing this).


**Closing Remarks**

If you have questions or comments on this post, feel free to at/pm me on Discord at Summer#8727 :)

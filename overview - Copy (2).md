---
layout: default
title: Home
---

<style>
  .large-text {
    font-size: 36px; /* Adjust the font size as desired */
  }
  .post-count {
    font-size: 20px; /* Set the font size for the post count */
  }
</style>

<div class="icons-container">
  <div class="icon">
    <a href="/topics/cooking/">
      <img src="/files/icons/cooking2.png" alt="Cooking">
      <span class="large-text">Cooking</span> {% assign cooking_posts = site.posts | where: "tags", "cooking" %}
      {% if cooking_posts.size == 1 %}
        (<span class="post-count">1 post</span>)
      {% elsif cooking_posts.size > 1 %}
        (<span class="post-count">{{ cooking_posts.size }} posts</span>)
      {% endif %}
    </a>
  </div>
  <div class="icon">
    <a href="/topics/farming/">
      <img src="/files/icons/farming2.png" alt="Farming">
      <span class="large-text">Farming</span> {% assign farming_posts = site.posts | where: "tags", "farming" %}
      {% if farming_posts.size == 1 %}
        (<span class="post-count">1 post</span>)
      {% elsif farming_posts.size > 1 %}
        (<span class="post-count">{{ farming_posts.size }} posts</span>)
      {% endif %}
    </a>
  </div>
  <div class="icon">
    <a href="/topics/processing/">
      <img src="/files/icons/processing2.png" alt="Processing">
      <span class="large-text">Processing</span> {% assign processing_posts = site.posts | where: "tags", "processing" %}
      {% if processing_posts.size == 1 %}
        (<span class="post-count">1 post</span>)
      {% elsif processing_posts.size > 1 %}
        (<span class="post-count">{{ processing_posts.size }} posts</span>)
      {% endif %}
    </a>
  </div>
  <div class="icon">
    <a href="/topics/alchemy/">
      <img src="/files/icons/alchemy2.png" alt="Alchemy">
      <span class="large-text">Alchemy</span> {% assign alchemy_posts = site.posts | where: "tags", "alchemy" %}
      {% if alchemy_posts.size == 1 %}
        (<span class="post-count">1 post</span>)
      {% elsif alchemy_posts.size > 1 %}
        (<span class="post-count">{{ alchemy_posts.size }} posts</span>)
      {% endif %}
    </a>
  </div>
  <div class="icon">
    <a href="/topics/trading/">
      <img src="/files/icons/trading2.png" alt="Trading">
      <span class="large-text">Trading</span> {% assign trading_posts = site.posts | where: "tags", "trading" %}
      {% if trading_posts.size == 1 %}
        (<span class="post-count">1 post</span>)
      {% elsif trading_posts.size > 1 %}
        (<span class="post-count">{{ trading_posts.size }} posts</span>)
      {% endif %}
    </a>
  </div>
  <div class="icon">
    <a href="/topics/lifeskills/">
      <img src="/files/icons/all_lifeskills2.png" alt="All Lifeskills">
      <span class="large-text">All Lifeskills</span> {% assign lifeskills_posts = site.posts | where: "categories", "lifeskills" %}
      {% if lifeskills_posts.size == 1 %}
        (<span class="post-count">1 post</span>)
      {% elsif lifeskills_posts.size > 1 %}
        (<span class="post-count">{{ lifeskills_posts.size }} posts</span>)
      {% endif %}
    </a>
  </div>
  <div class="icon">
    <a href="/topics/misc/">
      <img src="/files/icons/misc.png" alt="Misc">
      <span class="large-text">Misc</span> {% assign misc_posts = site.posts | where: "tags", "misc" %}
      {% if misc_posts.size == 1 %}
        (<span class="post-count">1 post</span>)
      {% elsif misc_posts.size > 1 %}
        (<span class="post-count">{{ misc_posts.size }} posts</span>)
      {% endif %}
    </a>
  </div>
</div>



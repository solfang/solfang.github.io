---
layout: default
title: Home
---

<div class="posts">
  {% for post in site.posts %}
    {% if post.type contains 'blog' %}
      <article class="post">
        <h1><a href="{{ site.baseurl }}{{ post.url }}">{{ post.title }}</a></h1>
        {% if post.image %}
          <img height="180" src="{{ site.baseurl }}{{ post.image }}" alt="Preview Image">
        {% endif %}
        <div class="entry">
          {{ post.excerpt }}
        </div>
        <a href="{{ site.baseurl }}{{ post.url }}" class="read-more">Read More</a>
      </article>
    {% endif %}
  {% endfor %}
</div>


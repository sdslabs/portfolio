---
layout: home
title: Portfolio
---
<div class="pure-g">
  <!-- Begin Load Content from md -->
  {% for post in site.posts %}
    <div class="pure-u-1-3 block">
      <img src="{{ post.images.first }}">
      <a href="{{ post.url }}">{{ post.title }}</a>
      <div class="excerpt">
      	{{ post.excerpt }}
      </div>
      <div class="full-content">
      	{{ post.content }}
      </div>
    </div>
  {% endfor %}
</div>
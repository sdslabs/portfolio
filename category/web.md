---
layout: home
title: Web Development | SDSLabs
---
<ul>
  {% for post in site.categories.web %}
    <li>
      <img src="{{ post.images.first }}">
      <a href="{{ post.url }}">{{ post.title }}</a>
      <div class="excerpt">
      	{{ post.excerpt }}
      </div>
      <div class="full-content">
      	{{ post.content }}
      </div>
    </li>
  {% endfor %}
</ul>
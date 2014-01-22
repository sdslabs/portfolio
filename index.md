---
layout: home
title: Portfolio
---
<div class="pure-g">
  <!-- Begin Load Content from md -->
  {% for post in site.posts %}
    <div class="pure-u-1-3 block" style="background-image:url('{{ post.images.first }}')">
      <div class="hover">
        <h6>
         <a href="{{ post.url }}">{{ post.title }}</a>
        </h6>
        <div class="excerpt">
        	{{ post.excerpt }} <a href="{{ post.url }}">Read More</a>
        </div>
      </div>
      <div class="full-content">
      	{{ post.content }}
      </div>
    </div>
  {% endfor %}
</div>
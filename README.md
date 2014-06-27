SDSLabs Portfolio
=================

This is a portfolio of various products made by SDSLabs. It will also include
our achievements (such as contests won) and some details about the members involved
in the specific item.

#Installation
- Make sure you have ruby installed, if not install the latest from [rvm](https://rvm.io)
- Now run `gem install jekyll`. Wait, _gem is slow_ :D
- Simply execute `jekyll serve` and app will be hosted at address which jekyll will tell you.

#Development
This repository uses Jekyll for storing data as markdown items that are easily
edited/created. All items will be created as posts in jekyll, and will be available
at a custom URL of their own as well.

The Home Page will include all the stories in thumbnails, optionally filtered by
type of story.

A direct post page (muzi.html) will only show the direct popup with nothing in bg.

This repo uses a lot of jekyll magic to make sure everything is clean and simple.
Instead of relying on JavaScript to filter stuff when you click on something, we
instead use HTML pages (easily created by Jekyll) over an AJAX request
made by checking for clicks using JQuery and History.js to decide what content to show.
History.js takes care of making URLs, and the back button work for us.

#Adding a new Tile
To add a new post, just create a new post under `_posts/YEAR-MONTH-DATE-TITLE.md`
format. Make sure you add the images, excerpt (shown on hover), and a single word
(lowercase) category. A small title and layout: post is also needed.

Before committing run the script for generating thumbnails as well (#todo)

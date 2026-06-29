# web-scraper
Trying to iterate through a website and storing all the links for posts and sorting them on a timeline.

https://scp-wiki.wikidot.com/groups-of-interest
I started reading SCP wiki stories recently, and would like to understand where things fall on the timeline more.
Stories are currently sorted by alphabet not timeline. The problem is likely that stories don't always connect to each other or have a specific period.

So I want to make a script that iterates through the GOI (groups of interest) page, goes to each GOI's individual page, and then catalogs each story's info on that page.
Info I want: characters involved, date if possible, location if possible, tags, the story's link (just the page link itself), if it is part of a series

I have no previous knowledge of webscraping, but am familiar with html and some frontend so I can at least understand what I'm looking at, so we'll see how this goes.

___________________________________________
Before looking anything up:

Example page: https://scp-wiki.wikidot.com/a-betamax-suicide-note
Inspected the page, saw that the story was contained in simple paragraphs. This is a fairly normal design for pages, so I can use this as a standard.

 - There were some pages that had different organization styles or images, like the Odysseus stories, but I'll look at those later.

View in editor

This page had it's story all stored in <div id="page-content">, with the page's title in <div id="page-title">, both of which are children of <div id="main-content">.
The on-page title and series info were stored right before the paragraphs under a <div style="text-align: center;">, and looks like this: 
[
<div class="meta-title">
<p>A Betamax Suicide Note</p>
</div>
<div class="pseudocrumbs">
<p><a href="/monarchs-and-maestros">Monarchs and Maestros Hub</a> » A Betamax Suicide Note</p>
</div>
<p><span style="white-space: pre-wrap;"> </span></p>
<h2 id="toc0"><span>April 4th, 2005</span></h2>
<h3 id="toc1"><span><a href="/locations-of-interest#backdoor-soho">Backdoor SoHo</a></span></h3>
</div>
]
This included the title under class meta-title, a link to the series page under class pseudocrumbs, the date of the story under id toc0, and a location under id toc1.
Then I want characters and tags.
Characters will be difficult, as they have multiple names and can be referred to differently throughout a story, so I'll ignore that until I can get everything else.
Tags are under page-content in <div class="page-tags">, and then listed out in a span as hrefs.

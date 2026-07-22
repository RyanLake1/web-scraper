Goals and issues:
I can see why a timeline feature is not implemented. Many stories do not have related dates.
I really want to be able to make a timeline though, one where you can enter a character, a location or an scp and see what occurred where at what point in time, 
or at least being able to read them in a chronological order.

So that is the main goal and issue.

Side-note:
Personal Log of █████ "Iceberg" ████
The block character █, (U+2588) in unicode, is used to mark 'redacted' information consistently in the website, so I need to be able to manage it when it shows up, and maybe even store it.

ALL DATE FORMATS FOUND:
2029/09/13
2019
04/08/2004
April 4th, 2005

Pattern ideas:
[
If a page has multiple dates, always use the oldest one.
    Good at handling: 
        - dated flashbacks
        - happen over multiple dated days
    Issues with: 
        - if a page has something saying that something is planned for a future date and includes that date
    Is this a problem?
        - if something is recorded over multiple years, like a yearly report on a location
            No, because the last date is when we theoretically view the document, which helps our immersion
]

Date problem (example):
This story happens at a determined time: https://scp-wiki.wikidot.com/dr-kondraki-cut-up-while-thinking
It happens "About a month after the bullet and the butterflies"
"the bullet and the butterflies" links to https://scp-wiki.wikidot.com/scp-7408, which details later in the page the time of that specific event.
So, if I want to see the timeline of stories involving Dr. Kondraki, I would first want to see scp-7408, then the other.

The positive is that "all" pages that involve Dr. Kondraki have a tag called "doctor-kondraki", which itself links to a page that has all pages on it with that particular tag.
https://scp-wiki.wikidot.com/system:page-tags/tag/doctor-kondraki#pages
The site has 110 pages with this tag currently.

I am going to use the "doctor-kondraki" tag as an example from now on, where my end goal is to organize all things with this tag in chronological order using a program.
To do this, I may try to manually arrange them and look for patterns I can use.

https://scp-wiki.wikidot.com/deadgirlwalking
This story takes place in 2019, with no additional information. However, a majority of the page content focuses on flashbacks to 2016, again with no month/day.

The year '2019' is stored in id="toc1". id="toc0" stores the page title.
Following [id="toc" + #] stores more years corresponding to information under it.

Potentially getting all id="toc#" and then applying some sort of filter could get all dates.


Here I have written out future resources, organizational ideas, goals, etc.
Should move most of README.md to this and have a quick user guide instead.

Current tables:
[('story_to_date',), ('story_to_tag',), ('story_to_location',), ('story_to_character',), ('scp_stories',), ('story_to_scp',)]

_________________________________________________________________________________________________________________________________________________________
Locations are already managed at:
https://scp-wiki.wikidot.com/locations-of-interest
This page has locations listed, as well as all articles that have tagged themselves with that location as well.
This reduces my need to be heavily involved in storing location data, as it would be relatively easy to just pull from this page.

https://scp-wiki.wikidot.com/locations-complete-list - Semi-comprehensive list of locations of interest
This page actually has all locations I think. Each location has related articles/pages under it.

Other semicomprehensive lists:
https://scp-wiki.wikidot.com/goi-complete-list - Groups of interest
Has the major groups of interest shown at [https://scp-wiki.wikidot.com/groups-of-interest] under GOI with hub pages, where the group name is a link to its hub page.

https://scp-wiki.wikidot.com/poi-complete-list - Persons of interest
Has people listed in alphabet ranges A-F, G-L, M-S, T-Z, as well as unnnamed under '#', and others under numerical '#'

https://scp-wiki.wikidot.com/facilities-complete-list - Foundation Facilities

There are about 15 comprehensive lists at the bottom of locations-complete-list, but these 4 complete lists are the most applicable to my project.
_________________________________________________________________________________________________________________________________________________________

https://scp-wiki.wikidot.com/hub-hub - The hub of hubs.

Important hubs (for this project potentially) and description

https://scp-wiki.wikidot.com/series-archive - Series Hub
Contains a list of all series (and their hub links) as well as series-related tags.

https://scp-wiki.wikidot.com/scp-calendar - SCP Calendar
Contains a lists of all SCPs, date and time published, and author that published it.

https://scp-wiki.wikidot.com/tale-calendar - Tale Calendar
Contains a lists of all Tales, date and time published, and author that published it.


Sister site: https://wanderers-library.wikidot.com/
_________________________________________________________________________________________________________________________________________________________


Goals and issues:
I can see why a timeline feature is not implemented. Many stories do not have related dates.
I really want to be able to make a timeline though, one where you can enter a character, a location or an scp and see what occurred where at what point in time, 
or at least being able to read them in a chronological order.

So that is the main goal and issue.

Look at implementingTimeline.md in the doctor_kondraki folder for my thought process.


Potential tables:
# Character table (persons of interest):
# cursor.execute("""
#     CREATE TABLE poi (
#         id INTEGER PRIMARY KEY,
#         name TEXT
#     )
# """)
# how do I handle nicknames?
# there are also characters that are referred to with the same name sometimes
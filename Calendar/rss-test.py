#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""
RSS-feed parser for multiple rss-feeds from URLs.
In development for the E-Paper-Calendar software.
Stability: Stable

Copyright by aceisace
"""

import feedparser
import random
from PIL import ImageFont

path = '/home/pi/E-Paper-Master/Calendar/'

font = font = ImageFont.truetype(path+'OpenSans-Semibold.ttf', 28)

rss_feeds=[
    "http://feeds.bbci.co.uk/news/world/rss.xml#"
    ] # From which URLs should the RSS-feeds be fetched?

"""
More feeds can be added in the following way:
rss_feeds=[ 'feed1', 'feed2', ... ]
"""

rss_feed = [] #Create an empty list which will be used later

for feeds in rss_feeds: # Use all urls to get rss-feeds.
    text = feedparser.parse(feeds) # Read them with feedparser
    print('\n',text['feed']['title']) # Display the title of the RSS-feed URL
    print('________________________')
    for posts in text.entries: # Get RSS-feed title (usually a shorter description)
        rss_feed.append(posts.title) # Add the titles to the rss_feed list

"""
By now, all titles from all given RSS-feed URLs should have been added to the
rss_feed list. Let's check this by printing the list:

"""
#print(rss_feed) #May be very long

"""
Since this list is too long, we'd have to chop the list to the correct length,
in this case, the number of 'lines' below the Calendar.
The problem is that since RSS-feed don't get updated too frequently (unlike the
calendar), it would lead to displaying the same rss-feeds over and over.
To tackle this issue, we're going to 'shuffle' the list:
"""

random.shuffle(rss_feed) # Shuffle the list
del rss_feed[7:] # Delete all elements after the 7th element


"""
Since not all RSS-feed titles  can fit in a single line, it's required to
split the titles 'correctly' into smaller lines. The max. of each 'RSS-line'
is set 1100px. The full display width is 1200px, so with 'padding' of 50px on
either side, it is 1100px. Below is the fuction that handles this.
"""

def multiline_text(text, max_width):
    lines = []
    if font.getsize(text)[0] <= max_width:
        lines.append(text)
    else:
        words = text.split(' ')
        i = 0
        while i < len(words):
            line = ''
            while i < len(words) and font.getsize(line + words[i])[0] <= max_width:
                line = line + words[i] + " "
                i += 1
            if not line:
                line = words[i]
                i += 1
            lines.append(line)
    return lines

"""
Let's split the titles into lines then.
"""

news = [] # create an empty list first

for items in rss_feed:
    lines = multiline_text(items, 1100)
    news.append(lines)
    
"""
If you print the 'news' list, you'll see nested lists (lists within lists). This
is problematic when trying to display the lines on the E-Paper, so we'll remove
the nesting.
"""

news = [j for i in news for j in i] # Remove nesting

"""
Now that we have a 'flat' list, we can print it out once again:
"""

#print(news) #prints entire news list.

# Alternatively, print the index of each line along with the title:

for i in range(len(news)):
    print('Line number:',i,'Title:',news[i])

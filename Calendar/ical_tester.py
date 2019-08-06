from datetime import datetime, date, timedelta
from ics import Calendar, Event
from urllib.request import urlopen

# Your iCalendar URL
url = ""

# Display events which are max. 60 days in the future. Can be changed.
events_max_range = "60"

# Parsing the iCalendar and fixing errors related to actions
decode = str(urlopen(url).read().decode())
fix_e_1 = decode.replace('BEGIN:VALARM\r\nACTION:NONE','BEGIN:VALARM\r\nACTION:DISPLAY\r\nDESCRIPTION:')            
fix_e_2 = fix_e_1.replace('BEGIN:VALARM\r\nACTION:EMAIL','BEGIN:VALARM\r\nACTION:DISPLAY\r\nDESCRIPTION:')

"""Remove  the '#' sign before the print to display the iCalendar"""
#print(fix_e_2)
ical = Calendar(fix_e_2)

# Function for time-span using the 'events_max_range'
today = date.today()
time_span = today + timedelta(days=int(events_max_range))

# create a list
upcoming = []

# Filter events and add them to the 'upcoming list'
for events in ical.events:
    if today <= events.begin.date() <= time_span:
        upcoming.append({'date':events.begin.format('YYYY MM DD'), 'event':events.name})

# Sort events
def takeDate(elem):
    return elem['date']

upcoming.sort(key=takeDate)

# Remove events if there are more than 7. Max. 7 events can be displayed
del upcoming[7:]

# Print upcoming events as they would appear on the E-Paper
print('Upcoming events:')
print(upcoming)

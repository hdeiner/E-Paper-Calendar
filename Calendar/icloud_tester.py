from datetime import datetime, date, timedelta
from pyicloud import PyiCloudService
from urllib.request import urlopen


# Authenticate
#api = PyiCloudService('howard.deiner@deinersoft.com', 'hJd040686$')
# I have stored my password in my keyring, using username=howard.deiner@deinersoft.com
# the password for the keyring is hJd040686$
api = PyiCloudService('howard.deiner@deinersoft.com')

# Two Factor Authentication
#if api.requires_2sa:
#    import click
#    print("Two-step authentication required. Your trusted devices are:")

#    devices = api.trusted_devices
#    for i, device in enumerate(devices):
#        print("  %s: %s" % (i, device.get('deviceName',
#            "SMS to %s" % device.get('phoneNumber'))))

#    device = click.prompt('Which device would you like to use?', default=0)
#    device = devices[device]
#    if not api.send_verification_code(device):
#        print("Failed to send verification code")
#        sys.exit(1)

#    code = click.prompt('Please enter validation code')
#    if not api.validate_verification_code(device, code):
#        print("Failed to verify verification code")
#        sys.exit(1)

# Devices
print(api.devices[0])

# Calendar
from_dt = datetime(2019,7,1)
to_dt = datetime(2019,7,31)
print(api.calendar.events(from_dt, to_dt))

# Your iCalendar URL
#url = ""

# Display events which are max. 60 days in the future. Can be changed.
#events_max_range = "60"

# Parsing the iCalendar and fixing errors related to actions
#decode = str(urlopen(url).read().decode())
#fix_e_1 = decode.replace('BEGIN:VALARM\r\nACTION:NONE','BEGIN:VALARM\r\nACTION:DISPLAY\r\nDESCRIPTION:')            
#fix_e_2 = fix_e_1.replace('BEGIN:VALARM\r\nACTION:EMAIL','BEGIN:VALARM\r\nACTION:DISPLAY\r\nDESCRIPTION:')

"""Remove  the '#' sign before the print to display the iCalendar"""
#print(fix_e_2)
#ical = Calendar(fix_e_2)

# Function for time-span using the 'events_max_range'
#today = date.today()
#time_span = today + timedelta(days=int(events_max_range))

# create a list
#upcoming = []

# Filter events and add them to the 'upcoming list'
#for events in ical.events:
#    if today <= events.begin.date() <= time_span:
#        upcoming.append({'date':events.begin.format('YYYY MM DD'), 'event':events.name})

# Sort events
#def takeDate(elem):
#    return elem['date']

#upcoming.sort(key=takeDate)

# Remove events if there are more than 7. Max. 7 events can be displayed
#del upcoming[7:]

# Print upcoming events as they would appear on the E-Paper
#print('Upcoming events:')
#print(upcoming)

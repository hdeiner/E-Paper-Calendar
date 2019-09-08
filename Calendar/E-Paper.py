#!/usr/bin/python3
# -*- coding: utf-8 -*-
# For 9.7 inch E-Paper
"""
E-Paper Software (main script) for the 3-colour and 2-Colour E-Paper display
A full and detailed breakdown for this code can be found in the wiki.
If you have any questions, feel free to open an issue at Github.

Copyright by aceisace, Howard Deiner
"""
from __future__ import print_function
import glob, os
from settings import *
from icon_positions_locations import *
import random
import gc
from PIL import Image, ImageDraw, ImageFont, ImageOps
import calendar,  pyowm
from ics import Calendar, Event
from datetime import datetime, date, timedelta
from time import sleep
try:
    from urllib.request import urlopen
except Exception as e:
    print('It seems the network is offline :(', file=sys.stdout)
    pass

try:
    import feedparser
except ImportError:
    print("Please install feedparser with: sudo pip3 install feedparser", file=sys.stdout)
    print("and", file=sys.stdout)
    print("pip3 install feedparser", file=sys.stdout)

import sys 
import logging
from write_text_to_epaper import *
from draw_time_to_epaper import *

if NO_EPAPER:
    path = '/home/howarddeiner/IdeaProjects/E-Paper-Calendar/Calendar/'
else:
    path = '/home/pi/E-Paper-Calendar/Calendar/'

os.chdir(path)

logging.basicConfig(format='%(asctime)s %(levelname)s:%(message)s', filename='E-Paper.log',level=logging.INFO)

# from https://github.com/JuiceBoxZero/LowBatteryShutdown/blob/master/LowBatteryShutdown.py

#import RPi.GPIO as GPIO

# This is going to let us use the BCM pin numbers.  The number on JuiceBox
# Zero is labeled
# according to BCM.  See https://pinout.xyz/ for more details on pinouts.

#GPIO.setmode(GPIO.BCM)

# This is where you would change the GPIO from pin 16 to 25, if you needed
# to do so on the
# Juice Box Zero board itself. Default is GPIO 16. In order to change the
# hardware, you would
# need to cut the GPIO 16 trace on the board and make a solder bridge over
# GPIO 25.
# See http://www.blog.juiceboxzero.com/ for more details.
#shutdown_pin = 16  # defines pin 16 as the pin we're watching
#GPIO.setup(shutdown_pin, GPIO.IN, pull_up_down = GPIO.PUD_DOWN)
#print("JuiceboxZero GPIO monitor pin set", file=sys.stdout)

def shutdown_callback_function( shutdown_pin ):

    # uncomment the following line to have the Pi tell you that the pin is
    # HIGH and that the callback function has been entered. This is mostly
    # useful for debugging.
    print("the low battery pin is HIGH now, shutting down.", file=sys.stdout)

    os.system("sudo shutdown -h now")

# This is the magic line that adds pin 16 so it is always being watched.

#GPIO.add_event_detect(shutdown_pin, GPIO.RISING, callback=shutdown_callback_function)
#print("JuiceboxZero shutdown callback added", file=sys.stdout)

# Now, back to the E-Paper-Calendar...

owm = pyowm.OWM(api_key)

EPD_WIDTH = 1200
EPD_HEIGHT = 825
font_normal = ImageFont.truetype(path+'OpenSans-Semibold.ttf', 28)
font_calendar = ImageFont.truetype(path+'OpenSans-Bold.ttf', 28)
font_big = ImageFont.truetype(path+'OpenSans-Semibold.ttf', 52)
font_time = ImageFont.truetype(path+'digital-7.ttf', 120)
clock_face = "other/analog-clock-without-hands-clipart-6.jpg"
im_open = Image.open

def main():
    while True:
        for i in range(1):
            time = datetime.now()
            """At the following hours (midnight, midday and 6 pm), perform
               a calibration of the display's colours"""
            #if hour is 0 or hour is 12 or hour is 18:
            #    logging.info('DAILY CALIBRATION OF DISPLAY COLORS')
            #    image.paste(im_open(opath+'white.jpeg'))

            image_name = 'current-image'
            logging.info('STARTING NEW LOOP')

            """Create a blank white page first"""
            image = Image.new('L', (EPD_WIDTH, EPD_HEIGHT), 255)
            if (DRAW_BORDER):
                ImageDraw.Draw(image).line([(2,2),(EPD_WIDTH-4,2),(EPD_WIDTH-4,EPD_HEIGHT-2),(2,EPD_HEIGHT-2),(2,2)], fill=0, width=2)

            # Put in the time
            write_text_to_epaper(500, 130, str(time.strftime("%I:%M %p")), (4,70), image, font_time, 'center', logging)
            #draw_time_to_epaper(325, 550, 490, time, image, clock_face, logging)
            draw_time_to_epaper(625, 550, 190, time, image, clock_face, logging)

            """Add the icon with the current month's name"""
            #image.paste(im_open(mpath+str(time.strftime("%B")+'.jpeg')), monthplace)
            # write_text_fontbig_center(500, 70, str(time.strftime("%B  %Y")), (0, 100))
            write_text_to_epaper(500, 70, str(time.strftime("%B  %Y")), (4, 250), image, font_big, 'center', logging)

            """Add weekday-icons (Mon, Tue...) and draw a circle on the
            current weekday"""
            logging.debug('week_starts_on='+week_starts_on)
            if (week_starts_on is "Monday"):
                logging.debug('code for week_starts_on Monday')
                calendar.setfirstweekday(calendar.MONDAY)
                #image.paste(weekmon, weekplace)
                #image.paste(weekday, weekdaysmon[(time.strftime("%a"))], weekday)
                write_text_to_epaper(65, 50, "Mon", (20, 350), image, font_calendar, 'center', logging)
                write_text_to_epaper(65, 50, "Tue", (85, 350), image, font_calendar, 'center', logging)
                write_text_to_epaper(65, 50, "Wed", (150, 350), image, font_calendar, 'center', logging)
                write_text_to_epaper(65, 50, "Thu", (215, 350), image, font_calendar, 'center', logging)
                write_text_to_epaper(65, 50, "Fri", (280, 350), image, font_calendar, 'center', logging)
                write_text_to_epaper(65, 50, "Sat", (345, 350), image, font_calendar, 'center', logging)
                write_text_to_epaper(65, 50, "Sun", (410, 350), image, font_calendar, 'center', logging)

            """For those whose week starts on Sunday, change accordingly"""
            if (week_starts_on is "Sunday"):
                logging.debug('code for week_starts_on Sunday')
                calendar.setfirstweekday(calendar.SUNDAY)
                #image.paste(weeksun, weekplace)
                #image.paste(weekday, weekdayssun[(time.strftime("%a"))], weekday)
                write_text_to_epaper(65, 50, "Sun", (20, 350), image, font_calendar, 'center', logging)
                write_text_to_epaper(65, 50, "Mon", (85, 350), image, font_calendar, 'center', logging)
                write_text_to_epaper(65, 50, "Tue", (150, 350), image, font_calendar, 'center', logging)
                write_text_to_epaper(65, 50, "Wed", (215, 350), image, font_calendar, 'center', logging)
                write_text_to_epaper(65, 50, "Thu", (280, 350), image, font_calendar, 'center', logging)
                write_text_to_epaper(65, 50, "Fri", (345, 350), image, font_calendar, 'center', logging)
                write_text_to_epaper(65, 50, "Sat", (410, 350), image, font_calendar, 'center', logging)

            """Using the built-in calendar function, add icons for each
               number of the month (1,2,3,...28,29,30)"""
            cal = calendar.monthcalendar(time.year, time.month)
            #print(cal) #-uncomment for debugging with incorrect dates

            for i in cal[0]:
                #image.paste(im_open(dpath+str(i)+'.jpeg'), positions['a'+str(cal[0].index(i)+1)])
                write_text_to_epaper(65, 50, str(i), (20+65*(i-1), 400), image, font_calendar, 'center', logging)
            for i in cal[1]:
                #image.paste(im_open(dpath+str(i)+'.jpeg'), positions['b'+str(cal[1].index(i)+1)])
                write_text_to_epaper(65, 50, str(i), (20+65*(i-cal[1][0]), 450), image, font_calendar, 'center', logging)
            for i in cal[2]:
                #image.paste(im_open(dpath+str(i)+'.jpeg'), positions['c'+str(cal[2].index(i)+1)])
                write_text_to_epaper(65, 50, str(i), (20+65*(i-cal[2][0]), 500), image, font_calendar, 'center', logging)
            for i in cal[3]:
                #image.paste(im_open(dpath+str(i)+'.jpeg'), positions['d'+str(cal[3].index(i)+1)])
                write_text_to_epaper(65, 50, str(i), (20+65*(i-cal[3][0]), 550), image, font_calendar, 'center', logging)
            for i in cal[4]:
                #image.paste(im_open(dpath+str(i)+'.jpeg'), positions['e'+str(cal[4].index(i)+1)])
                write_text_to_epaper(65, 50, str(i), (20+65*(i-cal[4][0]), 600), image, font_calendar, 'center', logging)
            if len(cal) is 6:
                for i in cal[5]:
                    #image.paste(im_open(dpath+str(numbers)+'.jpeg'), positions['f'+str(cal[5].index(numbers)+1)])
                    write_text_to_epaper(65, 50, str(i), (20+65*(i-cal[5][0]), 650), image, font_calendar, 'center', logging)

            """Connect to Openweathermap API to fetch weather data"""
            logging.info('Openweathermap...')
            if owm.is_API_online() is True:
                logging.debug('weather location = '+ location)
                observation = owm.weather_at_place(location)
                weather = observation.get_weather()
                weathericon = weather.get_weather_icon_name()
                Humidity = str(weather.get_humidity())
                cloudstatus = str(weather.get_clouds())
                weather_description = (str(weather.get_status()))

                if units is "metric":
                    Temperature = str(int(weather.get_temperature(unit='celsius')['temp']))
                    windspeed = str(int(weather.get_wind()['speed']))
                    write_text_to_epaper(200, 50, Temperature + " °C", (990, 20), image, font_normal, 'left', logging)
                    write_text_to_epaper(200, 50, windspeed+" km/h", (990, 120), image, font_normal, 'left', logging)

                if units is "imperial":
                    Temperature = str(int(weather.get_temperature(unit='fahrenheit')['temp']))
                    windspeed = str(int(weather.get_wind()['speed']*0.621))
                    write_text_to_epaper(200, 50, Temperature + " °F", (990, 20), image, font_normal, 'left', logging)
                    write_text_to_epaper(200, 50, windspeed+" mph", (990, 120), image, font_normal, 'left', logging)

                if hours is "24":
                    sunrisetime = str(datetime.fromtimestamp(int(weather.get_sunrise_time(timeformat='unix'))).strftime('%-H:%M'))
                    sunsettime = str(datetime.fromtimestamp(int(weather.get_sunset_time(timeformat='unix'))).strftime('%-H:%M'))

                if hours is "12":
                    sunrisetime = str(datetime.fromtimestamp(int(weather.get_sunrise_time(timeformat='unix'))).strftime('%-I:%M %p'))
                    sunsettime = str(datetime.fromtimestamp(int(weather.get_sunset_time(timeformat='unix'))).strftime('%-I:%M %p'))

                logging.debug('Temperature: '+Temperature+' °C')
                logging.debug('Humidity: '+Humidity+'%')
                logging.debug('Icon code: '+weathericon)
                logging.debug('weather-icon name: '+weathericons[weathericon])
                logging.debug('Wind speed: '+windspeed+'km/h')
                logging.debug('Sunrise-time: '+sunrisetime)
                logging.debug('Sunset time: '+sunsettime)
                logging.debug('Cloudiness: ' + cloudstatus+'%')
                logging.debug('Weather description: '+weather_description)

                """Add the weather icon"""
                image.paste(im_open(wpath+weathericons[weathericon]+'.jpeg'), wiconplace)

                """Add the temperature icon at it's position"""
                image.paste(tempicon, tempplace)

                """Add the humidity icon and display the humidity"""
                image.paste(humicon, humplace)
                write_text_to_epaper(200, 50, Humidity + " %", (990, 70), image, font_normal, 'left', logging)

                """Add the sunrise icon and display the sunrise time"""
                image.paste(sunriseicon, sunriseplace)
                write_text_to_epaper(200, 50, sunrisetime, (750, 70), image, font_normal, 'left', logging)

                """Add the sunset icon and display the sunset time"""
                image.paste(sunseticon, sunsetplace)
                write_text_to_epaper(200,50, sunsettime, (750, 120), image, font_normal, 'left', logging)

                """Add the wind icon at it's position"""
                image.paste(windicon, windiconspace)

                """Add a short weather description"""
                if len(cloudstatus) > 0:
                	write_text_to_epaper(200,50, weather_description, (750, 20), image, font_normal, 'left', logging)
                else:
                	write_text_to_epaper(200,50, weather_description, (750, 20), image, font_normal, 'left', logging)

            else:
                image.paste(no_response, wiconplace)
                pass

            """Algorithm for filtering and sorting events from your
            iCalendar/s"""
            logging.info('Fetching calendar')
            events_this_month = []
            upcoming = []
            today = date.today()

            """Create a time span using the events_max_range value (in days)
            to filter events in that range"""
            time_span = today + timedelta(days=int(events_max_range))

            ical_urls = []
            for icalendars in ical_urls:
                decode = str(urlopen(icalendars).read().decode())
                fix_e_1 = decode.replace('BEGIN:VALARM\r\nACTION:NONE','BEGIN:VALARM\r\nACTION:DISPLAY\r\nDESCRIPTION:')
                fix_e_2 = fix_e_1.replace('BEGIN:VALARM\r\nACTION:EMAIL','BEGIN:VALARM\r\nACTION:DISPLAY\r\nDESCRIPTION:')
                #uncomment line below to display your calendar in ical format
                #print(fix_e_2, file=sys.stdout)
                ical = Calendar(fix_e_2)
                for events in ical.events:
                    if events.begin.date().month is today.month:
                        if int((events.begin).format('D')) not in events_this_month:
                            events_this_month.append(int((events.begin).format('D')))
                    if today <= events.begin.date() <= time_span:
                        upcoming.append({'date':events.begin.format('YYYY MM DD'), 'event':events.name})

            def takeDate(elem):
                return elem['date']

            upcoming.sort(key=takeDate)

            del upcoming[7:]

            #print('Upcoming events:',upcoming, file=sys.stdout) #Display fetched events

            """Write event dates and names on the E-Paper"""
            for dates in range(len(upcoming)):
                #readable_date = datetime.strptime(upcoming[dates]['date'], '%Y %m %d').strftime('%-d %b')
                readable_date = datetime.strptime(upcoming[dates]['date'], '%Y %m %d').strftime('%b %-d')
                #write_text_fontnormal_right(100, 40, readable_date, date_positions['d'+str(dates+1)])
                #write_text_fontnormal_right(100, 40, readable_date, date_positions['d'+str(dates+1)])
                write_text_to_epaper(100, 40, readable_date, date_positions['d'+str(dates+1)], image, font_normal, 'right', logging)

            for events in range(len(upcoming)):
                #write_text_fontnormal_left(540, 40, (upcoming[events]['event']), event_positions['e'+str(events+1)])
                write_text_to_epaper(540, 40, (upcoming[events]['event']), event_positions['e'+str(events+1)], image, font_normal, 'left', logging)

            """Add rss-feeds at the bottom section of the Calendar"""
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

            rss_feed = []
            for feeds in rss_feeds:
                text = feedparser.parse(feeds)
                for posts in text.entries:
                    rss_feed.append(posts.title+" "+posts.description)

            random.shuffle(rss_feed)
            news = []

            if len(cal) is 5:
                del rss_feed[4:]

            if len(cal) is 6:
                del rss_feed[2:]

            for title in range(len(rss_feeds)):
                news.append(multiline_text(rss_feed[title], 1100))

            news = [j for i in news for j in i]

            if len(cal) is 5:
                if len(news) > 5:
                    del news[4:]
                for lines in range(len(news)):
                    #write_text_fontnormal_left(1100, 40, news[lines], rss_places['line_'+str(lines+1)])
                    write_text_to_epaper(1100, 40, news[lines], rss_places['line_'+str(lines+1)], image, font_normal, 'left', logging)

            if len(cal) is 6:
                if len(news) > 3:
                    del news[2:]
                for lines in range(len(news)):
                    #write_text_fontnormal_left(1100, 40, news[lines], rss_places['line_'+str(lines+1)])
                    write_text_to_epaper(1100, 40, news[lines], rss_places['line_'+str(lines+1)], image, font_normal, 'left', logging)

            """Draw smaller squares on days with events"""
            #for numbers in events_this_month:
            #    if numbers in cal[0]:
            #        image.paste(eventicon, positions['a'+str(cal[0].index(numbers)+1)], eventicon)
            #    if numbers in cal[1]:
            #        image.paste(eventicon, positions['b'+str(cal[1].index(numbers)+1)], eventicon)
            #    if numbers in cal[2]:
            #        image.paste(eventicon, positions['c'+str(cal[2].index(numbers)+1)], eventicon)
            #    if numbers in cal[3]:
            #        image.paste(eventicon, positions['d'+str(cal[3].index(numbers)+1)], eventicon)
            #    if numbers in cal[4]:
            #        image.paste(eventicon, positions['e'+str(cal[4].index(numbers)+1)], eventicon)
            #    if len(cal) is 6:
            #        if numbers in cal[5]:
            #            image.paste(eventicon, positions['f'+str(cal[5].index(numbers)+1)], eventicon)

            """Draw a larger square on today's date"""
            today = time.day
            if today in cal[0]:
                #image.paste(dateicon, positions['a'+str(cal[0].index(today)+1)], dateicon)
                image.paste(dateicon, (20+65*(today-cal[0][0]), 385), dateicon)
            if today in cal[1]:
                #image.paste(dateicon, positions['b'+str(cal[1].index(today)+1)], dateicon)
                image.paste(dateicon, (20+65*(today-cal[1][0]), 435), dateicon)
            if today in cal[2]:
                #image.paste(dateicon, positions['c'+str(cal[2].index(today)+1)], dateicon)
                image.paste(dateicon, (20+65*(today-cal[2][0]), 485), dateicon)
            if today in cal[3]:
                #image.paste(dateicon, positions['d'+str(cal[3].index(today)+1)], dateicon)
                image.paste(dateicon, (20+65*(today-cal[3][0]), 535), dateicon)
            if today in cal[4]:
                #image.paste(dateicon, positions['e'+str(cal[4].index(today)+1)], dateicon)
                image.paste(dateicon, (20+65*(today-cal[4][0]), 585), dateicon)
            if len(cal) is 6:
                if today in cal[5]:
                    #image.paste(dateicon, positions['f'+str(cal[5].index(today)+1)], dateicon)
                    image.paste(dateicon, (20+65*(today-cal[5][0]), 635), dateicon)

            if NO_EPAPER:
                image.show()
            else:
                # Save the generated image in the E-Paper-folder.
                logging.info('Saving generated image')
                image.save(str(image_name)+'.bmp')
                logging.info('Image saved')

            # Send to E-Paper
                logging.info('Updating E-Paper')
                #os.system('sudo /home/pi/E-Paper-Calendar/Calendar/Driver-files/IT8951/IT8951 0 0 /home/pi/E-Paper-Calendar/Calendar/current-image.bmp')
                os.system('sudo /home/pi/Drivers/IT8951/IT8951 0 0 /home/pi/E-Paper-Calendar/Calendar/current-image.bmp')
                logging.info('Done updating')

            #print('______Sleeping until the next loop______'+'\n', file=sys.stdout)

            # delete the list so deleted events can be removed from the list
            del events_this_month
            del upcoming
            del rss_feed
            del news
            gc.collect()

            for i in range(1):
                #nexthour = ((60 - int(time.strftime("%-M")))*60) - (int(time.strftime("%-S")))
                #sleep(nexthour)
                nextminute = (60 - int(datetime.now().strftime("%-S")))
                logging.info('sleep for '+str(nextminute)+' seconds')
                sleep(nextminute)

if __name__ == '__main__':
    main()

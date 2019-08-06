#!/usr/bin/python3
# -*- coding: utf-8 -*-
from PIL import Image, ImageFont
from settings import *
im_open = Image.open

path = '/home/pi/E-Paper-Calendar/Calendar/'
wpath = path+'weather-icons/'
mpath = path+'translations/'+language+'/months/'
weekpath =  path+'translations/'+language+'/week/'
dpath = path+'days/'
opath = path+'other/'

weekday = im_open(opath+'weekday.png')
eventicon = im_open(opath+'event.png')
dateicon = im_open(opath+'today.png')
tempicon = im_open(wpath+'wi-thermometer.jpeg')
humicon = im_open(wpath+'wi-humidity.jpeg')
weekmon = im_open(weekpath+'week-mon.jpeg')
weeksun = im_open(weekpath+'week-sun.jpeg')
no_response= im_open(wpath+'wi-na.jpeg')
sunriseicon = im_open(wpath+'wi-sunrise.jpeg')
sunseticon = im_open(wpath+'wi-sunset.jpeg')
windicon = im_open(wpath+'wi-strong-wind.jpeg')

wiconplace = (550, 90)
tempplace = (950, 90)
humplace = (950, 140)
monthplace = (50, 90)
weekplace = (50, 200)
windiconspace = (950, 190)
sunriseplace = (700, 140)
sunsetplace = (700, 190)

rss_places = {
    'line_1' : (50, 625), 'line_2' : (50, 665), 'line_3' : (50, 705),
    'line_4' : (50, 745), 'line_5' : (50, 785)
    }

e_col = 660
date_col = 550

e_row_1 = 290
e_row_2 = 330
e_row_3 = 370
e_row_4 = 410
e_row_5 = 450
e_row_6 = 490
e_row_7 = 530


event_positions = {
'e1': (e_col, e_row_1), 'e2': (e_col, e_row_2), 'e3': (e_col, e_row_3),
'e4': (e_col, e_row_4), 'e5': (e_col, e_row_5), 'e6': (e_col, e_row_6),
'e7': (e_col, e_row_7)
}

date_positions = {
'd1': (date_col, e_row_1), 'd2': (date_col, e_row_2), 'd3': (date_col, e_row_3),
'd4': (date_col, e_row_4), 'd5': (date_col, e_row_5), 'd6': (date_col, e_row_6),
'd7': (date_col, e_row_7)
}

col1 = 50
col2 = 110
col3 = 170
col4 = 230
col5 = 290
col6 = 350
col7 = 410

row1 = 240
row2 = 310
row3 = 380
row4 = 450
row5 = 520
row6 = 590

positions = {
'a1': (col1, row1), 'a2': (col2, row1), 'a3': (col3, row1), 'a4': (col4, row1),
'a5': (col5, row1), 'a6': (col6, row1), 'a7': (col7, row1),

'b1': (col1, row2), 'b2': (col2, row2), 'b3': (col3, row2), 'b4': (col4, row2),
'b5': (col5, row2), 'b6': (col6, row2), 'b7': (col7, row2),

'c1': (col1, row3), 'c2': (col2, row3), 'c3': (col3, row3), 'c4': (col4, row3),
'c5': (col5, row3), 'c6': (col6, row3), 'c7': (col7, row3),

'd1': (col1, row4), 'd2': (col2, row4), 'd3': (col3, row4), 'd4': (col4, row4),
'd5': (col5, row4), 'd6': (col6, row4), 'd7': (col7, row4),

'e1': (col1, row5), 'e2': (col2, row5), 'e3': (col3, row5), 'e4': (col4, row5),
'e5': (col5, row5), 'e6': (col6, row5), 'e7': (col7, row5),

'f1': (col1, row6), 'f2': (col2, row6), 'f3': (col3, row6), 'f4': (col4, row6),
'f5': (col5, row6), 'f6': (col6, row6), 'f7': (col7, row6)
}

week_row = 200

weekdaysmon = {
'Mon': (col1,week_row), 'Tue': (col2,week_row), 'Wed': (col3,week_row),
'Thu': (col4,week_row), 'Fri': (col5,week_row), 'Sat': (col6,week_row),
'Sun': (col7,week_row)
}

weekdayssun = {
'Sun': (col1,week_row), 'Mon': (col2,week_row), 'Tue': (col3,week_row),
'Wed': (col4,week_row), 'Thu': (col5,week_row), 'Fri': (col6,week_row),
'Sat': (col7,week_row)
}

weathericons = {
'01d': 'wi-day-sunny', '02d':'wi-day-cloudy', '03d': 'wi-cloudy',
'04d': 'wi-cloudy-windy', '09d': 'wi-showers', '10d':'wi-rain',
'11d':'wi-thunderstorm', '13d':'wi-snow', '50d': 'wi-fog',
'01n': 'wi-night-clear', '02n':'wi-night-cloudy',
'03n': 'wi-night-cloudy', '04n': 'wi-night-cloudy',
'09n': 'wi-night-showers', '10n':'wi-night-rain',
'11n':'wi-night-thunderstorm', '13n':'wi-night-snow',
'50n': 'wi-night-alt-cloudy-windy'}

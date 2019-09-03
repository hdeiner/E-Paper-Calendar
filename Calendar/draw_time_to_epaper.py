from PIL import Image, ImageDraw, ImageFont, ImageOps
from settings import *
import math

def draw_time_to_epaper(size, position_x, position_y, time, image, clock_face, logging):
    #print('draw_time_to_epaper size=' + str(size) + ' x=' + str(position_x) + ' y=' + str(position_y))
    logging.debug('write_text_to_epaper size=' + str(size) +' x=' + str(position_x) + ' y=' + str(position_y))

    space = Image.new('L', (size*4, size*4), color=255)
    if (DRAW_OUTLINES):
        ImageDraw.Draw(space).line([(2,2),(size*4-2,2),(size*4-2,size*4-2),(2,size*4-2),(2,2)], fill=0, width=2)

    #image.paste(Image.open(clock_face))
    clock_image = Image.open(clock_face)
    clock_image_resized = clock_image.resize((size*4, size*4), Image.ANTIALIAS)
    space.paste(clock_image_resized)

    hours = int(time.strftime("%-I"))
    minutes = int(time.strftime("%-M"))
    hour_degrees = (hours + minutes/60)/12 * 360
    hour_radians = hour_degrees * 3.14159 / 180
    minute_degrees = minutes/60 * 360
    minute_radians = minute_degrees * 3.14159 / 180

    #print('draw_time_to_epaper hours=' + str(hours))
    #print('draw_time_to_epaper minutes=' + str(minutes))
    #print('draw_time_to_epaper seconds=' + str(seconds))

    #print('draw_time_to_epaper hour_degrees=' + str(hour_degrees))
    #print('draw_time_to_epaper hour_radians=' + str(hour_radians))
    #print('draw_time_to_epaper hour_display sin=' + str(math.sin(hour_radians)))
    #print('draw_time_to_epaper hour_display cos=' + str(math.cos(hour_radians)))
    end_x = size*4/2 + math.sin(hour_radians)*((size*4/2)-75*4)
    end_y = size*4/2 - math.cos(hour_radians)*((size*4/2)-75*4)
    start_x = size*4/2 - math.sin(hour_radians)*10
    start_y = size*4/2 + math.cos(hour_radians)*10
    #print('draw_time_to_epaper hour_display start_x=' + str(start_x))
    #print('draw_time_to_epaper hour_display start_y=' + str(start_y))
    #print('draw_time_to_epaper hour_display end_x=' + str(end_x))
    #print('draw_time_to_epaper hour_display end_y=' + str(end_y))
    ImageDraw.Draw(space).line((start_x, start_y, (end_x, end_y)), fill=0, width=10*4)

    #print('draw_time_to_epaper minute_degrees=' + str(minute_degrees))
    #print('draw_time_to_epaper minute_radians=' + str(minute_radians))
    #print('draw_time_to_epaper minute_display sin=' + str(math.sin(minute_radians)))
    #print('draw_time_to_epaper minutedisplay cos=' + str(math.cos(minute_radians)))
    end_x = size*4/2 + math.sin(minute_radians)*((size*4/2)-15*4)
    end_y = size*4/2 - math.cos(minute_radians)*((size*4/2)-15*4)
    start_x = size*4/2 - math.sin(minute_radians)*10
    start_y = size*4/2 + math.cos(minute_radians)*10
    #print('draw_time_to_epaper minute_display start_x=' + str(start_x))
    #print('draw_time_to_epaper minute_display start_y=' + str(start_y))
    #print('draw_time_to_epaper minute__display end_x=' + str(end_x))
    #print('draw_time_to_epaper minute_display end_y=' + str(end_y))
    ImageDraw.Draw(space).line((start_x, start_y, (end_x, end_y)), fill=0, width=5*4)

    ImageDraw.Draw(space).ellipse((size*2-7.5, size*2-7.5, size*2+7.5, size*2+7.5), fill=255)

    space_resized = space.resize((size, size), Image.ANTIALIAS)
    image.paste(space_resized, (position_x, position_y))

#    image.paste(space, (position_x, position_y))

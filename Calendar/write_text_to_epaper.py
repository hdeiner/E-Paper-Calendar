from PIL import Image, ImageDraw, ImageFont, ImageOps
from settings import *

def write_text_to_epaper(box_width, box_height, text, tuple, image, font, alignment, logging):
    text_width, text_height = font.getsize(text)
    #print("write_text_fontnormal_center text_width=" + str(text_width) + " text_height=" + str(text_height), file=sys.stdout)
    logging.debug('write_text_to_epaper text_width=' + str(text_width) + ' text_height=' + str(text_height))
    #print("write_text_fontnormal_center box_width=" + str(box_width) + " box_height=" + str(box_height), file=sys.stdout)
    logging.debug('write_text_to_epaper box_width=' + str(box_width) + ' box_height=' + str(box_height))
    if (text_width, text_height) > (box_width, box_height):
        logging.error('write_text_to_epaper Sorry, your text is too big for the box')
        raise ValueError('Sorry, your text is too big for the box')
    else:
        if (alignment == 'center'):
            x = int((box_width / 2) - (text_width / 2))
        elif (alignment == 'right'):
            x = box_width - text_width
        else:
            x = 0
        space = Image.new('L', (box_width, box_height), color=255)
        if (DRAW_OUTLINES):
            ImageDraw.Draw(space).line([(2,2),(box_width-2,2),(box_width-2,box_height-2),(2,box_height-2),(2,2)], fill=0, width=2)
        ImageDraw.Draw(space).multiline_text((x, 0), text, fill=0, font=font, spacing=1, align=alignment)
        image.paste(space, tuple)

import argparse
import password_generator
import Image, ImageDraw, ImageFont

DEFAULT_IMG_FILE = './info.png'

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--destination',
    help='File destination', default=DEFAULT_IMG_FILE)
parser.add_argument('-p', '--password',
    help='Text for password, blank for generating random', default='')
    
args = vars(parser.parse_args())

img_file = args['destination']
if not args['password']:
    password = password_generator.generate()
else:
    password = args['password']
    
size = (200,100)
black = (0,0,0)
white = (255,255,255)
img = Image.new('RGB', size, white)
draw = ImageDraw.Draw(img)
text_pos = (10,10)
draw.text(text_pos, password, fill=black)
draw = ImageDraw.Draw(img)
img.save(img_file)
    
print password
    

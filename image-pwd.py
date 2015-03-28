#!/usr/bin/env python
import os
import argparse
import password_generator
import svgwrite
import cairosvg

IMG_LOCATION = './output-passwords/'

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--destination',
    help='Output folder default is ' + IMG_LOCATION, default=IMG_LOCATION)
parser.add_argument('-p', '--password',
    help='Password, if blank generates random', default='')
parser.add_argument('-u', '--username',
    help='Username associated with the password, if blank generates random', default='')
    
args = vars(parser.parse_args())

if not args['destination']:
    img_location = IMG_LOCATION
else:
    img_location = args['destination']

if not args['password']:
    password = password_generator.generate()
else:
    password = args['password']
    
if not args['username']:
    username = ''
else:
    username = args['username']
    
filename = img_location + password + '.png'
font_size_title, font_size_text = 10, 20
x_size_px = len(password) * 16.5
dwg = svgwrite.Drawing(filename, (x_size_px, 50))
dwg.add(dwg.rect(insert=(0, 0), size=('100%', '100%'), fill='white'))

if not username:
	dwg.add(dwg.text(password, insert=('5%', '20%'),
		font_family="serif",
		font_size=font_size_text,
		font_weight='bold',
		fill='black'))
	sucess_msg = 'Generated image for password ' + password+ '\nFile saved in ' + img_location
else:
	dwg.add(dwg.text(password, insert=('5%', '20%'),
		font_family="serif",
		font_size=font_size_text/2,
		font_weight='bold',
		fill='black'))
	dwg.add(dwg.text(password, insert=('10%', '40%'),
		font_family="serif",
		font_size=font_size_text/2,
		font_weight='bold',
		fill='black'))
	sucess_msg = 'Generated image for user ' + username + ' and password ' + password + '\nFile saved in ' + img_location

if not os.path.exists(img_location):
    os.makedirs(img_location)

fout = open(filename,'w')
cairosvg.svg2png(bytestring=dwg.tostring(),write_to=fout)

print sucess_msg

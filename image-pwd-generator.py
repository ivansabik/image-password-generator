import argparse
import password_generator

parser = argparse.ArgumentParser()
parser.add_argument('-d', '--destination',
    help='File destination', default='./info.png')
parser.add_argument('-p', '--password',
    help='Text for password, blank for generating random', default='')
args = vars(parser.parse_args())

if not args['password']:
    password = password_generator.generate()
else:
    password = args['password']
print password
    

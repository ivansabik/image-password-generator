# Image password generator
[![Build Status](https://travis-ci.org/ivansabik/image-password-generator.svg)](https://travis-ci.org/ivansabik/image-password-generator)

Image password generator generates random passwords in images for sharing via e-mail on a safer way. It also supports generating an image for a password. Uses https://github.com/sebdah/password-generator for generating random password strings.

### Installation

Install dependencies with ```pip install -r requirements.txt```.
You may need ```sudo apt-get install python-cairosvg```

### Usage

```
usage: image-pwd.py [-h] [-d DESTINATION] [-p PASSWORD] [-u USERNAME]

optional arguments:
  -h, --help            show this help message and exit
  -d DESTINATION, --destination DESTINATION
                        Output folder default is ./output-passwords/
  -p PASSWORD, --password PASSWORD
                        Password, if blank generates random
  -u USERNAME, --username USERNAME
                        Username associated with the password, if blank
                        generates random
```

### Run tests

To run the tests: ```python -m unittest discover```

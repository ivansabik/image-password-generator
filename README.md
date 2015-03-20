# Image password generator
[![Build Status](https://travis-ci.org/ivansabik/image-password-generator.svg)](https://travis-ci.org/ivansabik/image-password-generator)

Image password generator generates random passwords in images for sharing via e-mail on a safer way. It also supports generating an image for a password. Uses https://github.com/sebdah/password-generator for generating random password strings.

### Installation

To install globally:

- Give permissions for the file with ```chmod +x image-pwd-generator```
- Copy script``cp image-pwd-generator /usr/local/bin/```
- Use it with ```image-pwd-generator``` 

Alternatively you run it in the folder where you downloaded it with ```python image-pwd-generator``` or ```./image-pwd-generator```

### Usage

```
usage: image-pwd-generator.py [-h] [-d DESTINATION] [-p PASSWORD]

optional arguments:
  -h, --help            show this help message and exit
  -d DESTINATION, --destination DESTINATION
                        File destination
  -p PASSWORD, --password PASSWORD
                        Text for password, blank for generating random
```

### Run tests

To run the tests: ```python -m unittest discover```

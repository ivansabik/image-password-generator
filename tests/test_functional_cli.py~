import unittest
import subprocess
import os

class CliFunctionalTest(unittest.TestCase):
	def test_generate_random_pass(self):
		# Generate random password and write image with default options
		# An image is created with the password at ./imgs/info.png
		# Output in CLI contains the generated password
		cli_response =  subprocess.check_output(['python','../image-pwd-generator.py'], stderr=subprocess.STDOUT)
		self.fail('Finish test to generate random password!')
		
	def test_generate_img_for_input_pass(self):
		# Generate and write image for password passed as option
		# An image is created with the password at ./imgs/info.png
		# Output in CLI contains a success
		cli_response =  subprocess.check_output(['python','../image-pwd-generator.py'], stderr=subprocess.STDOUT)
		self.fail('Finish test to generate image from text password!')
		
	def test_invalid_cli_options(self):
		# Invalid options passed outputs error
		try:
			cli_response =  subprocess.check_output(['python','../image-pwd-generator.py', '-y'], stderr=subprocess.STDOUT)
			self.fail('Did not output error for unrecognized arguments')
		except subprocess.CalledProcessError, e:
			assert 'unrecognized arguments' in e.output
	
	def test_existing_file_confirmation(self):
		# When a file already exists, ask for confirmation to overwrite
		self.fail('Finish test for confirmation to overwrite file')

if __name__ == '__main__':
	unittest.main()

import unittest
import subprocess
import os
import re

DEFAULT_IMG_FILE = './info.png'
CLI_SCRIPT = './image-pwd-generator.py' # Change if tests runned from ./tests
PASS_FOR_INPUT_TEST = 'MySuperSecretPass'

class CliFunctionalTest(unittest.TestCase):
	
	def tearDown(self):
		global DEFAULT_IMG_FILE
		try:
			os.remove(DEFAULT_IMG_FILE)
		except OSError:
			pass
		
	def test_generate_random_pass(self):
		# Generate random password and write image with default options
		# An image is created with the password at ./info.png
		# Output in CLI contains the generated password
		global DEFAULT_IMG_FILE, CLI_SCRIPT
		cli_response =  subprocess.check_output(['python', CLI_SCRIPT], stderr=subprocess.STDOUT)
		password_pattern = re.compile('^[A-Za-z0-9]{12}$')
		assert password_pattern.match(cli_response) is not None, 'Output "%s" does not match password alpanumeric of length 12' % cli_response
		assert os.path.isfile(DEFAULT_IMG_FILE), 'Image file not found: %s' % DEFAULT_IMG_FILE
		
	def test_generate_img_for_input_pass(self):
		# Generate and write image for password passed as option
		# An image is created with the password at ./info.png
		# Output in CLI contains a success
		global CLI_SCRIPT, PASS_FOR_INPUT_TEST
		cli_response =  subprocess.check_output(['python', CLI_SCRIPT, '-p', PASS_FOR_INPUT_TEST], stderr=subprocess.STDOUT)
		assert PASS_FOR_INPUT_TEST in cli_response
		assert os.path.isfile(DEFAULT_IMG_FILE), 'Image file not found: %s' % DEFAULT_IMG_FILE
		
	def test_invalid_cli_options(self):
		global CLI_SCRIPT
		# Invalid options passed outputs error in console
		try:
			cli_response =  subprocess.check_output(['python', CLI_SCRIPT, '-y'], stderr=subprocess.STDOUT)
			self.fail('Did not output error for unrecognized arguments')
		except subprocess.CalledProcessError, e:
			assert 'unrecognized arguments' in e.output
	
	@unittest.skip('Skipping test for existing file confirmation')
	def test_existing_file_confirmation(self):
		# When a file already exists, ask for confirmation to overwrite
		self.fail('Finish test for confirmation to overwrite file')

if __name__ == '__main__':
	unittest.main()

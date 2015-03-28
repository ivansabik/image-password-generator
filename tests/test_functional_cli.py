import unittest
import os
import re
from scripttest import TestFileEnvironment

CMD_GENERATE_DEFAULT_OUTPUT = 'python ../image-pwd.py'
CMD_GENERATE_CUSTOM_OUTPUT  = 'python ../image-pwd.py -d ./custom-output-test-images/'
CMD_GENERATE_CUSTOM_PASS  = 'python ../image-pwd.py -p K3nnw0r7hy'
CMD_GENERATE_USER_PASS = 'python ../image-pwd.py -u kenny -p K3nnw0r7hy'
CMD_GENERATE_USER_RANDOM_PASS  = 'python ../image-pwd.py -u kenny'

class CliFunctionalTest(unittest.TestCase):
	def setUp(self):
		self.env = TestFileEnvironment('./test-output')
		
	def test_generate_random_pass_default_dir(self):
		# Generate random password and write image with default options
		# An image is created with the password at ./output-passwords/
		# Output in CLI contains success message
		cli_response = self.env.run(CMD_GENERATE_DEFAULT_OUTPUT)
		success_pattern = re.compile('Generated image for password*.*\nFile saved in \.\/output-passwords\/')
		self.assertTrue(
			success_pattern.match(cli_response.stdout),
			'Output was: ' + cli_response.stdout)
		self.assertTrue(
			cli_response.files_created,
			'File with image was not created')
			
	def test_generate_random_pass_custom_dir(self):
		# Generate random password and write image with destination
		# folder ./custom-output-test-images/
		# An image is created with the password at ./custom-output-test-images/
		# Output in CLI contains success message
		cli_response = self.env.run(CMD_GENERATE_CUSTOM_OUTPUT)
		success_pattern = re.compile('Generated image for password*.*\nFile saved in \.\/custom-output-test-images\/')
		self.assertTrue(
			success_pattern.match(cli_response.stdout),
			'Output was: ' + cli_response.stdout)
		self.assertTrue(
			cli_response.files_created,
			'File with image was not created')
	
	def test_generate_img_for_input_pass(self):
		# Generate and write image for password K3nnw0r7hy passed as option
		# An image is created with the password at ./output-passwords/K3nnw0r7hy.png
		# Output in CLI contains success message
		cli_response = self.env.run(CMD_GENERATE_CUSTOM_PASS)
		success_pattern = re.compile('Generated image for password K3nnw0r7hy\nFile saved in \.\/output-passwords\/')
		self.assertTrue(
			success_pattern.match(cli_response.stdout),
			'Output was: ' + cli_response.stdout)
		self.assertTrue(
			cli_response.files_created,
			'File with image was not created')
		
	def test_generate_img_for_input_user_and_pass(self):
		# Generate and write image for username kenny
		# and password K3nnw0r7hy passed as options
		# An image is created with the password at ./info.png
		# Output in CLI contains a success message
		cli_response = self.env.run(CMD_GENERATE_USER_PASS)
		success_pattern = re.compile('Generated image for user kenny and password K3nnw0r7hy\nFile saved in \.\/output-passwords\/')
		self.assertTrue(
			success_pattern.match(cli_response.stdout),
			'Output was: ' + cli_response.stdout)
		self.assertTrue(
			cli_response.files_created,
			'File with image was not created')
		
	def test_generate_img_for_input_user_and_pass(self):
		# Generate and write image for username kenny
		# and password K3nnw0r7hy passed as options
		# An image is created with the password at ./info.png
		# Output in CLI contains a success message
		cli_response = self.env.run(CMD_GENERATE_USER_RANDOM_PASS)
		success_pattern = re.compile('Generated image for user kenny and password*.*\nFile saved in \.\/output-passwords\/')
		self.assertTrue(
			success_pattern.match(cli_response.stdout),
			'Output was: ' + cli_response.stdout)
		self.assertTrue(
			cli_response.files_created,
			'File with image was not created')

if __name__ == '__main__':
	unittest.main()

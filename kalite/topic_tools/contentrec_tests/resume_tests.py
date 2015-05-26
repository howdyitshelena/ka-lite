'''
This module contains all tests for the functions invoked to
get the "Resume" recommendations.
'''

import unittest
from kalite.topic_tools.content_recommendation import *

class TestResumeMethods(unittest.TestCase):

	def setUp(self):
		'''Performed before every test'''
		self.user_with_no_activity = 1	#a brand new user
		self.user_with_activity = 2		#a user with valid rows in Facility+ExerciseLogs

	def tearDown(self):
		'''Performed after each test'''
		self.user_with_activity = None
		self.user_with_no_activity = None

	def test_resume_overall(self):
		'''get_resume_recommendations()'''
		pass

	def test_get_most_recent_incomplete_item(self):
		'''test_get_most_recent_incomplete_item()'''
		pass




#runs tests
suite = unittest.TestLoader().loadTestsFromTestCase(TestResumeMethods)
unittest.TextTestRunner(verbosity=2).run(suite)

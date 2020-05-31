# Unit tests for helper_functions.py
import pandas as pd
import unittest
import os
import sys
sys.path.append('../data')
from helper_functions import *

test_df = pd.DataFrame({'movies' : ["A", "B", "C", "D"], 
			'genres' : ["Action", "Comedy", "Comedy", "Romance"]})

class test_df(unittest.TestCase):
	"""
	Check that the unique genres in the test_df
	have been correctly identified.
	"""
	def one_shot_unique_genres(self):
		self.assertEqual(
			get_unique_genres(test_df), 
			set(["Action", "Comedy", "Romance"]))

	def test_save_file():
	"""
	Check that the save_file function correctly outputs a csv file,
	then remove the created file.
	"""	
		save_file(test_df, "./", "test_file", ".csv")
		self.assertTrue(os.path.exists(self.cwd + './test_file.csv'))
		os.system("rm test_file.csv")


if __name__ == '__main__':
    unittest.main() 

""" prime function test"""

import unittest
from primes import is_prime


class Test_primes(unittest.TestCase):
	def setUp(self):
		pass

	def test_no_string_input(self):
		self.assertEqual (is_prime ("one"), "Enter a number")

	def test_non_negative_input(self):
		self.assertEqual (is_prime (-1), "Enter a positive number")
	
	def test_non_zero_numbers(self):
		self.assertEqual(is_prime(0), "Enter a positive number")


	def test_no_float_input(self):
		self.assertEqual (is_prime (3.2), "Sorry! Prime numbers are whole")

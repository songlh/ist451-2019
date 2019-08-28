import unittest
from fib import *
from twoSum import *

class TestFIB(unittest.TestCase):
	def test_0(self):
		self.assertEqual(fib(0), 1)
		self.assertEqual(fib(1), 1)

	def test_1(self):
		self.assertEqual(fib(2), 2)

	def test_2(self):
		self.assertEqual(fib(3), 3)

	def test_3(self):
		self.assertEqual(fib(4), 5)
		self.assertEqual(fib(5), 8)
		self.assertEqual(fib(6), 13)

	def test_4(self):
		self.assertEqual(fib(7), 21)
		self.assertEqual(fib(8), 34)
		self.assertEqual(fib(9), 55)

	def test_5(self):
		nums = [2, 7, 11, 15]
		target = 9

		rets = twoSum(nums, target)
		
		self.assertEqual(rets[0], 0)
		self.assertEqual(rets[1], 1)

	def test_6(self):
		nums = [3, 2, 4]
		target = 6

		rets = twoSum(nums, target)
		
		self.assertEqual(rets[0], 1)
		self.assertEqual(rets[1], 2)

	def test_7(self):
		nums = [0, 2, 11, 19, 90]
		target = 21

		rets = twoSum(nums, target)
		
		self.assertEqual(rets[0], 1)
		self.assertEqual(rets[1], 3)

	def test_8(self):
		nums = [-8, -2, -1,  1,  5, 9, 11]
		target = 0

		rets = twoSum(nums, target)
		
		self.assertEqual(rets[0], 2)
		self.assertEqual(rets[1], 3)

	def test_9(self):
		nums = [-8, -2,  0,  1, 8, 11 ]
		target = 3

		rets = twoSum(nums, target)
		
		self.assertEqual(rets[0], 0)
		self.assertEqual(rets[1], 5)

if __name__ == '__main__':
	unittest.main()
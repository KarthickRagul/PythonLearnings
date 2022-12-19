import unittest   # unittest library 
import add

class TestAddition(unittest.TestCase): # We are inherting the unittest class

	def test_addition(self):
		number1 = 10
		number2 = 20
		result = add.addition(number1,number2)
		self.assertEqual(result,30)

if __name__ == '__main__':
	unittest.main()

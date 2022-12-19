class Calculation_Square:
	def __init__(self,number):
		self.number=number

	def square(self):
		square=self.number ** 2
		print(f"Square of the number is : {square}")


class_obj = Calculation_Square(3)
class_obj.square()
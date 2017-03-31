class Shape:
	__wight = ''
	__height = ''

	def __init__(self, wight, height):
		self.__wight = wight
		self.__height = height

	def get_wight(self):
		return self.__wight

	def get_height(self):
		return self.__height

class Triangle(Shape):
	def __init__(self, wight, height):
		Shape.__init__(self, wight, height)

	def area(self):
		return 0.5 * self.get_wight() * self.get_height()

class Rectangle(Shape):
	def __init__(self, wight, height):
		Shape.__init__(self, wight, height)

	def area(self):
		return self.get_wight() * self.get_height()

ABCD = Rectangle(3, 4)

ABC = Triangle(3, 4)

print(ABCD.area(), ' ', ABC.area())
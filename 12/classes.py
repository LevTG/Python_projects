class Parent:
	x = 1
	def __init__(self):
		self.z = 0

class Child1(Parent):
	pass

class Child2(Parent):
	pass

print(Parent.x, Child1.x, Child2.x) # 1 1 1

Child1.x = 2

print(Parent.x, Child1.x, Child2.x) # 1 2 1

Parent.x = 3

print(Parent.x, Child1.x, Child2.x) # 3 2 3

mother = Parent()
dougther = Child1()
print(mother.z, dougther.z)

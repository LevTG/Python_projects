class Mother:
	sername = ''
	name = ''

	def __init__(self, Name, Sername):
		self.sername = Sername
		self.name = Name

	def get_name(self):
		return self.name

	def get_sername(self):
		return self.sername

	def __repr__(self):
		return self.get_repr(self)

	def get_repr(self):
        return " ".join(["Mother:", self.get_name(), "\n",
                    	 self.get_sername(), "\n"])


class Doughter(Mother):
	def __init__(self, Name, Sername):
		Mother.__init__(self, Name, Sername)

	def get_repr(self):
		return return " ".join(["Doughter:", self.name, "\n", "sername:", self.sername, "\n"])
	

mama = Mother('A', 'L')
doch = Doughter('B', 'L')

if __name__ == "__main__":
    strange_list = [mama, doch]

    for element in strange_list:
        if isinstance(element, Mother):
            print(element)
        else:
        	print("\n\t", element) 
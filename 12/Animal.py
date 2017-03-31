from abc import abstractmethod

class Animal:
    __name = ""
    __age = ""

    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def set_name(self, name):
        self.__name = name

    def set_age(self, age):
        self.__age = age

    @abstractmethod
    def get_repr(self):
        pass

    def __repr__(self):
        return self.get_repr()


class Zebra(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def __repr__(self):
        return self.get_repr()

    def get_repr(self):
        return " ".join(["Zebra:", self.get_name(), "\n",
                        "age:", self.get_age(), "\n"])

class Dolphin(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def get_repr(self):
        return " ".join(["Dolphin:", self.get_name(), "\n",
                        "age:", self.get_age(), "\n"])

if __name__ == "__main__":
    Zebra = Zebra('Marty', '10')
    Dolphin = Dolphin('Sally', '5')
    strange_list = [Zebra, Dolphin]

    for element in strange_list:
        if isinstance(element, Animal):
            print(element)
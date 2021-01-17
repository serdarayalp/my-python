class person:

    def __init__(self):
        self.__name = ''

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @name.deleter
    def name(self, value):
        del self.__name


p = person()

p.name = "Serdar"
print(p.name)

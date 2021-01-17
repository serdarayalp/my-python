class My_Class():
    def __init__(self):
        self.__private = "privat"
        self._protected = "protected"
        self.public = "public"


my_object = My_Class()

print(my_object._My_Class__private)

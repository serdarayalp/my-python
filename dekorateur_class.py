class my_decorator_class:

    def __init__(self, my_decorator_function):
        self.my_decorator_function = my_decorator_function

    def __call__(self):
        print("inside of __call__", self.my_decorator_function.__name__)
        self.my_decorator_function()


@my_decorator_class
def my_function():
    print("inside of my_function")


my_function()

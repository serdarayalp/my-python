def my_function_decorator(decorator_function):
    def my_decorator_function():
        my_decorator_function.counter += 1
        return decorator_function()

    my_decorator_function.counter = 0
    return my_decorator_function


@my_function_decorator
def my_function():
    pass

for i in range(10):
    my_function()

print(my_function.counter)

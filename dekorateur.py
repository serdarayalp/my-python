def my_dekorateur(dekorateur_function):
    def my_dekorateur_function(a, b):
        if type(a) == int and a > 0 and type(b) == int and b > 0:
            return dekorateur_function(a, b)
        else:
            raise Exception("IllegalArgument")
    return my_dekorateur_function


@my_dekorateur
def my_function(a, b):
    return a + b


print(my_function(1, 2))

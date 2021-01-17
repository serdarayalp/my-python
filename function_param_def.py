def my_function(param):
    print(param, my_function.authorName, my_function.authorSurname)

my_function.authorName = 'Max'
my_function.authorSurname = 'Mustermann'

my_function(10)

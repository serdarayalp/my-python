class A:
    pass


x = A()
print(type(x))


# -----------------------

# Alternative zur Klassenerstellung
B = type("B", (), {})
x = B()
print(type(x))

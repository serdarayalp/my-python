def f(x):
     # Alternativ: if "counter" in dir(f):
    if hasattr(f, "counter"):
        f.counter += 1
    else:
        f.counter = 0
    return x + 3


for i in range(10):
    f(i)

print(f.counter)

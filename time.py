import time

n = 100000

start_time = time.time()
l = []
for i in range(n):
    l = l + [i * 2]
print(time.time() - start_time)  # ? seconds

# ------------------------------

start_time = time.time()
l = []
for i in range(n):
    l += [i * 2]
print(time.time() - start_time)  # ? seconds

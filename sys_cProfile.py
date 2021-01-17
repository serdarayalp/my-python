import sys
import cProfile

nums_squared_lc = [num ** 2 for num in range(100000)]
nums_squared_gc = (num ** 2 for num in range(100000))

print(sys.getsizeof(nums_squared_lc))
print(sys.getsizeof(nums_squared_gc))

cProfile.run('sum([i * 2 for i in range(100000)])')
cProfile.run('sum((i * 2 for i in range(100000)))')

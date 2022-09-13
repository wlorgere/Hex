import timeit

f1 = lambda: 2**100
f2 = lambda: 1<<100

print(timeit.timeit(f1, number=1000000))

print(timeit.timeit(f2, number=1000000))
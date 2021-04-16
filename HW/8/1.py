from functools import reduce
numbers = [57, 287, 4581, 6, 77, 9]
max = reduce(lambda x, y: x + y, map(str, sorted(numbers, key=str, reverse=True)))

print(max)
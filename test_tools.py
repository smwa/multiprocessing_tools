from multiprocessing_tools import map, filter

def mapper(item):
    return item**2

def filterer(item):
    return item % 2 == 0

items = range(6)

mapped = list(map(mapper, items, ordered=True))
print(mapped)
assert(mapped == [0, 1, 4, 9, 16, 25])
filtered = list(filter(filterer, mapped))
print(filtered)
assert(filtered == [0, 4, 16])

numbers_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


# a functional way of summing
from functools import reduce

cumsum = reduce(lambda acc, x: acc + x, numbers_list)
print(cumsum)

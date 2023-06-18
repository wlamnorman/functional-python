def add(x, y, z):
    return x + y + z


def add_partial(x):
    return lambda y, z: x + y + z


# using partial from functools
from functools import partial

add_5 = add_partial(5)
print(add_5(6, 7))


add_5 = partial(add, 5)
print(add_5(6, 7))

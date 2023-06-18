numbers_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# re-write the following in a functional way using the map function
doubled_list = []
for x in numbers_list:
    doubled_list.append(x * 2)
print(doubled_list)

# functional way
doubled_list_func = list(map(lambda num: 2 * num, numbers_list))
print(doubled_list_func)

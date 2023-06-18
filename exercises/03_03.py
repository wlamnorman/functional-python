numbers_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# re-write the following in a functional way using the filter function
even_numbers = []
for x in numbers_list:
    if x % 2 == 0:
        even_numbers.append(x)
print(even_numbers)

# functional
even_numbers = list(filter(lambda num: num % 2 == 0, numbers_list))
print(even_numbers)

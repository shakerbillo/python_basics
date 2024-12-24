my_set = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
print(my_set)
print(len(my_set))

for x in my_set:
    print(x)


my_set.discard(10)
print(my_set)
my_set.add(12)
print(my_set)
my_set.update([14, 25, 36, 47, 52, 67])
print(my_set)


my_tuple = (1, 2, 3, 4, 5, 6, 7, 8)
print(my_tuple)
print(len(my_tuple))
print(my_tuple[4])

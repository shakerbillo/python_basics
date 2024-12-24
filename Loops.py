my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(my_list[0])
# print(my_list[1])
# print(my_list[2])
# print(my_list[3])
# print(my_list[4])

for iterator in my_list:
    print(iterator)


sum_of_list = 0
for num in my_list:
    sum_of_list += num

print("Sum of the list:", sum_of_list)


days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

for day in days:
    print(f"Happy {day}!")


# Using a while loop to iterate over the list
i = 0
while i < len(days):
    print(f"Happy {days[i]}!!!!!")
    i += 1

x = 0
while x < 10:
    x += 1
    if x % 2 == 0:
        continue
    print(x)

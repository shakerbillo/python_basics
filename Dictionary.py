user_dictionary = {
    "id": 1,
    "name": "Alice Smith",
    "age": 25,
    "username": "alyst",
    "city": "Los Angeles",
}

user_dictionary["married"] = True
print(user_dictionary)
print(len(user_dictionary))

for x in user_dictionary:
    print(x)


user_dictionary2 = user_dictionary.copy()
user_dictionary2["address"] = "123 Main St"
print(user_dictionary2)
user_dictionary.pop("age")
print(user_dictionary)

user_dictionary.clear()
print(user_dictionary)

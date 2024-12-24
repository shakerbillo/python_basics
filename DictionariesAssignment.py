"""
Based on the dictionary:

my_vehicle = {
    "model": "Ford",
    "make": "Explorer",
    "year": 2018,
    "mileage": 40000
}
- Create a for loop to print all keys and values

- Create a new variable vehicle2, which is a copy of my_vehicle

- Add a new key 'number_of_tires' to the vehicle2 variable that is equal to 4

- Delete the mileage key and value from vehicle2

- Print just the keys from vehicle2
"""

my_vehicle = {"model": "Ford", "make": "Explorer", "year": 2018, "mileage": 40000}

for key, value in my_vehicle.items():
    print(f"{key}: {value}")


vehicle2 = my_vehicle.copy()
vehicle2["number_of_tires"] = 4
print(vehicle2)


del vehicle2["mileage"]

print(vehicle2.keys())

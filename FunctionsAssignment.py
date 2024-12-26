"""
- Create a function that takes in 3 parameters(firstname, lastname, age) and

returns a dictionary based on those values
"""


def create_person_info(firstname, lastname, age):
    person_info = {"firstname": firstname, "lastname": lastname, "age": age}
    return person_info


person_1 = create_person_info("Agyei", "Kissi", 31)
print(person_1)

person_2 = create_person_info("Ebo", "Appiah", 36)
print(person_2)

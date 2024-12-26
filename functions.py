print("Hello welcome to functions")


def print_my_name(first_name, last_name):
    print(f"Hello {first_name} {last_name}!")


print_my_name("William", "Steel")


def print_color_red():
    color = "Red"
    print(color)


color = "Blue"
print(color)
print_color_red()


def print_numbers(highest_number, lowest_number):
    print(highest_number)
    print(lowest_number)


print_numbers(29, 6)


def multiply_numbers(num1, num2):
    result = num1 * num2
    return result


print(multiply_numbers(5, 10))


def print_list(list_of_numbers):
    for number in list_of_numbers:
        print(number)
        

numbers_list = [1, 2, 3, 4, 5,6]
print_list(numbers_list)


def buy_item(cost_of_item):
    return cost_of_item + add_tax_to_item(cost_of_item)

def add_tax_to_item(cost_of_item):
    current_tax_rate = .03
    return cost_of_item * current_tax_rate

final_cost = buy_item(60)
print(final_cost)
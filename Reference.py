# Create A Dictionary
example_dict = {1: 5, 2: 5, 3: 5, 4: 2, 5: 2, 6: 1, 7: 3}
for key, value in example_dict.items():
    print(f'{key}: {value}')
# count dictionary into another
count_dict = {}
for value in example_dict.values():
    count_dict[value] = count_dict.get(value, 0) + 1
print(count_dict)

# List
random_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_of_random_things = [1, 2, "Hello World", 3, 4]
print(len(list_of_random_things))
print(list_of_random_things[0:3])
print(list_of_random_things[2])

list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list_of_added_numbers = [x + 1 for x in list_of_numbers]
print(list_of_added_numbers)

# sets
countries = ['Angola', 'Maldives', 'India', 'United States', 'India', 'Denmark', 'Sweden', 'Ghana']
country_set = set(countries)
print(country_set)
numbers = [1, 2, 6, 3, 1, 1, 6]
unique_nums = set(numbers)
print(unique_nums)

# map
random_string = "Hello World"

upper_list = list(map(str.upper, random_string))
print(upper_list)


def add_number(x):
    return x + 5


random_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
added_numbers = list(map(add_number, random_numbers))
print(added_numbers)

added_numbers_lambda = list(map(lambda x: x + 100, random_numbers))
print(added_numbers_lambda)

# print
value = 100
speed = 150
print(f"Value is {value}")
print("value is {} and speed {}".format(value, speed))

while True:
    try:
        x = int(input("Enter a number: "))
        break
    except:
        print("Invalid input")

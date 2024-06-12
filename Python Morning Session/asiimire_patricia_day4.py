# # Exercise
# # use remove method
# """
# The remove method in lists removes the first occurrence of the specified value.
# """

fruits = ['apple', 'banana', 'cherry', 'banana']
fruits.remove('banana')
print(fruits)  # Output: ['apple', 'cherry', 'banana']

# """

# """
# # common dictionary methods

# # 1. dict.clear()
# # Removes all items from the dictionary.

my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}
my_dict.clear()
print(my_dict)  # Output: {}

# # 2. dict.copy()
# # Returns a shallow copy of the dictionary.

my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}
copy_dict = my_dict.copy()
print(copy_dict)  # Output: {'name': 'Alice', 'age': 25, 'city': 'New York'}

# # 3. dict.fromkeys(iterable, value=None)
# # Creates a new dictionary with keys from an iterable and values set to a specified value.

keys = ['name', 'age', 'city']
new_dict = dict.fromkeys(keys, 'unknown')
print(new_dict)  # Output: {'name': 'unknown', 'age': 'unknown', 'city': 'unknown'}

# # 4. dict.get(key, default=None)
# # Returns the value for a key if it exists, otherwise returns the default value.

my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}
print(my_dict.get('name'))  # Output: Alice
print(my_dict.get('country', 'USA'))  # Output: USA

# # Exercise 3
# # use the update method to change values in your age

my_dict = {
    'name': 'Asiimire',
    'age': 25,
    'city': 'New York'
}

# # Update the 'age' value using the update method
my_dict.update({'age': 26})

# # Print the updated dictionary
print(my_dict)  # Output: {'name': 'Asiimire', 'age': 120, 'city': 'New York'}

# Exercise 4: use if to check if the key (age) is present in the updated dictionary
# Initial dictionary
my_dict = {
    'name': 'Alice',
    'age': 25,
    'city': 'New York'
}

# Check if the 'age' key exists and update it if present, then return the value
if 'age' in my_dict:
    if my_dict['age'] < 30:  # Additional condition to spice it up
        my_dict.update({'age': 26})
        print("Age updated.")
    else:
        print("Age not updated because it does not meet the condition.")
else:
    my_dict.update({'age': 26})
    print("The key 'age' was not present, so it was added.")

# Print the value of 'age'
print(f"Current age: {my_dict['age']}")

# keys(), values() and items() methods

# # dict.items()
# # Returns a view object that displays a list of a dictionary's key-value tuple pairs.

# The keys() method returns a view object that displays a list of all the keys in the dictionary.
# The values() method returns a view object that displays a list of all the values in the dictionary.
# The items() method returns a view object that displays a list of a dictionary's key-value tuple pairs.

my_dict = {'name': 'Alice', 'age': 25, 'city': 'New York'}
print(my_dict.items())  # Output: dict_items([('name', 'Alice'), ('age', 25), ('city', 'New York')])

# Initial dictionary
student_info = {
    'name': 'Asiimire',
    'age': 25,
    'city': 'New York',
    'course': 'Physics'
}

# Update the 'course' value and add a new 'whatsapp' key
student_info.update({
    'course': 'Mathematics',
    'whatsapp': '+256758969973'
})

# Print the updated dictionary
print(student_info)

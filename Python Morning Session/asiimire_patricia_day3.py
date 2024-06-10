# Define the range of numbers
numbers = range(1, 11)

# Use dictionary comprehension to create the dictionary
cubes = {num: num**3 for num in numbers}

# Convert the dictionary to a list of tuples (key, value)
dict_to_tuples = list(cubes.items())

# Convert the cube values in the dictionary to a list of tuples
cubes_to_tuples = [(value,) for value in cubes.values()]

# Print the results
print("Dictionary converted to list of tuples:")
print(dict_to_tuples)

print("\nList of tuples from cube values in the dictionary:")
print(cubes_to_tuples)


# Exercise
# Create a reverse of the input 12345 to be 54321, while loop

# Input number
number = 12345

# Initialize the reversed number to 0
reversed_number = 0

# Use a while loop to reverse the digits of the number
while number > 0:
    # Get the last digit of the current number
    digit = number % 10
    # Append the digit to the reversed number
    reversed_number = reversed_number * 10 + digit
    # Remove the last digit from the current number
    number = number // 10

# Print the reversed number
print("Reversed number is:", reversed_number)

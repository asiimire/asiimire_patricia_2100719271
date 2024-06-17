# Defining Functions

# Function syntax and parameter
# Return value
# Lambda functions

# Functions i python are defined using the 'def' keyword, followed by function name then parentheses()
# inside parentheses you put a parameter name and the colon

# Example 1:
def multiply(a, b):
    return a * b

result = multiply(5,10)
print(result)

# Example 2: Multiple return values
def get_coordinates():
    return 10, 20

x, y = get_coordinates()
print(x, y)

# Exercise 1:
# Define a function greet with a parameter name, set to 'Guest', and print the message 
# I am a software engineer
def greet(Guest = "Asiimire"):
    print (f"I am a software engineer")

print(greet('Asiimire'))  

# Example 3: Return name and position
def get_name_and_position():
    name = "Patricia Asiimire" 
    position = "I am a software engineer"
    return name, position

name, position = get_name_and_position()
print(name, position)

# Exercise 4: Return multiple return values of your name and age
def get_name_and_age():
    name = "Patricia Asiimire" 
    age = 30
    return name, age

name, age = get_name_and_age()
print(name, age)

"""_summary_

def: Keyword to define a function
function_name: Name of the function
parameters: Optional, argument passedto the function
Docstrings: Optional, describes the function purpose
return: Optional , returns a value from the function

"""
# Lambda function
# Lambda function are small anonymous functions defined using the lambda keyword,
# they are restricted to a single expression

# Syntax for lambda function
# lambda parameter: expression

# Example 4: Cretae a lambda function to add two numbers
add = lambda a, b : a + b
print(add(45,70))

# Example 5: Use cases of lambda function for sorting
coordinates = [(1,2), (2,3), (3,1), (5,0)]
coordinates.sort(key=lambda coordinate: coordinate[1])
print(coordinates)

# Map, Filter and Reduce
# Example 6:
# Get the squres of 1 to 5 using map, filter, reduce

number_squares = [1, 2, 3, 4, 5] 
squares = list(map(lambda x: x**2, number_squares))
print(squares)

# Exercise 5:
# Define a function to get user info that accepts arbitrary keyword arguments and prints each key value pair
def bsse_student(**student):
    for key, value in student.items():
        print("Students: " + f"{key} : {value}")

bsse_student(fname = 'Asiimire', lname = "Patricia")

# Example 7:
def my_function(a,b, **kwargs):
    print(f"a: {a}, b: {b}")

    for key, value in kwargs.items():
        print(f"{key}:{value}")

my_function(1,2, x=100,y=200,z=300)        
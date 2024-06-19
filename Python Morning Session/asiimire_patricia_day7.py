# Example 1: syntax: Create a class where a dog inherits from animal and overrides

class Animal:
    def __init__(self, name):
        self.name = name
    
    def speak(self):
        return "An animal speaks in its own way."

class Dog(Animal):
    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed
    
    def speak(self):
        return "Woof!"

# Creating an instance of Dog
my_dog = Dog("Buddy", "Golden Retriever")

# Printing some information about the dog
print(f"My dog's name is {my_dog.name}.")
print(f"It is a {my_dog.breed}.")
print(f"And when it speaks, it says: '{my_dog.speak()}'")

# Polymorphism
# 
# Method Resolution Order (MRO) determines the sequence in which methods are resolved
# in a class hierarchy, especially in cases of inheritance involving multiple parent
# classes.

# How polymorphism works in python

# Exercise 1: create a simple application to manage different tyoes of vehicles.
# Implement derived class to demonstate inheritance and polymorphism
"""
Requirements
1. Base class to be vehicle
Attributes: make, model and year
method: display_info(print()

2. Derived class
Car: inherits from vehicle
Attributes: number_of_doors
Override: display_info(print()

Motorcycle: inherits from vehicle
Attributes: type_of_bike (cruiser, sport, touring)
override: display_info()
# Exercise 2: create a function that accepts a list of vehicle objects and
# call their display_info() memthod to print details of each vehicle object

"""

# Solution to Exercise 2

# Define the base class Vehicle
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
    
    def display_info(self):
        print(f"Make: {self.make}, Model: {self.model}, Year: {self.year}")

# Define the derived class Car
class Car(Vehicle):
    def __init__(self, make, model, year, number_of_doors):
        super().__init__(make, model, year)
        self.number_of_doors = number_of_doors
    
    def display_info(self):
        super().display_info()
        print(f"Number of doors: {self.number_of_doors}")

# Define the derived class Motorcycle
class Motorcycle(Vehicle):
    def __init__(self, make, model, year, type_of_bike):
        super().__init__(make, model, year)
        self.type_of_bike = type_of_bike
    
    def display_info(self):
        super().display_info()
        print(f"Type of bike: {self.type_of_bike}")

# Function to accept a list of vehicle objects and display their info
def display_vehicle_info(vehicles):
    for vehicle in vehicles:
        vehicle.display_info()
        print()  # Add a blank line between each vehicle's info for clarity

# Example usage
if __name__ == "__main__":
    # Create instances of vehicles
    vehicles = [
        Car("Toyota", "Camry", 2023, 4),
        Motorcycle("Harley-Davidson", "Sportster", 2022, "Cruiser"),
        Car("Honda", "Civic", 2021, 4),
        Motorcycle("Ducati", "Panigale V4", 2023, "Sport")
    ]

    # Display information of all vehicles
    display_vehicle_info(vehicles)

# Reading and Writing files in python
"""
Working with text files
Handling csv files
JSON and XML file processing
"""
# Working with text files
# Note: Python provides in-built functions to handle text files
# Key concepts:
"""
__description
"""
file_path = 'pat.txt'

# Example 3: write to a file and read a file ('w')
# writing to a text file
with open('pat.txt', 'w') as file:
    file.write('Hello, this is a pat.\n')
    file.write('I love python.\n')
    file.write('I use it for web development.')
# reading from a text file
with open('pat.txt', 'r') as file:
    content = file.read()
    print(content)

# Handling csv files
"""
CSV comma separated values, widely used for data exchange

Key concepts:
Reading csv files: use csv.reader()
Writing csv files: use csv.writer()
DictReader and DictWriter: read and write csv files as dictionaries
"""

# Example 4: Writing and reading csv files
import csv
# writing to a csv file
with open('pat.csv', 'w', newline='') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['name', 'position','course'])
    writer.writerow(['Pat', 'Student', 'BSSE'])
    writer.writerow(['Asiimire', 'Student', 'BSSE'])
# read from csv file
with open('pat.csv', 'r') as csv_file:
    reader = csv.reader(csv_file)
    for row in reader:
        print(row)
# JSON and XML file processing
"""
JSON- JavaScript Object Notation
XML- eXtensible Markup Language
Are used to structure data (usd for storing and exchanging data between systems)
""" 
# Key concepts:
# loading JSON data using json.load() for reading a json file 
# dumping JSON data using json.dump() for writing a json file 
# parsing JSON data using json.loads() for handling a json strings

# Example 6: Write and read json file
import json
# writing to a json file
student_data = {
    'name': 'Pat',
    'course': 'bse',
    'year': 'year 3'
}

# open the file
with open('student_data.json', 'w') as json_file:
    json.dump(student_data, json_file)

# reading json file
with open('student_data.json', 'r') as json_file:
    student_data = json.load(json_file)
    print(student_data)

# Exercise 2: write and read the xml file
import xml.etree.ElementTree as ET

# Function to write data to an XML file
def write_to_xml(filename):
    # Creating root element
    root = ET.Element("data")

    # Creating child elements
    item1 = ET.SubElement(root, "item")
    item1.set("name", "item1")
    item1.text = "Item 1 description"

    item2 = ET.SubElement(root, "item")
    item2.set("name", "item2")
    item2.text = "Item 2 description"

    # Creating XML tree
    tree = ET.ElementTree(root)

    # Writing tree to file
    with open(filename, "wb") as fh:
        tree.write(fh)

    print(f"Data has been written to {filename}")

# Function to read data from an XML file
def read_from_xml(filename):
    # Parsing XML file
    tree = ET.parse(filename)
    root = tree.getroot()

    # Accessing elements and attributes
    for child in root:
        print(f"Name: {child.attrib['name']}, Description: {child.text}")

# Usage example
if __name__ == "__main__":
    filename = "data.xml"
    
    # Write to XML file
    write_to_xml(filename)
    
    # Read from XML file
    read_from_xml(filename)


# Exercise 3: using abstraction calculate the area and perimeter of a rectangle
class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def calculate_area(self):
        return self.length * self.width
    
    def calculate_perimeter(self):
        return 2 * (self.length + self.width)

if __name__ == "__main__":
    # Taking user input for dimensions
    length = float(input("Enter the length of the rectangle: "))
    width = float(input("Enter the width of the rectangle: "))
    
    # Creating a Rectangle object
    rectangle = Rectangle(length, width)
    
    # Calculating area and perimeter
    area = rectangle.calculate_area()
    perimeter = rectangle.calculate_perimeter()
    
    # Displaying the results
    print(f"Area of the rectangle: {area}")
    print(f"Perimeter of the rectangle: {perimeter}")

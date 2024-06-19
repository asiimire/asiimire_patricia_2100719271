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

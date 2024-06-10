"""
Control Structures
Loops (for, while)
Comprehensions (list, dictionary,Comprehentions)
"""
age = 31
if age<18:
    print("You are not an adult")
elif age > 65:
    print("You are senior citizens")
else:
    print("You are a youth ")

grade = 88 

if grade>=90:
    print("A")
elif grade>=80:
    print("B")
elif grade>=70:
    print("C")
elif grade>=60:
    print("D")
else: 
    print("Not good grade")


"""
children under 13 get discount for price = shs 1000
Teenagers between 13 and 18 get discount for price = shs 500
Adults above pay full price = shs 2000
otherwise senior citizen pay full price = shs 5000
"""
age = int(input("what is your age: "))
price = 2000

if age >=60:
    print(price + 3000)
elif age >= 18:
    print(price)
elif age >= 13:
    print(price-500)
else:
    print(price-1000)

#loops (for, while)
"""
for loop iterates over a sequence (list, tuple , dictionary,set string)
the while loop repeates as long as  a condition is met
"""

# Example 

cars = ['Tesla', 'Audi', 'BMW','jeep','RangRover']

for car in cars :
    print(car)

#Example 4 count 1 t0 10

count = 1
while count <= 10:
    print("count 1 to 10", count)
    count +=1

#Exercise 
"""
1.Create your own list of favorite colors using for loop
"""

# List of favorite color
favorite_colors = ["blue", "green", "red", "purple", "yellow"]

# Empty list to store the result
colors_list = []

# Using a for loop to iterate over the favorite colors and add them to the colors_list
for color in favorite_colors:
    colors_list.append(color)

# Print the resulting list
print("My favorite colors are:", colors_list)

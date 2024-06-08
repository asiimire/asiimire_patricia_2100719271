# 7th June Morning session

    # if statements
# Prompt the user to enter their age
age = int(input("Enter age: "))
# print(f"age: {age}")

# Determine the ticket price based on age
if age < 13:
    price = 1000  # Price for children under 13
elif 13 <= age < 18:
    price = 1500  # Price for teenagers between 13 and 18 (2000 - 500 discount)
elif age >= 60:
    price = 5000  # Price for senior citizens 60 and above
else:
    price = 2000  # Price for adults 18 to 59

# Print the ticket price
print(f"The ticket price is: shs {price}")

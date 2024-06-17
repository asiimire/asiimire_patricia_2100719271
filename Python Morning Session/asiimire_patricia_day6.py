#Error Handling
#Exceptions handling with try,except,else,and finally
#Custom Exceptions

""" 
    NOTES
    Error Handling- Helps handle unexpected situations and errors.

    1.Try: contains code that might throw an exception
    NB: If an exception occurs the rest of the code in the try block is skipped or ignored

    2. Except : Catches and handles exceptions.
     - You can specify different handlers for different actions
    
    3. Else: The code runs if no exception occurs
    if no exceptions are raised in the try block it runs

    4. Finally: It runs whether an exception is raised or not




    More :
    try/except
        catch and recover from exceptions raised by Python, or by you.
    try/finally
        Perform cleanup actions, whether exceptions occur or not.
    raise
        Trigger an exception manually in your code.
    assert
        Conditionally trigger an exception in your code.
    with/as
        Implement context managers in Python 2.6, 3.0, and later (optional in 2.5).

 """

#Example 1: Handle exception with division by zero

try:
    number = int(input("Enter number : "))
    result = 20/number
except ValueError:
    print("Invalid number input! Enter valid number")
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print(f"Result is {result}")


# Example 2: Handle multiple exceptions
try:
    number = int(input("Example 2: Enter number: "))
    result = 20 / number
except ValueError as valueError:
    print("Invalid number input! Please enter a valid number.")
    print(f"ValueError: {valueError}")
except ZeroDivisionError as zeroError:
    print("Division by zero is not allowed! Please enter a non-zero number.")
    print(f"ZeroDivisionError: {zeroError}")
else:
    print(f"Result is {result}")

# #Exercise 1: Write a function that converts a string to an integer and handle both valueError
# #If the string can not be converted to an integer and the typeError if the input is not a string
# #Use multiple except block to handle these exceptions

# print("Exercise 1")
def convert_to_integer():
    try:
        number = int(input("Enter string value: "))
    except ValueError as valueError:
        print("Invalid number input! Please enter a valid number.")
        print(f"ValueError: {valueError}")
    except TypeError as typeError:
        print("Please enter a string")
        print(f"ValueError: {typeError}")
        
    else:
        print(f"Result is {number}")

# convert_to_integer()

# #Example 3: Custom exceptions
class insufficientFundsError(Exception) : 
    def _init_(self,balance,amount) :
        self.balance =balance
        self.amount = amount
        self.message = f"attempt to withdraw {self.amount} with only {self.balance}in account"
        super() ._init_(self.message)
        

def withdraw(balance,amount):
    if amount > balance :
        raise insufficientFundsError(balance, amount)
        return (balance - amount)
    
# # Custom exceptions handling

try :
    balance = 20000
    amount_to_withdraw = 100000
    new_balance = withdraw(balance, amount_to_withdraw)
except insufficientFundsError as e:
    print(f"Error: {e.message}")
else:
    print(f"New balance is {new_balance}")
finally:
    print("Transaction completed")
    
# #Exercise 2: Create a custom exception InvalidAgeError and write a function that raises this excedption if the given age is negative. Handle this custom exception when calling the function


class InvalidAgeError(Exception):
    def _init_(self, age):
        self.age = age
        self.message = f"Invalid age {self.age}. Enter a valid age input."
        super()._init_(self.message)
        # Super()
        # calling
        # initializing parent class constructor
        

def check_age():
    age = int(input("Enter your age: "))
    if age < 0:
        raise InvalidAgeError(age)
    else:
        print(f"Age is {age}")

try:
    check_age()
except InvalidAgeError as e:
    print(e.message)
else:
    print("Valid age entered.")
finally:
    print("Age check complete.")
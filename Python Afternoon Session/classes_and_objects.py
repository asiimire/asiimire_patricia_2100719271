#CLASSES AND OBJECTS


#CLASSES
# a class is a blueprint for creating objects
# use keyword class
# init (Constructor)
# init function is a special method called when an object is created
# init can be used to initialize attributes
# self refers to the current object being created

#Efrata
def adde(th): # declaring a method outside of the class
        print( "hello " )
        
class Employee:
    go = adde
    
    Department = "Finance" #common attribute to all objects
    
    #pass ...if class attributes are not declared
    
    def __init__ (self, name, age):
        self.name = name
        self.age = age
        
    def displaydetail(agg):
        print(agg.name + " " + str(agg.age))

#Stacey
    @classmethod
    def myfunc2(cls):
        print("this is my class method")    

    @staticmethod
    def myfunc3():
        print("this is my static method")       
#@classmethod and @staticmethod are decorators that modify the behavior of methods within a class.
#When a method is decorated with @classmethod, it becomes a class method.
#A class method receives the class itself as its first parameter, conventionally named cls.



#When a method is decorated with @staticmethod, it becomes a static method.
#Static methods do not receive any implicit first parameter (neither self nor cls).
#They can be called on the class itself or on an instance of the class.
       
       #the __str__() method is a special method that controls how an object is represented as a string
        #if __str__ function is not set returns string representation of the object 
        # <__main__.Employee object at 0x00000277BC2564E0> class name and memory location
        
    def __str__(this):
        return f"Employee(name is {this.name}, their age is {this.age})"
    # f string provides readable way to format a string
    
    #Cyiza
    def __str__(emp3):
     return f" name is {emp3.name} , age is {emp3.age}"
        
        #classes and other blocks of code including functions and loops are defined by indentation
        # rather than explicit keywords or braces
        #When the indentation decreases, the block is considered to have ended
        
    print()
        
    print("Employee Details")
    print("__________________")
    print()
    
    # Asiimire Patricia
 # Creating objects 
 
 # Change the class attribute (Setting the Attribute Directly on the Class):

# Employee.Department = "HR"


Emp1 = Employee( "Celine", 54)
Emp2 = Employee("Benson" , 25)
Emp3 = Employee("Terry" , 28)
Emp4 = Employee("Roman", 38)
# Change the class attribute (Setting the Attribute on an Instance)
Emp1.Department = "Sales" 

#accessing objects and attributes   
print("first Employee name:" + " " + Emp1.name + " " + "and age is" + " " + str(Emp1.age))

print()
#or

print(Emp1 , " " , Emp1.Department)
print(Emp2 , " " , Emp2.Department)
print()
print(Emp3)
print()

# #Yusuf
# Emp4.displaydetail()
# Emp1.age = 42 #modifying age of object Emp1 to 42
# # del Emp1  deleting object and del Emp1.age to delete object property
# # del Emp1.age

# print(str(Emp1.age) + " " + Emp1.name)

# #Victoire
# Emp4.go() #calling method from outside the class
# Emp4.status= "hired" #setting a unique attribute for an object
# print(Emp4.status, Emp4.name)

# Employee.myfunc2()
# Employee.myfunc3()
# Emp4.myfunc3()

# #you can also change the value of the property of the object
# Emp4.name="Mark"
# print(Emp4.name)
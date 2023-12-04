# example 1.

class calculator:
    num = 100 # Class variable
    def getData(self):
        print("I am now executing as method in class")

# Syntax to create objects in python.
obj=calculator() # object class
obj.getData() # object method
print(obj.num) # object variable

# example 2. create with constructor

class calculator:
    num = 100 # Class variable

#  default constructor
    def __init__(self):
        print('I am called automatically when object is created')
    def getData(self):
        print("I am now executing as method in class ")
obj=calculator()
obj.getData()
print(obj.num)

# Example 3

class person:

    def __init__(self, name):
        self.name=name
    def say_hi(self):
        print("My name is : ", self.name)

obj=person('Anitha')
obj.say_hi()

# Example 4

class person:

    def __init__(self, name):
        self.name=name
    def say_hi(self):
        print("My name is : ", self.name)

obj1=person('Anitha')
obj2=person("Aruna")
obj3=person("Rama")
obj1.say_hi()
obj2.say_hi()
obj3.say_hi()

# Example 5..

class calculator:
    num = 200

    def __init__(self, a, b): # default constructor
        self.Firstname = a # Instance Varaible
        self.Secondname = b
        print("I am called automatically shen object is created")

    def getData(self):
        print("I am now executing as method in class")

    def summation(self):
        return self.Firstname+self.Secondname+calculator.num


obj = calculator(2, 3)
obj.getData()
print(obj.summation())

obj1 = calculator(16, 2)
obj1.getData()
print(obj1.summation())
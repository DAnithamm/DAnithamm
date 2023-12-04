# What is print Statment & How to print line by line?
# A print statement executed by any data with single & double quotes line by line.
# Examples
'''print('Hello world') # with single quotes string o/p : Hello world
print("hello world") # with double  quotes string o/p :hello world
print("0-----") # Any data o/p: 0-----
print("|||||    ") # any special letters and space also o/p: |||||
print('*' * 10) # String and operation types o/p: **********'''


'''# 2.How to store value in veriables?
#example1
Price=10
rating=4.9
Name= 'Ani'
is_published = True
#example2
# We check in a patient named John Smith. He's 20 years old and is a new patient.?
Patient_name = 'John Smith'
Age =20
is_new = True'''

# How to receive input from user under terminal ?


String = 'ASTRING'

# Using slice constructor
#s1 = slice(3)
s2 = slice(1, 5, 2)
#s3 = slice(-1, -12, -2)

print("String slicing")
#print(String[s1])
print(String[s2])
#print(String[s3])

# Python program to demonstrate
# string slicing

# String slicing
String = 'GEEKSFORGEEKS'

# Prints string in reverse
print(String[::-2])

s = "Geeksforgeeks"
str = ''
def reverse(s):
    for i in s:
        str = i + str
    return str

print("The original string is : ", end="")
print(s)

print("The reversed string(using loops) is : ", end="")
print(reverse(s))










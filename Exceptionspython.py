
#ItemIncart = 0

#if ItemIncart != 2:#raise Exception("product cart count not matching") #Exception: product cart count not matching
 #   pass
#assert (ItemIncart!=2)

#dic={"Red", "Green", " Broccoli", "Blue", "Banana", "Yellow", "Carrot", "Orange", "Spinnach"}


'''data = ['Red','Apple','Green','Broccoli','Blue','Banana','Yellow','Carrot','Orange','Spinach']

user_input = input('Please give input which type you want to select 1. Fruits 2. Veg 3. Colors ')
if user_input == "1":
    print("Colors:")
    print('Red')
    print('Apple')
    print('Banana')
    print('Orange')
elif user_input == "2":
    print("Vegetables:")
    print('Broccoli')
    print('Carrot')
    print('Spinach')
elif user_input == "3":
    print("Colors:")
    print('Red')
    print('Blue')
    print('Green')
    print('Yellow')
else:
    print("you have entered invalid input")'''

data = ['Red','Apple','Green','Broccoli','Blue','Banana','Yellow','Carrot','Orange','Spinach']

user_input = input('Please give input which type you want to select 1. Fruits 2. Veg 3. Colors ')
if user_input == "1":
    print("Friuts:")
    print('Apple')
    print('Banana')
    print('Orange')
elif user_input == "2":
    print("Vegetables:")
    print('Broccoli')
    print('Carrot')
    print('Spinach')
elif user_input == "3":
    print("Colors:")
    print('Red')
    print('Blue')
    print('Green')
    print('Yellow')
else:
    print("Fruits:")
    print('Apple')
    print('Banana')
    print('Orange')
    print()
    print("Vegetables:")
    print('Broccoli')
    print('Carrot')
    print('Spinach')
    print()
    print("Colors:")
    print('Red')
    print('Blue')
    print('Green')
    print('Yellow')
# List
Values= [1, 2, "rahul", 4, 5]
print(Values[0]) # 1
print(Values[-1]) #5
print(Values[1:3]) # [2, 'rahul']
Values.insert(4, "shetty")
print(Values) #[1, 2, 'rahul', 4, 'shetty', 5]
Values.append("End")
print(Values) # [1, 2, 'rahul', 4, 'shetty', 5, 'End']
# updating
Values[4] = "SHETTY"
print(Values) #[1, 2, 'rahul', 4, 'SHETTY', 5, 'End']

del Values[2]
print(Values) # [1, 2, 4, 'SHETTY', 5, 'End']

# TUPLE
'''Val = (1, 2, "rahul", 4.5)
print(Val[1])
Val[2] = "RAHUL"
print(Val) # 'tuple' object does not support item assignment'''

Val = [1, 2, "rahul", 4.5]
print(Val[1])
Val[2] = "RAHUL"
print(Val) #[1, 2, 'RAHUL', 4.5]

#Dictionary

dic = {"a": 3, 4: "abc", "c": "hello world"}
print(dic["c"])
print(dic[4])
 # How to create dictionary at run time and data into it?

dict = {}
dict["firstname"] = "Rahul"
dict["lastname"] = "Shetty"
dict["gender"] = "Male"
print(dict)
print(dict["firstname"])




def reverse_case_in_words(input_str):
    words = input_str.split()
    reversed_case_words = [word.swapcase() for word in words]
    output_str = ' '.join(reversed_case_words)
    return output_str

input_str = "This is my World"
output_str = reverse_case_in_words(input_str)
print(output_str)



def reverse_first_char_case(input_str):
    words = input_str.split()
    reversed_case_words = [word[0].swapcase() + word[1:] for word in words]
    output_str = ' '.join(reversed_case_words)
    return output_str

input_str = 'This is my World'
output_str = reverse_first_char_case(input_str)
print(output_str)


 #Swap Two Elements in a List using comma assignment

#list = [23, 65, 19, 90]
#pos2, pos4 = 2, 4
'''
def swapPositions(list, pos2, pos4):
    list[pos2], list[pos4] = list[pos4], list[pos2]
    return list
print(swapPositions(list, pos2-1, pos4-1))

# 3 Reverse list slicing method

list = [1, 2, 3, 4, 5]
def revesre_list(list):
    new_list= list[::-1]
    return new_list
print(revesre_list(list))

# 4.Reverse Array using the reversed() and reverse() built-in function

lst = [9, 8, 7, 6, 5, 4, 3, 2, 1]
lst.reverse()
print(lst)
#print(list(reversed(lst)))'''

#Get the Length of a List in Python using len()
'''
list = [1, 3, 4, 5]
n = len(list)
print(n)

lst = [1, 2, 33, 44, 5, 6]
s = 0
for i, a in enumerate(lst):
    s += 1
print(s)
lst = [1, 9, 8, 4, 9, 2, 9]
value=9
def remove_element(begin,oldlist,value,newlist):
  if begin==len(oldlist):
    return newlist
  if value !=oldlist[begin]:
    newlist.append(oldlist[begin])
  return remove_element(begin+1, oldlist, value, newlist)
result = remove_element(0, lst, value, [])
print(result)'''




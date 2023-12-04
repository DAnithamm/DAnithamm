'''a = ''
data = "hI Dear"
for each in data:
    if each == ' ':
        a+=' '
    if each.islower():
        a+=each.upper()
        continue
    elif each.isupper():
        a+=each.lower()
        continue
print(a)'''


original_string = "This is MY World"
reversed_string = ' '.join(word[::-1]for word in original_string.split())
print(reversed_string)

str = "Rama is"
str_rev = " "
for x in reversed(str):
    str_rev += x
print(str_rev)

s = "Aruna"

# Using a for loop to print the reverse of the string
reverse_string = ""
for i in reversed(s):
    reverse_string += i

print(reverse_string)



def reverse_case_in_words(input_str):
    words = input_str.split()
    reversed_case_words = [word.swapcase() for word in words]
    output_str = ' '.join(reversed_case_words)
    return output_str

input_str = "This is MY World"
output_str = reverse_case_in_words(input_str)
print(output_str)


# Function to reverse a string
def reverse(string):
	string = string[::-1]
	return string

s = "Geeksforgeeks"

print("The original string is : ", end="")
print(s)

print("The reversed string(using extended slice syntax) is : ", end="")
print(reverse(s))



# test_your_code.py
import pytest

@pytest.fixture
def setup_data():
    data = {'key': 'value'}
    return data

def test_data_exists(setup_data):
    assert 'key' in setup_data

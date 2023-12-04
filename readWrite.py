file = open("text.txt")
#print(file.read())   # print the all content of text file
#print(file.read(5))   # Print n number of characters by passing parameter

#print one single line at a time readline()

#print(file.readline())
#print(file.readline())

#print line by line using readline method
# differance b/t readline() and readlins()

# exp 1
#line = file.readline()
#while line!= "":
 #   print(line)
  #  line = file.readline()
#example 2

for line in file.readlines():
    print(line)

file.close()


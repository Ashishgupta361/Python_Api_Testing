file = open("test.txt")
# Read all contents of file
# file.read()
#print(file.read())

# read n number of characters by passing parameter
#print(file.read(2))

# read one single line using readline method
#print(file.readline())

# print line by line using read line
# line = file.readline()
#
# while line != "":
#     print(line)
#     line = file.readline()

# readlines method work like read but save values in a list
for line in file.readlines():
    print(line)

file.close()
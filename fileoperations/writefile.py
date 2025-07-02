# file = open("test.txt")
#
# file.close()

# In place of open and close in different lines we can use below format to write the same in one line.
#with open('test.txt') as file:

# to open in read mode pass 'r' and for write mode pass 'w'

# read the line and store all values in a list
# reverse the list
# write back to file
with open('test.txt','r') as reader:
    content = reader.readlines() # []
    reversed(content) # []
    with open("test.txt",'w') as writer:
        for line in reversed(content):
            writer.write(line)
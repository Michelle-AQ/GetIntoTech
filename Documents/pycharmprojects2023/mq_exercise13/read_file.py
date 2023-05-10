# Question 2
# slurping
with open('pelican.txt') as f:
    contents = f.read()
    print(contents)

# or:

with open('pelican.txt') as f:
    f = f.read()
    print(f)
    print(type(f))

# the returned data type is a string

# Write some code that will read the pelican.txt file into a list and then output the number of items within the list
with open('pelican.txt') as f:
    list = f.readlines()
    print(list)
    print(type(list))
    print(len(list))


# Use a loop to iterate over and print the contents of the file.

for i in open('pelican.txt'):
    print(i)
#  Before the .rstrip method (with blank spaces)

for i in open('pelican.txt'):
    print(i.rstrip())
#  After the .rstrip method


for i in open('pelican.txt'):
    print(i, end="")




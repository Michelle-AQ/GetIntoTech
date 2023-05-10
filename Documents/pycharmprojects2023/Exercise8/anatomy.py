#!/usr/bin/python

# Example Python script




import sys
# needed to access system-specific parameters and function

argc = len(sys.argv)
# argc - argument count variable
# len - returns the length of an object i.e. string
# sys.argv - a list of command line inputs (in the file/module)
# argv - argument vector

if argc > 1:
    print('Too many args')

else:
    where = 'World'
    print("Hello", where)


print('Goodbye from ' + sys.argv[0])
    # print goodbye from list of all the arguments

print('Goodbye from ' + sys.argv[1])

print('Goodbye from ' + sys.argv[2])

print('Goodbye from ' + sys.argv[3])



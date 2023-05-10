#!/usr/bin/python
# Exercise 11 - Homework

# Part A
Belgium = 'Belgium,10445852,Brussels,737966,Europe,1830,Euro,Catholicism,Dutch,French,German'
# define the length variable by using the 'len' count function for the 'Belgium' string variable
length = len(Belgium)
print(length)
print('-' * length)
# print length to see the length of the string in the output
# print the '-' multiplied by the established length of the string to match the length on a new row

# "\n" - new line? didn't work in code so taken out from print function.
# Is it because it is not defined as a string variable?


# Part B
Belgium_colon = Belgium.replace(',', ':')
# define a new variable which will comprise adding a method to the 'Belgium' variable - in this case '.replace'
# specify the string values we want to replace
print(Belgium_colon)
#  print to see the output

Belgium_as_list = Belgium.split(",")
print(Belgium_as_list)
Belgium_population = Belgium_as_list[1]
Brussels_population = Belgium_as_list[3]



# Part C
# define a new variable which will have the total population value for Belgium and another for the total population value for the Brussels population
# Belgium_population = 10445852
# Brussels_population = 737966
Belgium_and_Brussels = int(Belgium_population) + int(Brussels_population)
# define a new function for adding the numerical values together
print(Belgium_and_Brussels)
#  print to see the output (numerical total)

#  ---------------------- slicing the string? alternative method to add numbers- did not work
text1 = Belgium
Belgium_number = text1
text1 = (text1[8:16])
print(text1)

text2 = Belgium
Brussels_number = text2
text2 = text2[27:32]
print(int(text1) + int(text2))


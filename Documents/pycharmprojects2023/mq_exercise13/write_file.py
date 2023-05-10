# Question 1
# Creating pelican.txt file
with open('pelican.txt','w') as f:
    f.write("A wonderful bird is the pelican")
    f.write("\nHis bill holds more than his belican\n")

    lines = ["He can take in his beak,\n", "Enough food for a week,\n","But I'm damned if I see how the helican.\n"]
    f.writelines(lines)

# \n is required for line breaks for string variables - this makes the string easier to read.

# with - makes sure that when blocks go to an end, it will close the file down














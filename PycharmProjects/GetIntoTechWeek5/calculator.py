# simple calculator
# add subtract multiply divide

def add(num1, num2):
    return num1 + num2


# variadic function - takes a variable number of arguments
def add_many(*numbers):
    answer = 0
    for number in numbers:
        answer = answer + number # long hand
        # answer += number # short hand
    return answer

# for loops can work with collections i.e. number collection

# challenge
# create the other 3 functions in this file

# Step 1: create functions subtract, multiply, divide
# Step 2: use the main trick in this file and test your functions

# Step 1
def subtract(num1, num2):
    return num1 - num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

# Step 2
if __name__ == '__main__':
    print(add(1,1))
    print(subtract(8, 5))
    print(multiply(10, 10))
    print(divide(100, 50))





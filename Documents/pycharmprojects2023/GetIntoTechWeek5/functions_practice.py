# Create a function
def say_hello():
    print('Hello')
    print('Bonjour')
    print('Hola')
# The body of the function should be indented not outdented

def say_hello_to_someone(firstname, lastname='Unknown'):
    print(f'Hello {firstname}, {lastname}')
    print(f'Bonjour {firstname} {lastname}')
    print(f'Your last name is {lastname}')

def welcome(firstname, lastname, hobby):
    greeting_message = f'Welcome {firstname} {lastname}. Your hobby is {hobby}.'
    return greeting_message


print(__name__)
# this means the 'main' starting point of the file - the entry point to the program
# the 'main' trick
if __name__ == '__main__':
    me = 'Michelle'
    surname = 'Quaye'
    say_hello_to_someone(me, surname)

    # call a function that RETURNS something
    message = welcome(me, surname, 'music')

    print(message)
    print(message.upper())

    # Call a function
    say_hello()
    print("Something else goes here")
    # Hello
    # Bonjour
    # Hola

    say_hello_to_someone('Victoria', 'Lloyd')
    say_hello_to_someone('Sophie', 'Jenkins')
    say_hello_to_someone(firstname='Michelle')

# ---------------------------------------

me = 'Michelle'
surname = 'Quaye'
say_hello_to_someone(me, surname)

# call a function that RETURNS something
message = welcome(me, surname, 'music')

print(message)
print(message.upper())



# Call a function
say_hello()
print("Something else goes here")
# Hello
# Bonjour
# Hola

say_hello_to_someone('Victoria', 'Lloyd')
say_hello_to_someone('Sophie', 'Jenkins')
say_hello_to_someone(firstname='Michelle')
# Hello Victoria
# Hello Sophie
# Hello Michelle
# --------------
# Hello Victoria
# Bonjour Victoria
# Your last name is Lloyd
# Hello Sophie
# Bonjour Sophie
# Your last name is Jenkins
# Hello Michelle
# Bonjour Michelle
# Your last name is Unknown





import functions_practice, thursday

print('='* 40)
# module dot function name
functions_practice.say_hello()
# 'module' also just means python file
# this option returns EVERYTHING in the other file being called

print('='* 40)
print('My name is Thursday')
print(f'My name is {__name__}')

print('=' * 40)
julie_greeting = functions_practice.welcome('Julie', 'Dooley', 'Pilates')
print(julie_greeting)

print(functions_practice.welcome('Dan', 'Dooley', 'Football'))

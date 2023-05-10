import calculator, functions_practice
print(calculator.add(2,1))
print(calculator.subtract(10, 5))
print(calculator.multiply(20, 10))
print(calculator.divide(200, 50))






result5 = calculator.add_many(10, 20, 30)
print(result5)

# unpacking a single collection i.e. tuple - adding a *
my_info = 'Lisa', 'Simpson', 'playing the Saxophone'
greet = functions_practice.welcome(*my_info)
print(greet)


planets = {'Mercury': 57.91, 'Venus': 108.2, 'Earth': 149.597870, 'Mars': 227.94}
print(planets)
print(type(planets))

# while loops are only used in conditions - for this situation we'd use a 'for' loop as it is a collection
# that you already know enough to process

# for row_number, planet in enumerate(planets.keys(), 1):
#     print(row_number, planet, planets[planet])
# This only gives the names - not the numerical values/keys
#  enumerate returns the numbers - in rows, and you can choose the number it starts on

# for loop variable in collection:
    # loop body

# for key in planets.keys():
#     print(key)
#     print(planets[key])

for row_number, planet in enumerate(planets.keys(), 1):
    print("{:2d} Planet {:<10s} {:06.2f} Gm".format(row_number, planet, planets[planet]))
# slots correct placeholders in returned output
# 2d - means slot 2 characters, it's a format specifier 'd' means a whole number
# left hand bracket means left aligned
# :06.2f - the 2f '2 float' after the dot - meaning 2 decimal places, 6 places i.e. width for numbers

# literal string interpolation "f" in strings - another way of format specifying
# for row_number, planet in enumerate(planets.keys(), 1):
#     print(f"({row_number:2d} Planet {[str] Distance{[str]:06.2f} Gm".format(row_number, planet, planets[planet]))
    






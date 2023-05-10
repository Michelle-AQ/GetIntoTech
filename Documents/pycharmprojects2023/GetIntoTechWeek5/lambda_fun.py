numbers = [2, 5, 8, 4]
increased_numbers = list(map(lambda n: n + 1, numbers))
#  map functions work on collections and iterate through every item one at a time
# almost like a 'for' loop
# maps add functionailty to each list item

print(increased_numbers)
# [3, 6, 9, 5]

# long hand version of the n: n + 1 above
def increase_by_one(collection)
    for n in collection:
        n = n + 1
    return collection
# using a lambda uses less syntax




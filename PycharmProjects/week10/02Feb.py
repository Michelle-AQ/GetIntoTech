print('Victoria says "hi" to the class')
print("""Victoria's peas were gross and she said "yuck"!""")
# quotes within speech marks

word = "spam "
print(word, word, word, word)
print(word * 12)

sentence = """Victoria's peas were gross and she said "yuck"!"""
sentence_as_uppercase = sentence.upper()
print(sentence_as_uppercase)

gross = sentence.find('gross')
print(gross)

toria = sentence.find('toria')
print(toria)

not_there = sentence.find("yum")
print(not_there)
# methods go into objects - that differs it from functions

# + with numeric operands means add
# + with string operands means concatenate
# operator overloading


text = "hello world"
print(text.count('o'))

if text.startswith('hell'):
    print("It's hell in there")

if text.endswith('d'):
    print('string ends in d')

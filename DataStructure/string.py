# string: ordered, immutable, text representation

my_string = "Hello_word"
text = """Hello word
         I'm a full engineering"""

print(my_string)
print(text)

char = my_string[-1]
print(char)
print(my_string[0])

#reverse str
print(my_string[::-1])

greeting = "Hello"
name = "Tom"
teacher = "teacher Peter"

sentence = greeting + " " + name
print(sentence)

print(sentence.split())
print(sentence.startswith(greeting))
print(sentence.endswith(name))
print(sentence.capitalize())
print(sentence.upper())
print(sentence.lower())
print(sentence.count('He'))
print(sentence.replace(name, teacher))

sentence = "Hello every one. I'm John. I'm a butler and full engineering"
word = sentence.split()
sub_sentence = " ".join(word)
print(word)
print(sub_sentence)
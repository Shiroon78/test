# Regular expression in python

import re 

pattern = r"[a-z]+s"
text = '''A regular expression (regex or RE) is, in simple terms, a search pattern. It is a sequence of characters that defines a search pattern, similar to how a recipe defines the ingredients and instructions for a dish.

In Python, regular expressions are implemented using the re module. To use regular expressions in Python, you can import the re module and use it to create a regular expression object. You can then use this object to search for matches in a string.'''

# match = re.search(pattern, text)
# print(match)

matchs = re.finditer(pattern, text)

# for match in matchs:
#     print(match)


for match in matchs:
    print(match.span())
    print(match.span()[0])
    print(text[match.span()[0]:match.span()[1]])





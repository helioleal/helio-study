# Author: Helio Leal
# this program shows some string operations with python.

# you can use single or double quotes
astring = "Hello world!"
astring2 = 'Hello world!'

# the position of first 'o' in variable asstring
print(astring.index("o"))

# the position of first 'w' in variable asstring
print(astring.index("w"))

# Counts how many 'l'  there is in variable assstring
print(astring.count("l"))

# print a part of astring varible
print(astring[3:7])

# This prints the characters of string from 3 to 7 skipping one character. This is extended slice syntax. The general form is [start:stop:step].
print(astring[3:10:2])
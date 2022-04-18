# Introduction to Python strings

message = " This is a string in Python"
print(message)
message = 'This is also a string'
print (message)
#======================================================================================================

# When a string contains a single quote, you should put in double-quotes like this:
message = "It's a string!"
print(message)

# When a string contains double quotes, you can use the single quotes:
message = '"Inner Beauty is better than Inner ugly." Said the stranger.'
print(message)

# To escape the quotes, you use the backslash ( \ ). For example:
message = 'It\'s also a valid strin.'
print(message)

# Python interpreter wil treat the backslash character ( \ ) as special. If you don't want to do so,
# you can use raw strings by adding the letter 'r' before the first quote.
message = r'C:\python\bin'
print(message)
#======================================================================================================

# Creating multiple strings
help_message = '''
Usage: mysql command
    -h hostname
    -d database name
    -u username
    -p password
'''

print(help_message)
#======================================================================================================

# Using variables in Python strings with the f-strings
name = 'John'
message = 'Hi'
print(message, name)

#You can use the value of the name variable inside the message string variable.
# To do it, you place the letter 'f' before the opening quotation mark and
#put the brace '{}' around the variable name:
name = 'John'
message = f'Hi {name}'
print(message)

# Python will replace the {name} by the value of the 'name' variable.
# The 'message' is a format string, or f-string in short.
#======================================================================================================

# Concatenating Python strings. When you place the string literals next to eachother,
# Python automatically concatenates then into one string.
greeting = 'Good ' 'Morning!'
print(greeting)

# To concatenate two string variables, you use the operator '+'
greeting = 'Good'
time = ' Afternoon'

greetings = greeting + time + '!'
print(greetings)
#======================================================================================================

# Accesing string elements
# Since a string is a sequence of characters, you can acces it's elements using an index.
# The first character in the string has an index of zero.
str = "Python String"
print(str[0])
print(str[1])
print(str[8])
print(str[3])
print(str[4])
print(str[11])

# If you use a negative index, Python returns the character starting from the end of the string.
str = "Python String"
print(str[-6])
print(str[-11])
print(str[-4])
print(str[-3])
print(str[-8])
print(str[-1])
#======================================================================================================

# Getting the length of a string
str = "Python String"
str_len = len(str)
print(str_len)
#======================================================================================================

# Slicing strings. Slicing allows you to get a substring from a string.
# The syntax for slicing is as follows 'string[start:end]'
# The str[0:2] returns a susbstring that includes the character from index 0(incl.) to 2(excl.).
str = "Python Strings"
print(str[0:2])
#======================================================================================================

# Python strings are immutable
str = "Python String"
str[0] = 'J'
# This piece of code will return as error.

# When you want to modify a string, you need to create a new one from the existing string.
str = "Python String"
new_string = 'X' + str[1:]
print(new_string)

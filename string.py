# Introduction to Python strings

message = " This is a string in Python"
print(message)
message = 'This is also a string'
print (message)

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

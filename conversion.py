# Introduction  to type conversion in Python.
# To get an input from users, you use the 'input()' function.
value = input('Enter a value:')
print(value)
# When you ececute this code, it'll prompt you for an input on the Terminal.
# When you enter a value, the program will display the value back.
# However, the 'input()' function returns a string, not an integer.

# The next example prompts you for entering two input values.
price = input('Enter the price ($):')
tax = input('Enter the tax rate (%):')

net_price = price * tax / 100
print(f'the net price is ${net_price}')

# When you execute this code you will get an error. Because the input values are strings,
# you cannot apply the arithmetic operator '*' to them. To solve this issue, you need to convert the strings into numbers.
# To convert a string to a number, you use the 'int()' function. The 'int()' function converst the string to an integer.

price = input('Enter the price($):')
tax = input(' Enter the tax rate (%):')

net_price = int(price) - (int(price) * int(tax) / 100)
print(f'The net price is ${net_price}')
# ================================================================================================================

# Other types of conversion functions. Python supports other types of conversion functions, like;
# float(str) - converts a string to a floating-point number
# bool(val) - converts a value to a boolean value, either 'True' or 'False'.
# str(val) - returns the string representation of a value.

# Getting the type of a value. To get the type of a value, you use the type(value) function.
type1 = type(100)
type2 = type(2.0)
type3 = type('Python String')
type4 = type(True)
print(type1, type2, type3, type4)

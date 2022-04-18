# Integers are numbers such as -1, 0, 1, 2, 3 .. and the have type 'int'.
# You can use Math operators like +, -, * and / to form expressions that include integers.
sum1 = 20 + 10
sum2 = 20 - 10
sum3 = 20 * 10
sum4 = 20 / 10
print (sum1, sum2, sum3, sum4)

# To calculate exponents, you use two multiplication symbols.
sum = 4**4
print(sum)

# To modify the order of operations, you use the parentheses '()'.
sum = 20 / (10 + 10)
print(sum)
#======================================================================================================

# Floats. Any number with a decimal point is a floating-point numder.
# The term float means that the decimal point can appear at any position in a number.
sum1 = 0.5 + 0.5
sum2 = 0.5 - 0.5
sum3 = 0.5 * 0.5
sum4 = 0.5 / 0.5
print(sum1, sum2, sum3, sum4)

# The devision of two integers always returns a float.
sum = 20 / 10
print(sum)

# If you mix an integer and a float in any arithmetic operation, the result is a float.
sum = 1 + 2.5
print(sum)

# Due to the internal representation of floats, Python will try to represent the result as precisly as possible.
# However, you may get the result that you would not expect.
sum = 0.1 + 0.2
print(sum)
#======================================================================================================

# Underscores in numbers. When a number is long, it'll become difficult to read.
count = 1000000
print(count)

# To make the long number more readable, you can group digits using underscores '_'.
count = 100_000_000_000
print(count)

# The underscores also work for both integers and floats.

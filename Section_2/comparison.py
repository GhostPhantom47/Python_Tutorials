# Introduction to Python comparison operators. Python has six comparison operators;
# Less than ( < )
# Less than or equal to ( <= )
# Greater than ( > )
# Greater than or equal to ( >= )
# Equal to ( == )
# Not equal to ( != )
# These comparison operators compate two values and return a boolean value, either 'True' or 'False'.
# And you can use the comparison operators to compare both numbers(integers) and strings.

# Less than operator ( < )
comp1 = 10 < 20
comp2 = 30 < 20
print(comp1, comp2)

str1 = 'apple' < 'orange'
str2 = 'banana' < 'apple'
print(str1, str2)
# The result of this piece of code is Python will look at the first letter of the words and compares them
# with their place in the alphabeth.

# This is an example on how you can use the less than( < ) operator with variables.
x = 10
y = 20
sum = x < y
print(sum)
# ===========================================================================================================

# Less than or equal to ( <= )
comp1 = 20 <= 25
comp2 = 30 <= 30
comp3 = 30 <= 25
print(comp1, comp2, comp3)

x = 25
y = 24
comp1 = x <= y
comp2 = y <= x
print(comp1, comp2)
# ===========================================================================================================

#Greater than  operator ( > )
comp1 = 21456 > 1234483
comp2 = 215423 > 12345
print(comp1, comp2)

str1 = 'apple' > 'orange'
str2 = 'banana' > 'kiwi'
print(str1, str2)
# ===========================================================================================================

# Greater than or equal to ( >= )
comp1 = 123456 >= 1234587
comp2 = 458695 >= 1234587
comp3 = 123456 >= 123456
print(comp1, comp2, comp3)

str1 = 'apple' >= 'apple'
str2 = 'banana' >= 'orange'
str3 = 'lemon' >= 'lime'
print(str1, str2, str3)
# ===========================================================================================================

# Equal to operator ( == )
comp1 = 20 == 25
comp2 = 15 == 15
print(comp1, comp2)

str1 = 'apple' == 'apple'
str2 = 'orange' == 'apple'
print(str1, str2)
# ===========================================================================================================

# Not equal to operator ( != )
comp1 = 15 != 25
comp2 = 264 != 264
print(comp1, comp2)

str1 = 'apple' != 'orange'
str2 = 'banana' != 'banana'
print(str1, str2)

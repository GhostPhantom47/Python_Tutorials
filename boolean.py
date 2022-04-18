# Introduction to Python Boolean data type. In programming, you often want to check if a condition is
# true or not and perform some actions based on the result. To represent true or false,
# Python provides you with the boolean data type. The boolean value has a technical name as 'bool'.
# The boolean data type has two values: True and False. Note that both values start with capital letters.

# When you compare two numbers, Python returns the result as a boolean value.
sum1 = 20 > 10
sum2 = 20 < 10
print(sum1, sum2)

# Also comparing two strings results in a boolean value.
str1 = 'a' < 'b'
str2 = 'a' > 'b'
print(str1, str2)
#======================================================================================================

# The bool() function. To find out if  a value is True or False, you use the bool() function.
str1 = bool('Hi')
str2 = bool('')
str3 = bool(100)
str4 = bool(0)
print(str1, str2, str3, str4)

# Falsy and Truthy values. When a value is True , it's truthy and when False, it's falsy.
# The following are falsy values in Python
# The number zero '0'
# An empty string ''
# 'False'
# 'None'
# An empty list []
# An empty tuple ()
# An empty dictionary {} 

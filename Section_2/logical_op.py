# Introduction to Python logical operators. Somtimes you want to check multiple conditions at the same time.
# To do so, you use logical operators. Python has three logical operators;
# 'and' - checks wether two conditions are both 'True' simultaneously
# 'or' - checks both conditions and returns 'True' when either or both conditions are 'True'
# 'not' - applies to one condition. It reverses that condition, 'True' becomes 'False' and 'False' becomes 'True'.

# The and operator
price = 9.95
con1 = price > 9 and price < 10
con2 = price < 9 and price > 10
con3 = price > 9 and price > 10
con4 = price < 9 and price < 10
print(con1, con2, con3, con4)
# ===========================================================================================================

# The or operator

price = 9.95
con1 = price > 9 or price < 10
con2 = price < 9 or price > 10
con3 = price > 9 or price > 10
con4 = price < 9 or price < 10
print(con1, con2, con3, con4)
# ===========================================================================================================

# The not operator

price = 9.95
con1 = not price < 10
con2 = not price > 10
con3 = not price < 10
con4 = not price > 10
print(con1, con2, con3, con4)
# ===========================================================================================================

# Combinations of logical operators

price = 9.95
con1 = not (price > 10 and price < 9)
con2 = (price > 9 and price > 8) or (not price > 9 and price < 10)
con3 = (price > 9 and price > 8) and (not price > 9 and price < 10)
print(con1, con2, con3)

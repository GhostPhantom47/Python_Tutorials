# Python if Statement. The simple Python if statement.
# The if statement checks the condition first. If the condition evaluates to 'True',
# it executes the statement in the if-block. Otherwise it ignores the statement.
age = input('Enter your age: ')
if int(age) >= 18:
    print("You're eligible to drive a car.")

# In this example you see two messages after you enter a value greater than or equal to 18 ( >= ).
# Here indentation is important. Any statement that follows the 'if' statement needs to have four spaces.
age = input('Enter your age:')
if int(age) >= 18:
    print("You're eligible to drive a car.")
    print("Let's go for a ride.")

# Here you can see an example when you don't use the indentation right. Because the last line of code doesn't have
# indentation Python sees it as a stand-alone block instead of a part of the if block.
age = input('Enter your age: ')
if int(age) >= 18:
    print("You're eligible to drive a car")
print("Let's go for a ride.")
# ===========================================================================================================

# Python if...else statement
# Typically, you want to perform an action when a condition is 'True' and another action when the condition is 'False'.
# To do so, you use the 'if...else' statement.
age = input('Enter your age:')
if int(age) >= 18:
    print("You're eligible to drive a car.")
else:
    print("You're not eligible to drive a car.")
# ===========================================================================================================

# Python el..elif..else statement
# If you want to check multiple conditions and perform an action accordingly, you can use the 'if...elif..else' statement.
# The 'elif' stands for 'else if'.
age = input('Enter your age:')

# Convert the string to int
your_age = int(age)

# Determine the ticket price
if your_age < 5:
    ticket_price = 5
elif your_age < 16:
    ticket_price = 10
else:
    ticket_price = 18

# Show the ticket price
print(f"You'll pay ${ticket_price} for the ticket")

# Introduction to Python comments. Sometimes, you want to document the code that you write.
# You may want to note why a piece of code works. Typically, you use comments to explain formulas,
# algorithms and complex business logic.
# When executing a program, the Python interpreter ignores the comment and only interprets the code.
# Python provides three kinds of comments including block comment, inline comment and documentation string.
# ================================================================================================================
# Python block comments
# A block comment explains the code that follows it.
# Typically, you indent a block comment at the same level as the code block.
# To create a block comment, you start with a single hash '#' sign, followed by a single space and a text string.

# increase price by 5%
price = 25.5
price = price * 1.05
print(price)
# ================================================================================================================

# Python inline comments
# When you place a comment on the same line as a statement, you'll have an inline comment.
salary = 35 # per hour
hours = 40 # per week
weeks = 44 # per year
income = salary * hours * weeks # yearly income
print(income)
# ================================================================================================================

# Python docstrings
# A documentation string is a string literal that you put as the first lines in a code block. for example, a function.
# Unlike a regular comment, a documentation string can be accessed at run-time using 'obj.__doc__' attribute were
# obj is the name of the function.
# Typically, you use a documentation string to automatically generate the code documentation.
# documentation strings are called docstrings.

# One-line docstrings. One-line docstrings fits one line. A one-line docstring begins with tripple quotes (""")
# and also ends with tripple quotes("""). Also, there won't be any blank line either before or after the one-line docstring.
# The following example illustrates a one-line docstring in the 'quicksort()' function.
def quicksort():
    """ sort the list using quicksort algorithm """
...
# ================================================================================================================

# Multi-line docstrings. A multi-line docstring also starts and end with tripple quotes ("""). And can span multiple lines.
def increase(salary, percentage, rating):
    """ increase salary base on rating and percentage
    rating 1 - 2 no increase
    rating 3 - 4 increase 5%
    rating 4 - 6 increase 10%
    """
# ================================================================================================================

# Python multiline comments. Python doesn't support multiline comments.
# However, you can use multi-line docstrings as multiline comments. It's a good practice to keep your comment(s);
# clear, consise and explanatory. The ultimate goal is to save time and energy for you and other developers
# who will work on the code.

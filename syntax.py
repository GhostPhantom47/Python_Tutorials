# Whitespace and Indentation
def main():
    i = 0.5
    max = 15
    while (i < max):
        print (i)
        i = i + 1

# Call function main
main()
#-------------------------------------------------
# Continuation of statements
if (a == True) and (b == False) and (c == True):
   print("Continuation of statements")
#-------------------------------------------------
# Keywords in Python

import keyword

print(keyword.kwlist)
#-------------------------------------------------
# Strings literals
s = 'This is a string!'
t = "This is a string using double quotes!"
r = '''lThis string can span
        multiple lines '''

print(s,t,r)

#!/usr/bin/env python3
# example workign with Functions
#By Ed 10/11/21

# Define function here
def printme(mystr):
    "This prints a passed string"
    print(mystr)
    return 42

# Now lets call the function
printme("this is a test")
return_value = printme("Hello World")
print(return_value)


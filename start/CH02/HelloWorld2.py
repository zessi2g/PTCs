#!/usr/bin/env python3
# A simple "Hello World" script in python with Inputs
# Created by Ed on 9/29/21

# Suggestion, build out 1 line at a time
# Once multiple print statemetns exist, put a breakpoint at first print line
# Then walk through as an example of "debugging"

your_name = input("What is your name? ")
print(your_name)
print("Hello " + your_name)
print("Hello" , your_name)
message = "Hello " + your_name
print(message)
print("Hello {0}".format(your_name))
print(f"Hello {your_name}")

#!/usr/bin/env python3
# A simple calculator to show math and conditionals
# Created by Ed on 10/1/21

# Get information from user
first_number = input("What is the first number? ") 
activity = input("What activity? ( + - * / ) ")
second_number = int( input("What is the second number? ") )

# Do math
if activity == "+":
    new_number = first_number + second_number
    print(new_number)
if activity == "-":
    print(first_number - second_number)
if activity == "*":
    print(first_number * second_number)
if activity == "/":
    print(first_number / second_number)


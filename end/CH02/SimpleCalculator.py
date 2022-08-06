#!/usr/bin/env python3
# A simple calculator to show math and conditionals
# Created by Ed Goad, 2/3/2021

# Get inputs first
# Note we are casting the numbers as "float", we could also do "int"
firstNum = float(input("What is the first number: "))
activity = input("What activity? ( + - * / ) ")
secondNum = float(input("What is the second number: "))

# depending on the selected activity, perform an action
if activity == "+":
    print(firstNum + secondNum)
if activity == "-":
    print(firstNum - secondNum)
if activity == "*":
    print(firstNum * secondNum)
if activity == "/":
    print(firstNum / secondNum)

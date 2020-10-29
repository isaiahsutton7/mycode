#!/usr/bin/env python3

"""This is a calculator"""

def equation(x,y):
    sym= input("Would you like to +, -, /, or *? ")

    if sym== "+":
        print(x+y)
    elif sym== "-":
        print(x-y)
    elif sym== "*":
        print(x*y)
    elif sym== "/":
        print(x/y)

def main():
    num1= float(input("What is your first number? "))
    num2= float(input("What is your second number? "))
    
    equation(num1,num2) #call function to sub x,y with user input

main()

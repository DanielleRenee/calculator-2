"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *

def calculator():

    while True:
        user_input = raw_input("> ")
        tokens = user_input.split(" ")

        operator = tokens[0]
        num1 = tokens[1]
        num2 = tokens[2]

        if operator == "+":
            result = add(float(num1), float(num2))

        elif operator == "-":
            result = subtract(float(num1), float(num2))

        elif operator == "*":
            result = multiply(float(num1), float(num2))

        elif operator == "/":
            result = divide(float(num1), float(num2))

        elif operator == "square":
            result = square(float(num1))

        elif operator == "cube":
            result = cube(float(num1))

        elif operator == "pow":
            result = power(float(num1), float(num2))

        elif operator == "mod":
            result = mod(float(num1), float(num2))

        elif not num1.isdigit() or not num2.isdigit():
            print """Those aren't numbers! You broke me. 
Start over and enter an integer followed by two numbers."""
            break

        print result
    return result
calculator()

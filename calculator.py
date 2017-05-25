"""A prefix-notation calculator.

Using the arithmetic.py file from Calculator Part 1, create the
calculator program yourself in this file.
"""

from arithmetic import *

#def calculator():

while True:
    user_input = raw_input("> ")
    tokens = user_input.split(" ")

    if len(tokens) > 3:
        print "Please enter one operator followed by two numbers."
        continue

    elif len(tokens) < 3:
        print """Please enter an operator followd by two numbers.
Format example:  + 10 5 ."""
        continue
    
    operator = tokens[0]
    num1 = tokens[1]
    num2 = tokens[2]


    if not num1.isdigit() or not num2.isdigit():
        print """Those aren't numbers! You broke me. 
Start over and enter an operator followed by two numbers."""
        continue


    elif operator == "+":
        result = add(int(num1), int(num2))

    elif operator == "-":
        result = subtract(int(num1), int(num2))

    elif operator == "*":
        result = multiply(int(num1), int(num2))

    elif operator == "/":
        result = float(divide(int(num1), int(num2)))

    elif operator == "square":
        result = square(int(num1))

    elif operator == "cube":
        result = cube(int(num1))

    elif operator == "pow":
        result = power(int(num1), int(num2))

    elif operator == "mod":
        result = mod(int(num1), int(num2))

    print result
 #   return result
#calculator()

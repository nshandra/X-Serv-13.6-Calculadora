#!/usr/bin/python3
# NAZAR SHANDRA

import sys

if len(sys.argv) != 4:
    sys.exit("Usage: calculadora.py function operand1 operand2")


def to_float(input):
    try:
        return float(input)
    except ValueError:
        sys.exit(input + ": Value error.")

function = sys.argv[1]
operand1, operand2 = to_float(sys.argv[2]), to_float(sys.argv[3])

if function == "add":
    result = operand1 + operand2
elif function == "sub":
    result = operand1 - operand2
elif function == "mul":
    result = operand1 * operand2
elif function == "div":
    try:
        result = operand1 / operand2
    except ZeroDivisionError:
        sys.exit("Division by zero error.")
else:
    sys.exit("wrong function. Usage: add, sub, mul, div.")

operators = {"add": '+', "sub": '-', "mul": '*', "div": '/'}

print(operand1, operators[function], operand2, '=', result)

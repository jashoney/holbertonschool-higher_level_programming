#!/usr/bin/python3

import sys
from calculator_1 import add
from calculator_1 import sub
from calculator_1 import mul
from calculator_1 import div


def main(argv):
    if len(argv) != 4:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    a = int(argv[1])
    b = int(argv[3])
    if argv[2] == '+':
        print(f'{a} + {b} = {add(a, b)}')
    elif argv[2] == '-':
        print(f'{a} - {b} = {sub(a, b)}')
    elif argv[2] == '*':
        print(f'{a} * {b} = {mul(a, b)}')
    elif argv[2] == '/':
        print(f'{a} / {b} = {div(a, b)}')
    else:
        print("Unknown operator. Available operators: +, -, * and /")
        exit(1)


if __name__ == "__main__":
    main(sys.argv)

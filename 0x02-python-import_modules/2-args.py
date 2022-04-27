#!/usr/bin/python3

import sys


def main(argv):
    if len(argv) == 1:
        print("0 arguments.")
    elif len(argv) == 2:
        print(f'{len(argv) - 1} argument:')
    else:
        print(f'{len(argv) - 1} arguments:')
    for i in range(1, len(argv)):
        print(f'{i}: {argv[i]}')


if __name__ == "__main__":
    main(sys.argv)

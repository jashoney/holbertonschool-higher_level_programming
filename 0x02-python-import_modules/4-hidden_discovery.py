#!/usr/bin/python3

import sys
import hidden_4


def main():
    namelist = dir(hidden_4)
    for i in range(0, len(namelist)):
        name = namelist[i]
        if name[0] != "_":
            print(namelist[i])


if __name__ == "__main__":
    main()

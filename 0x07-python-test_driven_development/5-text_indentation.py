#!/usr/bin/python3
"""
prints text with newlines
no spaces at the start of each newline
"""


def text_indentation(text):
    """ prints text with newlines after a .? and : """

    newline = True
    if text is None:
        return
    elif type(text) is not str:
        raise TypeError("text must be a string")
    else:
        length = len(text)
        for i in range(length):
            if text[i] in (".", "?", ":"):
                print(text[i])
                print()
                newline = True
            else:
                if not newline:
                    print(text[i], end="")
                else:
                    if text[i] != " ":
                        newline = False
                        print(text[i], end="")

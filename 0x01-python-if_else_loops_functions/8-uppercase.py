#!/usr/bin/python3

def uppercase(string):
	newstring = ""
	for i in range(0, len(string)):
		if ord(string[i]) >= 97 and ord(string[i]) <= 122:
			newstring = newstring + chr(ord(string[i]) - 32)

		else:
			newstring = newstring + string[i]

	print(newstring)

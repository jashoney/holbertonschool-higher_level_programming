#!/usr/bin/python3
for i in range(0, 10):
	for j in range(i + 1, 10):
		if i == 8:
			print(i * 10 + j)
			break

		else:
			print(f'{(i * 10 + j):02}', end = ", ")


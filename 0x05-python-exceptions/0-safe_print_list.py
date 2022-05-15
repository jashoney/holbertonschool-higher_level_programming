#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    new_list = []
    for i in range(x):
        try:
            new_list.append(my_list[i])
            count = count + 1
        except:
            break
    print(*new_list, sep="")
    return (count)

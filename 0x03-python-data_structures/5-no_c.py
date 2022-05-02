def no_c(my_string):
    new_string = ""
    banned_list = ["c", "C"]
    for i in range(len(my_string)):
        if my_string[i] in banned_list:
            continue
        else:
            new_string = new_string + my_string[i]
    return (new_string)

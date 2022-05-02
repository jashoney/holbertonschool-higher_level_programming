def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) > 2:
        a = tuple_a[0]
        b = tuple_a[1]
    if len(tuple_a) == 2:
        a, b = tuple_a
    elif len(tuple_a) == 1:
        a = tuple_a[0]
        b = 0
    else:
        a = 0
        b = 0
    if len(tuple_b) > 2:
        c = tuple_b[0]
        d = tuple_b[1]
    if len(tuple_b) == 2:
        c, d = tuple_b
    elif len(tuple_b) == 1:
        c = tuple_b[0]
        d = 0
    else:
        c = 0
        d = 0
    new_tuple = (int(a) + int(c), int(b) + int(d))
    return (new_tuple)

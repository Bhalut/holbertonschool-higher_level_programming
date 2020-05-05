#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    x = tuple_a[0] if len(tuple_a) <= 2 and len(tuple_a) > 0 else 0
    x += tuple_b[0] if len(tuple_b) <= 2 and len(tuple_b) > 0 else 0
    y = tuple_a[1] if len(tuple_a) >= 2 and len(tuple_a) > 0 else 0
    y += tuple_b[1] if len(tuple_b) >= 2 and len(tuple_b) > 0 else 0
    add = (x, y)
    return add

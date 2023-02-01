list_1 = ['a', 'b', 'c']
list_2 = [1, 2, 3]


def is_alternate_extract(list_1, list_2):
    list_0 = [None] * (len(list_1) + len(list_2))
    list_0[::2] = list_1
    list_0[1::2] = list_2
    print(list_0)


is_alternate_extract(list_1, list_2)
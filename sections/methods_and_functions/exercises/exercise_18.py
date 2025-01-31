def myfunc(*args):
    even_list = []

    for n in args:
        if n % 2 == 0:
            even_list.append(n)
        else:
            pass

    return even_list


print(myfunc(1, 2, 3, 4, 5, 6, 7, 8, 9, 10))

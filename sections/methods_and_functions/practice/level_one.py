def old_macdonald(name):
    # first = name[0]
    # between = name[1:3]
    # fourth = name[3]
    # rest = name[4:]

    # return first.upper() + between + fourth.upper() + rest

    first_half = name[:3]
    second_half = name[3:]

    return first_half.capitalize() + second_half.capitalize()


print(old_macdonald("Javier"))


def master_yoda(string):
    word_list = string.split()
    reverse = word_list[::-1]

    return " ".join(reverse)


print(master_yoda("Hello it's me"))


def almost_there(n):
    return (abs(100 - n) <= 10) or (abs(200 - n) <= 10)


print(almost_there(89))
print(almost_there(91))
print(almost_there(101))
print(almost_there(150))
print(almost_there(200))

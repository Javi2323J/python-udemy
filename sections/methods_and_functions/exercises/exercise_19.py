def myfunc(string):
    result = ""

    for index, letter in enumerate(string):
        if index % 2 == 0:
            result += letter.lower()
        else:
            result += letter.upper()

    return result


print(myfunc("helloworld"))

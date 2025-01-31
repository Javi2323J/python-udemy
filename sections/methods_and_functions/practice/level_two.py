def has_33(numlist):
    for i in range(0, len(numlist) - 1):
        if numlist[i] == 3 and numlist[i + 1] == 3:  # numlist[i:i + 2] == [3, 3]
            return True

    return False


print(has_33([1, 3, 1, 3, 1, 3]))
print(has_33([1, 3, 1, 3, 1, 3, 3]))


def paper_doll(text):
    result = ""

    for char in text:
        result += char * 3

    return result


print(paper_doll("Hello"))


def blackjack(a, b, c):
    if sum([a, b, c]) <= 21:
        return sum([a, b, c])
    elif 11 in [a, b, c] and sum([a, b, c]) <= 31:
        return sum([a, b, c]) - 10
    else:
        return "BUST"


print(blackjack(10, 8, 3))
print(blackjack(10, 8, 2))
print(blackjack(10, 11, 2))
print(blackjack(10, 11, 13))


def summer_69(arr):
    total = 0
    add = True

    for num in arr:
        while add:
            if num != 6:
                total += num
                break
            else:
                add = False
        while not add:
            if num != 9:
                break
            else:
                add = True
                break

    return total


print(summer_69([1, 2, 3, 6, 10, 50, 9]))
print(summer_69([1, 2, 3, 6, 10, 50, 9, 10]))

def vol(rad):
    return (4 / 3) * (3.14) * (rad**3)


print(vol(2))


def ran_check(num, low, high):
    return num in range(low, high + 1)


print(ran_check(5, 2, 7))
print(ran_check(5, 2, 5))
print(ran_check(5, 2, 3))


def up_low(s):
    lower_count = 0
    upper_count = 0

    for char in s:
        if char.isupper():
            upper_count += 1
        elif char.islower():
            lower_count += 1
        else:
            pass

    print(f"Lowercase count: {lower_count}")
    print(f"Uppercase count: {upper_count}")


up_low("Hello World")


def unique_list(numlist):
    x = []

    for number in numlist:
        if number not in x:
            x.append(number)

    return x


print(unique_list([1, 1, 1, 2, 3, 4, 4, 4, 5, 5, 6]))


def multiply(numbers):
    total = 1

    for num in numbers:
        total = total * num

    return total


print(multiply([1, 2, 3, 10]))


def palindrome(s):
    s = s.replace(" ", "")  # Remove spaces

    return s == s[::-1]


print(palindrome("nurses run"))
print(palindrome("hello world"))


import string


def ispangram(str1, alphabet=string.ascii_lowercase):
    alphaset = set(alphabet)

    str1 = str1.replace(" ", "")

    str1 = str1.lower()

    str1 = set(str1)

    return str1 == alphaset


print(ispangram("The quick brown fox jumps over the lazy dog"))

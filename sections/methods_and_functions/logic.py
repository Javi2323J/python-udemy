print(2 % 2)
print(3 % 2)
print(41 % 40)
print(20 % 2)
print(20 % 2 == 0)  # Check even or odd
print(21 % 2 == 0)


def even_check(num):
    return num % 2 == 0


even_check(20)
even_check(21)

# RETURN TRUE IF ANY ITEM IS EVEN INSIDE A LIST


def check_even_list(num_list):
    even_numbers = []

    for number in num_list:
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            pass

    return even_numbers


print(check_even_list([1, 3, 5, 7, 9]))
print(check_even_list([1, 3, 4, 5, 7, 9, 10]))
print(check_even_list([0, 2, 4, 6, 8, 9]))

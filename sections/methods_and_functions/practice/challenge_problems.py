def spy_game(numlist):
    code = [0, 0, 7, ""]

    for num in numlist:
        if num == code[0]:
            code.pop(0)

    return len(code) == 1


print(spy_game([1, 2, 3, 0, 4, 0, 5, 6, 7, 8, 9]))
print(spy_game([1, 2, 3, 0, 4, 0, 5, 6, 0, 8, 9]))
print(spy_game([1, 2, 3, 0, 4, 7, 5, 6, 0, 8, 9]))
print(spy_game([1, 2, 3, 7, 0, 0, 5, 6, 7, 8, 9]))

print("\nCHANGE\n")


def count_primes(n):
    if n < 2:
        return 0

    primes = [2]
    x = 3

    while x <= n:
        for i in primes:
            if x % i == 0:
                x += 2
                break
        else:  # We acceed this else if we do not break in the for loop
            primes.append(x)
            x += 2

    print(primes)

    return len(primes)


print(count_primes(100))

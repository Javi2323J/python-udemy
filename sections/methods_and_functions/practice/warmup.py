def lesser_of_two_evens(a, b):
    if a % 2 == 0 and b % 2 == 0:
        return min(a, b)
    else:
        return max(a, b)


print(lesser_of_two_evens(2, 4))
print(lesser_of_two_evens(2, 1))
print(lesser_of_two_evens(7, 4))


def animal_crackers(string):
    words = string.lower().split()

    return words[0][0] == words[1][0]


print(animal_crackers("Levelheaded Llama"))
print(animal_crackers("Levelheaded llama"))
print(animal_crackers("Crazy Kangaroo"))


def makes_twenty(n1, n2):
    return (n1 + n2) == 20 or n1 == 20 or n2 == 20


print(makes_twenty(10, 10))
print(makes_twenty(20, 10))
print(makes_twenty(2, 19))

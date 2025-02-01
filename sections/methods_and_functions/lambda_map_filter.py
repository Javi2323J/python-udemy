def square(num):
    return num**2


my_nums = [1, 2, 3, 4, 5]

for item in map(square, my_nums):
    print(item)

print(list(map(square, my_nums)))


def splicer(string):
    if len(string) % 2 == 0:
        return "EVEN"
    else:
        return string[0]


names = ["Andy", "Eve", "Sally"]

print(list(map(splicer, names)))


def check_even(num):
    return num % 2 == 0


mynumbers = [1, 2, 3, 4, 5, 6]

for item in filter(check_even, mynumbers):
    print(item)

square = lambda num: num**2

print(square(3))

print(list(map(lambda num: num**2, mynumbers)))

print(list(filter(lambda num: num % 2 == 0, mynumbers)))

print(list(map(lambda name: name[::-1], names)))

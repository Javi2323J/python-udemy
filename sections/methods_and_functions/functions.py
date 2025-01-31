def say_hello():
    print("hello")
    print("how")
    print("are")
    print("you")


say_hello()


def say_hello(name="Default"):
    print(f"Hello {name}")


say_hello("Javi")
say_hello()


def add_num(num1, num2):
    return num1 + num2


result = add_num(10, 20)

print(result)


def print_result(a, b):
    print(a + b)


def return_result(a, b):
    return a + b


print_result(10, 20)
result = print_result(10, 20)

print(result)  # None

return_result(10, 20)
result = return_result(10, 20)

print(result)


def myfunc(a, b):
    print(a + b)
    return a + b


myfunc(10, 20)
result = myfunc(10, 20)

print(result)


def sum_number(n1, n2):
    return n1 + n2


print(sum_number(20, 25))

print(sum_number("20", "25"))

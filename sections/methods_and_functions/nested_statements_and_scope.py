x = 25


def printer():
    x = 50
    return x


print(x)

print(printer())

# lambda num: num**2

# GLOBAL
name = "THIS IS A GLOBAL STRING"


def greet():
    # ENCLOSING
    name = "Sammy"

    def hello():
        # LOCAL
        name = "IM A LOCAL"

        print("Hello " + name)

    hello()


greet()

x = 50


def func(x):
    print(f"X is {x}")

    # LOCAL REASSIGNMENT
    x = 200
    print(f"I JUST LOCALLY CHANGED X TO {x}")


func(x)
print(x)

x = 50


def func():
    global x
    print(f"X is {x}")

    # LOCAL REASSIGNMENT
    x = "NEW VALUE"
    print(f"I JUST LOCALLY CHANGED GLOBAL X TO {x}")


func()
print(x)

def myfunc(a, b):
    return sum((a, b)) * 0.05


print(myfunc(40, 60))


def myfunc(*args):  # Tuple of parameters; args is chosen by convention
    return sum(args) * 0.05


print(myfunc(40, 60))
print(myfunc(40, 60, 50, 20, 10))
print(myfunc(40, 60, 20, 30, 40, 40, 50, 60, 70, 80))


def myfunc(**kwargs):
    if "fruit" in kwargs:
        print("My fruit of choice is {}".format(kwargs["fruit"]))
    else:
        print("I did not find any fruit here")


myfunc(fruit="apple", veggie="lettuce")
myfunc(veggie="lettuce")


def myfunc(*args, **kwargs):
    print("I would like {} {}".format(args[0], kwargs["food"]))


myfunc(10, 20, 30, fruit="orange", animal="dog", food="eggs")

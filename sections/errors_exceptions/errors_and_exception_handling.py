def add(n1, n2):
    print(n1 + n2)


add(10, 20)

# number1 = 10
# number2 = input("Please provide a number: ")

# add(number1, number2)
# print("Something happened!")

try:
    result = 10 + "10"
except:
    print("You're not adding correctly")
else:
    print("Add went well!")
    print(result)

print("aa")

print("\nCHANGE\n")

try:
    f = open("testfile", "r")
    f.write("Write a test line")
except TypeError:
    print("There was a type error!")
except OSError:
    print("Hey you have an OS Error")
except:
    print("All other exceptions")
finally:
    print("I always run")


def ask_for_int():
    while True:
        try:
            result = int(input("Please provide number: "))
        except:
            print("Whoops! That is not a number")
            continue
        else:
            print("Yes thank you")
            break
        finally:  # This runs even if its not highlighted
            print("End of try/except/finally")
            print("I will always run at the end")


ask_for_int()

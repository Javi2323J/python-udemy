example_row1 = [1, 2, 3]
example_row2 = [4, 5, 6]
example_row3 = [7, 8, 9]


def display(row1, row2, row3):
    print(row1)
    print(row2)
    print(row3)


display(example_row1, example_row2, example_row3)

row1 = [" ", " ", " "]
row2 = [" ", " ", " "]
row3 = [" ", " ", " "]

row2[1] = "X"

display(row1, row2, row3)

print("\nUSER INPUT\n")

# result = input("Please enter a value: ")
# result = int(result)


# position_index = int(input("Choose an index position: "))
# print(row2[position_index])

print("\nVALIDATE INPUT\n")


def user_choice():
    choice = ""
    acceptable_range = range(0, 11)
    within_range = False

    while choice.isdigit() == False or within_range == False:
        choice = input("Please enter a number (0-10): ")

        # Digit check
        if choice.isdigit() == False:
            print("Invalid input")

        # Range check
        if choice.isdigit() == True:
            if int(choice) in acceptable_range:
                within_range = True
            else:
                within_range = False
                print("Invalid range")

    return int(choice)


user_choice()

def display(board):
    print("\n" * 30)
    print(board[7] + " | " + board[8] + " | " + board[9])
    print("- - - - -")
    print(board[4] + " | " + board[5] + " | " + board[6])
    print("- - - - -")
    print(board[1] + " | " + board[2] + " | " + board[3])


def player_input():
    marker = ""

    while marker != "X" and marker != "O":
        marker = input("Player 1, choose X or O").upper()

        if marker != "X" and marker != "O":
            print("Please, choose a valid option")

    player1 = marker

    if player1 == "X":
        player2 = "O"
    else:
        player2 = "X"

    return (player1, player2)


def did_win(board, marker):
    return (
        (board[1] == marker and board[2] == marker and board[3] == marker)
        or (board[4] == marker and board[5] == marker and board[6] == marker)
        or (board[7] == marker and board[8] == marker and board[9] == marker)
        or (board[7] == marker and board[4] == marker and board[1] == marker)
        or (board[8] == marker and board[5] == marker and board[2] == marker)
        or (board[9] == marker and board[6] == marker and board[3] == marker)
        or (board[1] == marker and board[5] == marker and board[9] == marker)
        or (board[7] == marker and board[5] == marker and board[3] == marker)
    )


def play(initial_board, p1_mark, p2_mark):
    currentMarker = ""
    turn = 0
    p_input = 0

    while not did_win(initial_board, currentMarker):
        p_input = input("Select a tile: (1-9)")

        if int(p_input) not in range(1, 10) or initial_board[int(p_input)] != " ":
            print("Please, choose a valid tile")
        else:
            if turn % 2 == 0:
                currentMarker = p1_mark
            else:
                currentMarker = p2_mark

            initial_board[int(p_input)] = currentMarker
            turn += 1
            display(initial_board)

    if currentMarker == p1_mark:
        print("Player 1 won!")
    elif currentMarker == p2_mark:
        print("Player 2 won!")


def replay():
    inp = ""
    playagain = True

    while inp.upper() not in ["Y", "N"]:
        inp = input("Do you want to play again? (Y / N)").upper()

    if inp == "Y":
        playagain = True
    else:
        playagain = False

    return playagain


while True:
    initial_board = ["#", " ", " ", " ", " ", " ", " ", " ", " ", " "]
    display(initial_board)
    p1_marker, p2_marker = player_input()
    play(initial_board, p1_marker, p2_marker)
    if not replay():
        break

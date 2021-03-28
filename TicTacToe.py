# -- Set of Global Variables --

# Our board
grid = ["-", "-", "-",
        "-", "-", "-",
        "-", "-", "-"]

# Is game over?
game_still_goes = True

# Whose turn is it ? Player X start first
cur_player = 'X'

# Who wins the game?
winner = None

# -- Set of Functions --

# Display the game board to the screen


def display_grid():

    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(grid[0], grid[1], grid[2]))
    print('\t_____|_____|_____')

    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(grid[3], grid[4], grid[5]))
    print('\t_____|_____|_____')

    print("\t     |     |")

    print("\t  {}  |  {}  |  {}".format(grid[6], grid[7], grid[8]))
    print("\t     |     |")
    print("\n")


# How a single turn unfolds


def turn(player):
    print('Now it is {} \'s turn'.format(player))
    move = int(input('Please choose your desired position (1 (top left) to 9 (down right)): ')) - 1

    number_is_valid = False
    while not number_is_valid:
        while move not in range(9):
            move = int(input('Please choose your desired position (1 (top left) to 9 (down right)): ')) - 1

        if grid[move] == "-":
            number_is_valid = True
        else:
            move = int(input('This position is already taken. Please choose another position (1-9): ')) - 1

    # Display the board with the desired move
    grid[move] = player
    display_grid()


def game_is_over():
    # Check if someone won the game
    check_win()

    # Check if the game is a tie
    check_tie()


def check_tie():
    global game_still_goes
    # grid is a list so we check if we have any empty position
    if '-' not in grid:
        game_still_goes = False
    return


def check_win():
    global winner
    # Check in each direction
    row_win = check_if_win_in_rows()
    column_win = check_if_win_in_columns()
    diagonal_win = check_if_win_in_diagonals()

    if column_win:
        winner = column_win
    elif row_win:
        winner = row_win
    elif diagonal_win:
        winner = diagonal_win
    else:
        winner = None
    return

# Check the rows for a win


def check_if_win_in_rows():
    global game_still_goes
    # Check any row wins (given that it is not empty)
    row_1 = grid[0] == grid[1] == grid[2] != "-"
    row_2 = grid[3] == grid[4] == grid[5] != "-"
    row_3 = grid[6] == grid[7] == grid[8] != "-"
    # If we have a winner, stop the game
    if row_1 or row_2 or row_3:
        game_still_goes = False
    # Who won? (X or O)
    if row_1:
        return grid[1]
    elif row_2:
        return grid[4]
    elif row_3:
        return grid[7]
    else:
        return None


# Check the columns for a win


def check_if_win_in_columns():
    global game_still_goes
    # Check any column wins (given that it is not empty)
    column_1 = grid[0] == grid[3] == grid[6] != "-"
    column_2 = grid[1] == grid[4] == grid[7] != "-"
    column_3 = grid[2] == grid[5] == grid[8] != "-"
    # If we have a winner, stop the game
    if column_1 or column_2 or column_3:
        game_still_goes = False
    # Who won? (X or O)
    if column_1:
        return grid[3]
    elif column_2:
        return grid[4]
    elif column_3:
        return grid[5]
    else:
        return None


# Check the diagonals for a win

def check_if_win_in_diagonals():
    global game_still_goes
    # Check any diagonal wins (given that it is not empty)
    diagonal_1 = grid[0] == grid[4] == grid[8] != "-"
    diagonal_2 = grid[6] == grid[4] == grid[2] != "-"
    # If we have a winner, stop the game
    if diagonal_1 or diagonal_2:
        game_still_goes = False
    # Who won? (X or O)
    if diagonal_1:
        return grid[0]
    elif diagonal_2:
        return grid[6]
    else:
        return None

# Flip the current player from X to O, or O to X


def change_turn():
    global cur_player
    # If the current player was X, make it O and vice versa
    if cur_player == "X":
        cur_player = "O"
    else:
        cur_player = "X"


def playing_game():

    # Display our board
    display_grid()

    # While we still playing the game
    while game_still_goes:

        # Start a turn for each player
        turn(cur_player)

        # Check if game is finished
        game_is_over()

        # Change player
        change_turn()

        # How the game ends
    if winner == 'X' or winner == 'O':
        print('The winner is Player {} . Congrats!!!'.format(winner))
    elif winner is None:
        print('The game is a tie. Play again!!!')


# -- Start the Game --
print("\n")
print('Take your seats cause, the game is about to start!!!!!'.upper())
playing_game()

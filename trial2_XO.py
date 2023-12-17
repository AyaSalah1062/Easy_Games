
import random
def tic_tac_toe():
    print("Welcome to Tic Tac Toe!\n")
    print("Instructions:")
    print("-------------")

    print("The game is played on a 3x3 grid.")
    print("Player 1 is X, and Player 2 is O.")
    print("The first player to get 3 of their markers in a row (horizontally, vertically, or diagonally) wins.")
    print("If all 9 spaces are filled and no player has won, the game is a tie.")
    print("--------------------------------------------------------------------")


    # Prompt for game mode (1 player vs computer or 2 players)
    while True:
        game_mode = input("Enter '1' for 1 player vs computer, or '2' for 2 players: ")
        if game_mode == "1":
            player1_name = input("Enter your name: ")
            player2_name = "Computer"
            break
        elif game_mode == "2":
            player1_name = input("Enter Player 1 name: ")
            player2_name = input("Enter Player 2 name: ")
            break
        else:
            print("Invalid input. Please enter '1' or '2'.")

    # # Prompt for first player's marker (X or O)
    # if game_mode == "2":
    #     while True:
    #         first_player_marker = input(f"{player1_name}, choose your marker (X or O): ").upper()
    #         if first_player_marker == "X" or first_player_marker == "O":
    #             break
    #         else:
    #             print("Invalid input. Please enter 'X' or 'O'.")
    # else:
    #     print(f"{player1_name}, you are Player 1 and will play as X.")
    #     first_player_marker = "X"
# Prompt for first player's marker (X or O)
    if game_mode == "2":
        while True:
            first_player_marker = input(f"{player1_name}, choose your marker (X or O): ").upper()
            if first_player_marker == "X" or first_player_marker == "O":
                break
            else:
                print("Invalid input. Please enter 'X' or 'O'.")
    else:
        while True:
            first_player_marker = input(f"{player1_name}, choose your marker (X or O): ").upper()
            if first_player_marker == "X" or first_player_marker == "O":
                break
            else:
                print("Invalid input. Please enter 'X' or 'O'.")
        print(f"{player1_name}, you are Player 1 and will play as {first_player_marker}.")
        # Initialize the scoreboard
    player1_score = 0
    player2_score = 0
    ties = 0

    # Main game loop
    while True:
        # Initialize the board
        board = [" "]*9

        # Print the initial board
        print_board(board)

        # # Randomly decide which player goes first
        current_player_name = player2_name  if random.randint(0, 1) == 0 else player2_name
        current_player_marker = first_player_marker if current_player_name == player1_name else "X" if first_player_marker == "O" else "O"
        print(f"{current_player_name} ({current_player_marker}) goes first.")

        # Main game loop
        while True:
            # Get the current player's move
            if current_player_name == "Computer":
                position = get_computer_move(board)
            else:
                position = get_player_move(board, current_player_name)

            # Update the board
            board[position] = current_player_marker
            print_board(board)

            # Check if the game is over
            if has_won(board, current_player_marker):
                print(f"{current_player_name} wins!")
                if current_player_name == player1_name:
                    player1_score += 1
                else:
                    player2_score += 1
                break
            elif is_board_full(board):
                print("Tie game!")
                ties += 1
                break

            # Switch to the other player's turn
            current_player_name = player1_name if current_player_name == player2_name else player2_name
            current_player_marker = "X" if current_player_marker == "O" else "O"

        # Print the current scoreboard
        print(f"Score: {player1_name}: {player1_score}  {player2_name}: {player2_score}  Ties: {ties}")

        # Prompt to restart or exit the game
        while True:
            play_again = input("Enter 'r' to play again, or 'x' to exit: ")
            if play_again == "r":
                break
            elif play_again == "x":
                return
            else:
                print("Invalidinput. Please enter 'r' or 'x'.")
def print_board(board):
    for i in range(9):
        if board[i] == "X":
            print("\033[92mX\033[0m", end="")
        elif board[i] == "O":
            print("\033[94mO\033[0m", end="")
        else:
            print(i+1, end="")
        if i == 2 or i == 5:
            print("\n--|---|--")
        elif i == 8:
            print()
        else:
            print(" | ", end="")


def get_player_move(board, player_name):
    while True:
        try:
            position = int(input(f"{player_name}, choose a position (1-9): ")) - 1
            if position < 0 or position > 8:
                print("Invalid input. Please enter a number from 1 to 9.")
            elif board[position] != " ":
                print("That position is already taken. Please choose another position.")
            else:
                return position
        except ValueError:
            print("Invalid input. Please enter a number from 1 to 9.")
def get_winning_moves(board, player):
    winning_moves = 0
    for i in range(9):
        if board[i] == " ":
            new_board = board[:i] + [player] + board[i+1:]
            if has_won(new_board, player):
                winning_moves += 1
    return winning_moves
def get_computer_move(board):
    # Check if the computer can win in the next move
    for i in range(9):
        if board[i] == " " and has_won(board[:i] + ["X"] + board[i+1:], "X"):
            return i

    # Check if the player could win on their next move, and block them
    for i in range(9):
        if board[i] == " " and has_won(board[:i] + ["O"] + board[i+1:], "O"):
            return i

    # Check if the computer can create a fork and win in two ways
    for i in range(9):
        if board[i] == " ":
            new_board = board[:i] + ["X"] + board[i+1:]
            if new_board.count("X") >= 2 and get_winning_moves(new_board, "X") >= 2:
                return i

    # Check if the player can create a fork, and block them
    for i in range(9):
        if board[i] == " ":
            new_board = board[:i] + ["O"] + board[i+1:]
            if new_board.count("O") >= 2 and get_winning_moves(new_board, "O") >= 2:
                return i

    # Try to take the center, if it is free
    if board[4] == " ":
        return 4

    # Try to take one of the corners, if they are free
    corners = [0, 2, 6, 8]
    random.shuffle(corners)
    for corner in corners:
        if board[corner] == " ":
            return corner

    # Take any empty cell
    empty_cells = [i for i in range(9) if board[i] == " "]
    return random.choice(empty_cells)


def has_won(board, marker):
    # Check rows
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] == marker:
            return True

    # Check columns
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] == marker:
            return True

    # Check diagonals
    if board[0] == board[4] == board[8] == marker:
        return True
    if board[2] ==board[4] == board[6] == marker:
        return True

    # If none of the above conditions are met, the game is not over
    return False


def is_board_full(board):
    # Check if the board is full
    return all(cell != " " for cell in board)


# Example usage
tic_tac_toe()
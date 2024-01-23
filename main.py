from Modules.dice import dice_roll
from Modules.board import create_board, print_board
from Modules.text_file import write_file
from Modules.start import slow_print, start_text
import time
import sys

# Initialize move and black hole
total_human_moves = 0
total_comp_moves = 0
black_hole_h = 0
black_hole_c = 0

# Initialize player and computer positions
human_pos = 0
comp_pos = 0


def play_game():

    global total_human_moves, total_comp_moves, black_hole_h, black_hole_c, human_pos, comp_pos

    while True:
        board = create_board()
        # Human player's turn
        input("Press Enter to roll the dice...")
        h_dice = dice_roll()
        time.sleep(0.5)
        print("You rolled a ",h_dice,"\n")        

        # Check whether human player can enter the game
        if h_dice == 6 and human_pos == 0:
            human_pos = 1
            input("Press Enter to roll the dice again...")
            time.sleep(0.5)
            h_dice = dice_roll()
            print("You rolled a ",h_dice,"\n")
            
            human_move = h_dice // 2
            human_pos += human_move
            total_human_moves += 1

            board[0][human_pos - 1] = "X"
            human_stat = (
                "current location is" + " " + str(human_pos) + "(just entered the game)"
            )

        elif h_dice != 6 and human_pos == 0:
            human_move = 0
            human_stat = "cannot start the game"
        else:
            human_move = h_dice // 2
            human_pos += human_move

            # Check if human player wins
            if human_pos >= 20:
                total_human_moves += 1
                time.sleep(1)
                print("\n")
                print(
                    "  01   02   03   04   05   06   07   08   09   10   11   12   13   14   15   16   17   18   19   20  "
                )
                print_board(board)
                print(
                    "Human dice roll is "
                    + str(h_dice)
                    + " and current location is "
                    + str(human_pos)
                    + " (Winner!!)"
                )
                print(
                    "Computer dice roll is "
                    + str(c_dice)
                    + " and current location is "
                    + str(comp_pos)
                )
                # Write the game play in a text file
                write_file(
                    total_human_moves,
                    black_hole_h,
                    human_pos,
                    total_comp_moves,
                    black_hole_c,
                    comp_pos,
                )
                # Replay the game when human player win
                while True:
                    play_again = input("Do you want to play again? (yes or no)")
                    # Check if the input is valid
                    if play_again not in ["y", "n", "yes", "no", "Y", "N", "YES", "NO"]:
                        print("Invalid Answer! Try agian.")
                    else:
                        break
                    
                if play_again in ["y", "yes", "Y", "YES"]:
                    # Set main variables to zero to start the game again
                    human_pos = 0
                    comp_pos = 0
                    total_human_moves = 0
                    total_comp_moves = 0
                    black_hole_h = 0
                    black_hole_c = 0
                    continue
                else:
                    slow_print("\nThanks for playing :)")
                    break

            # check if player hits a black hole
            elif board[0][human_pos - 1] == board[0][6]:
                print("Oops you hit a black hole :( \n")
                human_pos = 1
                total_human_moves += 1
                black_hole_h += 1
                human_stat = "hit a black hole"

            else:
                total_human_moves += 1
                human_stat = "current location is" + " " + str(human_pos)
            board[0][human_pos - 1] = "X"

        # computer's turn
        print("Computer's turn..")
        c_dice = dice_roll()
        time.sleep(0.5)
        print("Computer rolled a ",c_dice,"\n")

        # Check whether human player can enter the game
        if c_dice == 6 and comp_pos == 0:
            comp_pos = 1
            print("Computer's turn again..")
            time.sleep(0.5)
            c_dice = dice_roll()
            print("Computer rolled a ",c_dice)
            
            computer_move = c_dice // 2
            comp_pos += computer_move
            total_comp_moves += 1

            board[1][comp_pos - 1] = "X"
            comp_stat = (
                "current location is"
                + " "
                + str(comp_pos)
                + "(just entered the game!!)"
            )

        elif c_dice != 6 and comp_pos == 0:
            computer_move = 0
            comp_stat = "cannot start the game"
        else:
            computer_move = c_dice // 2
            comp_pos += computer_move

            # check if computer wins
            if comp_pos > 19:
                total_comp_moves += 1
                time.sleep(1)
                print("\n")
                print(
                    "  01   02   03   04   05   06   07   08   09   10   11   12   13   14   15   16   17   18   19   20  "
                )
                print_board(board)
                print(
                    "Human dice roll is "
                    + str(h_dice)
                    + " and current location is "
                    + str(human_pos)
                )
                print(
                    "Computer dice roll is "
                    + str(c_dice)
                    + " and current location is "
                    + str(comp_pos)
                    + " (Winner!!) \n"
                )
                # Write the game play in a text file
                write_file(
                    total_human_moves,
                    black_hole_h,
                    human_pos,
                    total_comp_moves,
                    black_hole_c,
                    comp_pos,
                )
                # Replay the game when computer win
                while True:
                    play_again = input("Do you want to play again? (yes or no)")
                    # Check if the input is valid
                    if play_again not in ["y", "n", "yes", "no", "Y", "N", "YES", "NO"]:
                        print("Invalid Answer! Try again.")
                    else:
                        break
                if play_again in ["y", "yes", "Y", "YES"]:
                    # Set main variables to zero to start the game again
                    human_pos = 0
                    comp_pos = 0
                    total_human_moves = 0
                    total_comp_moves = 0
                    black_hole_h = 0
                    black_hole_c = 0
                    continue
                else:
                    # End the game
                    slow_print("\nThanks for playing :)")
                    break

            # check if computer hits a black hole
            elif board[1][comp_pos - 1] == board[1][6]:
                print("Oops computer hit the black hole -_- \n")
                comp_pos = 1
                total_comp_moves += 1
                black_hole_c += 1
                comp_stat = "hit a black hole"

            else:
                total_comp_moves += 1
                comp_stat = "current location is" + " " + str(comp_pos)
            board[1][comp_pos - 1] = "X"

        # Print the board the and the status of the players
        time.sleep(1)
        print("\n")
        print(
            "  01   02   03   04   05   06   07   08   09   10   11   12   13   14   15   16   17   18   19   20  "
        )
        print_board(board)
        print("Your status: Human dice roll is", h_dice, human_stat)
        print("Computer's status: Computer dice roll is", c_dice, comp_stat, "\n")


start_text()
play_game()




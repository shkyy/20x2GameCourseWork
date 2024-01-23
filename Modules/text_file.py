import datetime

def write_file(total_human_moves, black_hole_h, human_pos, total_comp_moves, black_hole_c, comp_pos):
    now = datetime.datetime.now()
    filename = now.strftime("%Y_%m_%d_%H_%M") + ".txt"

    with open(filename, "w") as f:

        f.write('Human \n')
        f.write("Total moves: " + str(total_human_moves) + "\n")
        f.write("Black hole hits: " + str(black_hole_h) + "\n")
        f.write(("Won the game" if human_pos < 19 else "Lost the game") + "\n")

        f.write('\nComputer \n')
        f.write("Total moves: " + str(total_comp_moves) + "\n")
        f.write("Black hole hits: " + str(black_hole_c) + "\n")
        f.write(("Won the game" if comp_pos < 19 else "Lost the game") + "\n")

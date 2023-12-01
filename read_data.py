def get_input(day,part):
    input_lines = []
    f = open("data/advent_{}_{}.txt".format(day,part), "r")
    for line in f:
        input_lines.append(line)
    return input_lines


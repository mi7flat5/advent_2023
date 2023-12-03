from read_data import get_input
import os
import math

def get_valid_game(game):
    samples = game.split(":")[1].split(';')

    game_map = {}
    for sample in samples:
        colors = sample.split(',')
        for color in colors:
            c = color.split(' ')[2]

            num = int(color.split(' ')[1].replace(' ',''))
            if c == 'red' and num > 12:
                return 0
            if c == 'green' and num > 13:
                return 0
            if c == 'blue' and num > 14:
                return 0
            if c in game_map:
                game_map[c] += num
            else:
                game_map[c] = num

    return int(game.split(":")[0].split(' ')[1])

def get_power_of_game(game):
    samples = game.split(":")[1].split(';')

    game_map = {}
    for sample in samples:
        colors = sample.split(',')
        for color in colors:
            c = color.split(' ')[2]

            num = int(color.split(' ')[1].replace(' ',''))

            if c in game_map:
                game_map[c] = max(game_map[c],num)
            else:
                game_map[c] = num
    vals = list(game_map.values())

    return math.prod(vals)


if __name__ == '__main__':
    finput = get_input(int(os.path.basename(__file__).split('.')[0].replace('day','')),1)
    sum = 0
    for game in finput:
        sum += get_valid_game(game)
    print(sum)

    finput = get_input(int(os.path.basename(__file__).split('.')[0].replace('day','')),2)
    sum = 0
    for game in finput:
        sum += get_power_of_game(game)
    print(sum)





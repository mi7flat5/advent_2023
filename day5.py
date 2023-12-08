from read_data import get_input
import os

if __name__ == '__main__':
    finput = get_input(int(os.path.basename(__file__).split('.')[0].replace('day','')),1)
    seeds = []

    maps = []
    i = -1
    for line in finput:
        if line == '':
            maps.append([])
            i+=1
            if len(maps) > 1:
                maps[i-1].pop(0)
        if 'seeds:' in line:
            seeds = [int(x) for x in line.split(':')[1].strip().split(' ') if x != '']
        elif 'map' not in line:
            maps[i].append([int(x) for x in line.strip().split(' ') if x != ''])
    ids = {}
    for seed in seeds:
        id = seed
        for i in range(len(maps)):

            for j in range(len(maps[i])):
                if  len(maps[i][j]) == 0:
                    continue
                if id >= maps[i][j][1] and id < maps[i][j][1] + maps[i][j][2]:
                    id = maps[i][j][0] + (id - maps[i][j][1])
                    break
        ids[seed] = id
    start = 0
    end = 1
    ids2 ={}



    print(min(ids.values()))
    print(min(ids2.values()))








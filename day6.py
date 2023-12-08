from read_data import get_input
import os

if __name__ == '__main__':
    finput = get_input(int(os.path.basename(__file__).split('.')[0].replace('day','')),1)
    times = [int(x) for x in finput[0].split(':')[1].strip().split(' ') if  x != '']
    dist =  [int(x) for x in finput[1].split(':')[1].strip().split(' ') if x != '']
    totals = 1
    for i in range(len(times)):
        wins = 0
        for j in range(times[i]):
            x = j * (times[i] - j)
            if x > dist[i]:
                wins += 1
        totals *= wins
    print(totals)
    time = int(''.join([str(x) for x in times]))
    dist = int(''.join([str(x) for x in dist]))
    i1 = 0
    i2 = time
    L,R = True,True
    while L and R:
        if i1 * (time - i1) < dist:
            i1 += 1
        else:
            L = False
        if i2 * (time - i2) < dist:
            i2 -= 1
        else:
            R = False
    print((i2 - i1)+1)










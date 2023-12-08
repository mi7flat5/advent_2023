from read_data import get_input
from math import gcd
from functools import reduce

def lcm(denominators):
    return reduce(lambda a,b: a*b // gcd(a,b), denominators)
import os

if __name__ == '__main__':
    finput = get_input(int(os.path.basename(__file__).split('.')[0].replace('day','')),1)
    nm = {}
    steps = []
    starts = []
    stops = []
    for line in finput:
        if '=' in line:
            nodep = line.split(' = ')[0].strip()
            nodec = [x.strip() for x in line.split(' = ')[1].strip().replace('(', '').replace(')', '').split(',')]

            nm[nodep] = nodec
            if nodep[-1] == 'A':
                starts.append(nodep)
            if nodep[-1] == 'Z':
                stops.append(nodep)

        elif line == '':
            pass
        else:
            steps = [0 if x == 'L' else 1 for x in line]

    current = 'AAA'
    step_count = 0
    while current != 'ZZZ':
        for step in steps:
            step_count +=1
            current = nm[current][step]

    print(step_count)

    step_count = 0
    stepi = 0
    currents = [x for x in starts]
    ended = False
    cm = {}
    while not ended:
        step = steps[stepi]
        for i in range(len(starts)):
            current = currents[i]
            currents[i] = nm[current][step]
            if current[-1] == 'Z':
                cm[current] = step_count

            if len(cm) == len(currents):
                print(lcm(cm.values()))
                ended = True
                break
        step_count+=1
        stepi += 1
        stepi = stepi % len(steps)

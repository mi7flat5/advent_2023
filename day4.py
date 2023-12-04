from read_data import get_input
import os

def get_score(card):
    a,b = card.split('|')
    winnum = a .split(':')[1].strip().split(' ')
    nums = b.strip().split(' ')
    winnum, nums = [int(x) for x in winnum if x.isnumeric()], [int(x) for x in nums if x.isnumeric()]

    matches = 0
    for n in winnum:
        if n in nums:
            if matches == 0:
                matches = 1
            else: matches *= 2
    return matches

def get_win_count(card):
    a,b = card.split('|')
    winnum = a .split(':')[1].strip().split(' ')
    nums = b.strip().split(' ')
    winnum, nums = [int(x) for x in winnum if x.isnumeric()], [int(x) for x in nums if x.isnumeric()]

    matches = 0
    for n in nums:
        if n in winnum:
            matches +=1
    return matches

def get_cards(card):
    return card.split(':')[1].strip()

if __name__ == '__main__':
    finput = get_input(int(os.path.basename(__file__).split('.')[0].replace('day','')),1)
    sum1 = 0
    m = {}
    for i in range(len(finput)):
        sum1 += get_score(finput[i])

        if i in m:
            m[i] += 1
        else:
            m[i] = 1
        wincount = get_win_count(finput[i])
        for j in range(wincount):
            if i + 1 + j in m:
                m[i + 1 + j] += m[i]
            else:
                m[i + 1 + j] = m[i]

    print(sum1)
    print(sum(m.values()))















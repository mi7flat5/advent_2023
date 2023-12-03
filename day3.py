from read_data import get_input
import os
def get_adjacent(a,b):
    if abs(a[0] - b[0]) <= 1 and abs(a[1]-b[1]) <= 1:
        return True
    return False

if __name__ == '__main__':

    finput = get_input(int(os.path.basename(__file__).split('.')[0].replace('day','')),1)
    num = 0
    r_bound = len(finput)
    c_bound = len(finput[0])
    s = 0
    adj = False
    g = set()
    gm = {}
    for i in range(r_bound):
        for j in range(c_bound):
            c = finput[i][j]
            if c.isnumeric():
                num = num*10+int(c)
                for id in [-1,0,1]:
                    for id2 in [-1,0,1]:
                        if i+id < r_bound and i+id >=0 and j+id2 < r_bound and j+id2 >=0:
                            ch = finput[i+id][j+id2]
                            if not ch.isnumeric() and ch != '.':
                                adj = True
                            if ch == '*':
                                g.add((i+id,j+id2))
            elif num > 0:
              if adj:
                  s += num
                  for gear in g:
                      if gear in gm:
                          gm[gear].append(num)
                      else:
                          gm[gear] = [num]
              num = 0
              adj = False
              g.clear()
    s2 = 0
    for gear in gm.keys():
        if len(gm[gear]) == 2:
            s2 += gm[gear][0]*gm[gear][1]
    print(s)
    print(s2)







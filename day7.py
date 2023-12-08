from read_data import get_input
import os

if __name__ == '__main__':
    finput = get_input(int(os.path.basename(__file__).split('.')[0].replace('day','')),1)
    hc = []
    op = []
    tp = []
    tk = []
    fh = []
    fk = []
    fvk = []
    for hand in finput:
        cards = hand.split(' ')[0]
        csl = len(set([c for c in cards]))
        if csl == 5:
            hc.append(hand)
            continue
        if csl == 1:
            fvk.append(hand)
            continue
        nums = [0] * 13
        for c in cards:
            if c.isnumeric():
                nums[int(c)-1] += 1
            elif c == 'A':
                nums[0] +=1
            elif c == 'T':
                nums[9] +=1
            elif c == 'J':
                nums[10] +=1
            elif c == 'Q':
                nums[11] +=1
            elif c == 'K':
                nums[12] +=1
        ct = sum([x for x in nums if x > 1])
        if ct == 2:
            op.append(hand)
        if ct == 3:
            tk.append(hand)
        if ct == 4:
            if csl == 2:
                fk.append(hand)
            else:
                tp.append(hand)
        if ct == 5:
            fh.append(hand)

    def sort_hands(hands):
        order = []
        for hand in hands:
            st = ""
            cards = hand.split(' ')[0]
            for c in cards:
                if c.isnumeric():
                    st += c
                else:
                    if c == 'T':
                        st += ':'
                    if c == 'J':
                        st += ';'
                    if c == 'Q':
                        st += '<'
                    if c == 'K':
                        st += '='
                    if c == 'A':
                        st += '>'
            order.append((st,hand))
        #print(sorted(order))
        return [x[1] for x in sorted(order)]
    def sort_hands_wild(hands):
        order = []
        for hand in hands:
            st = ""
            cards = hand.split(' ')[0]
            for c in cards:
                if c.isnumeric():
                    st += c
                else:
                    if c == 'T':
                        st += ':'
                    if c == 'J':
                        st += '1'
                    if c == 'Q':
                        st += '<'
                    if c == 'K':
                        st += '='
                    if c == 'A':
                        st += '>'
            order.append((st,hand))
        return [x[1] for x in sorted(order)]

    out= []
    for sets in [hc,op,tp,tk,fh,fk,fvk]:
        tmp = sort_hands(sets)
        for hand in tmp:
            out.append(hand)
    sum_ = 0
    for i in range(len(out)):
        sum_ += (i +1) * int(out[i].split(' ')[1])
    print(sum_)
    hc = []
    op = []
    tp = []
    tk = []
    fh = []
    fk = []
    fvk = []
    out = []
    for hand in finput:
        cards = hand.split(' ')[0]
        csl = len(set([c for c in cards]))
        if csl == 5 and 'J' not in cards:
            hc.append(hand)
            continue
        if csl == 1:
            fvk.append(hand)
            continue
        nums = [0] * 13
        for c in cards:
            if c.isnumeric():
                nums[int(c) - 1] += 1
            elif c == 'A':
                nums[0] += 1
            elif c == 'T':
                nums[9] += 1
            elif c == 'J':
                nums = [x + 1 for x in nums]
                nums[10] = 0
            elif c == 'Q':
                nums[11] += 1
            elif c == 'K':
                nums[12] += 1

        nums_ = [x for x in nums if x > 1] if 'J' not in cards else [x for x in nums if x > 1]

        ct = sum(nums_)
        # if 'J' in cards:
        #     print(nums_, cards, ct)
        #     input()
        if ct == 2:
            op.append(hand)
        if ct == 3:
            tk.append(hand)
        if ct == 4:
            if csl == 2 or 'J' in cards:
                fk.append(hand)
            else:
                tp.append(hand)
        if ct == 5:
            if 'J' not in cards:
                fh.append(hand)
            else:
                fvk.append(hand)
        if ct == 6:
            if len(set(nums)) == 1:
                fh.append(hand)
            else:
                fk.append(hand)
        if ct == 7 or ct == 27:
            tk.append(hand)
        if ct == 8:
            op.append(hand)
        if ct == 38:
            fk.append(hand)

    for sets in [hc,op,tp,tk,fh,fk,fvk]:
        tmp = sort_hands_wild(sets)
        for hand in tmp:
            out.append(hand)
    sum = 0

    for i in range(len(out)):
        sum += (i +1) * int(out[i].split(' ')[1])
    print(out)
    print(sum)















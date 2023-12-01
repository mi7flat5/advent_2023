from read_data import get_input
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    finput = get_input(1,1)


    def do_sum(local_input):
        sum = 0
        for line in local_input:
            nums = []
            for c in line:
                if c.isnumeric():
                    nums.append(c)
            if len(nums) == 0:
                continue
            if len(nums) == 1:
                sum += (int(nums[0]+nums[0]))
            if len(nums) >1:
                sum += int(nums[0]+nums[-1])
        print(sum)
    do_sum(finput)

    finput = get_input(1,2)
    anum = ['one','two','three','four','five','six','seven','eight','nine']
    anummap = {}
    w_to_n = 1

    for num in anum:
        anummap[num] = str(w_to_n)
        w_to_n += 1

    newinput = []
    for line in finput:
        numidx = []
        for num in anum:
            idx = line.find(num)
            if idx != -1:
                numidx.append((idx,num))
            idx2 = line.rfind(num)
            if idx2 != -1:
                numidx.append((idx2, num))
        if numidx:
            numidx = sorted(numidx)
            line = line[:numidx[0][0]] + anummap[numidx[0][1]] + line[numidx[0][0] +1:]
            line = line[:numidx[-1][0]] + anummap[numidx[-1][1]] + line[numidx[-1][0] + 1:]
        newinput.append(line)
    do_sum(newinput)





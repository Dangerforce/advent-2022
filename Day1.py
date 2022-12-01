with open('input1.txt', 'r') as f:
    elves = []
    s= 0
    for e in f.readlines():
        if e[:-1].isnumeric():
            s =  int(e[:-1]) + s
        else:
            elves.append(s)
            s =0

    print("Part One")
    print(max(elves))
    print("Part Two")
    print(sum(sorted(elves,)[-3:]))

with open("input4.txt", 'r') as f:
    lst = f.readlines()
    print("Part one")
    print(sum([1 if (int(p.split(',')[0].split('-')[0]) - int(p.split(',')[1].split('-')[0])) * (int(p.split(',')[0].split('-')[1]) - int(p.split(',')[1].split('-')[1])) <=0
    else 0
    for p in 
    lst]))

    print("Part Two")
    print(sum([1 if (int(p.split(',')[0].split('-')[0]) - int(p.split(',')[1].split('-')[1])) * (int(p.split(',')[1].split('-')[0]) - int(p.split(',')[0].split('-')[1])) >= 0
    else 0
    for p in 
    lst]))


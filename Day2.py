
with open('input2.txt', 'r') as f:
    lst = f.readlines()
    print("Part One")
    print(sum([(((ord(a.split()[1]) - ord(a.split()[0]) + 23) % 3) * 3) + ord(a.split()[1]) % 4 + 1 for a in lst]))

    print("Part Two")
    print(sum([((ord(a.split()[1]) % 4) *3) +  (65 + (ord(a.split()[0]) -65 + ((ord(a.split()[1])+1)%3) ))%4 for a in lst]))

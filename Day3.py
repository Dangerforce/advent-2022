
with open('input3.txt', 'r') as f:
        
        lst = f.readlines()
        print("Part One")
        print(sum([x -96 if x >= 97 else x-38 for x in [ ord(list(set(s[:int(len(s)/2)]).intersection(s[int(len(s)/2):]))[0]) for s in lst]]))
        print("Part Two")
        print(sum([x -96 if x >= 97 else x-38 for x in[ord(list(set(g[0][:-1]).intersection(g[1][:-1]).intersection(g[2][:-1]))[0]) for g in [lst[i:i+3] for i in range(0, len(lst), 3)]]]))
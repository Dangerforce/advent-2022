with open('input6.txt', 'r') as f:
    s = f.readlines()[0]
    for i in range(len(s)):
        if len(set(s[i:i+14])) == 14:
            print(i+14)
            break
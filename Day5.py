import re

with open('input5.txt', 'r') as f:
    lst = f.readlines()
    stackMap = [re.split(r'(\s+)', row) for row in lst[:8]]
    stacks = ['','','','','','','','','']
    for s in stackMap:
        i = 0
        for item in s:
            if '\n' in item:
                break
            if item[0]=='[':
                stacks[i] += item[1]
                i+=1
                            
            i+= int(len(item) /4)
inst = lst[10:]
for m in inst:
    move, frm, to = [int(n) for n in m.split() if n.isnumeric()]
    #for part 1 keep [::-1] (reverses list) for part 2 remove that part
    stacks[to-1] = stacks[frm-1][:move][::-1]+ stacks[to-1]
    stacks[frm-1] = stacks[frm-1][move:]
  

print(''.join([s[0] for s in stacks]))

    


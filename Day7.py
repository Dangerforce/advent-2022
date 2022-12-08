class Directory:
    def __init__(self, n = '/', p = None):
        self.name = n
        self.children = {}
        self.mem = 0
        self.parent = p
    def addChild(self, dir):
        self.children[dir] = Directory(n = dir,p=self)
    def memory(self):
        return self.mem + sum([v.memory() for k,v in self.children.items()])

class FilePointer:
    def __init__(self, current=None):
        self.cur = current
    def cd(self, inst):
        if inst == '..':
            self.cur = self.cur.parent
        else:
            self.cur = self.cur.children[inst]

    def ls(self, instructions = []):
        for inst in instructions:
            if inst.split()[0] == 'dir':
                self.cur.addChild(inst.split()[1])
            else:
                self.cur.mem += int(inst.split()[0])

files = []
def filesizes(root):
    global files
    files.append(root.memory())
    for child in root.children.values():
        files.append(filesizes(child))
    

with open('input7.txt','r') as f:

    lst = f.readlines()[1:]
    root = Directory('/')
    fp = FilePointer(root)
    for i in range( len(lst)):
        if lst[i][0] == '$':
            command = lst[i].split()
            if command[1] == 'cd':
                fp.cd(command[2])
            if command[1] == 'ls':
                j = i+1
                contents = []
                while j<len(lst) and lst[j][0] != '$':
                    contents.append(lst[j])
                    j+=1
                fp.ls(instructions = contents)

    filesizes(root)
    print("Part One")
    print(sum([k for k in [f for f in files if f] if k <=100000]))

    print("Part Two")
    free = 70000000-root.memory()
    deficit = 30000000 - free
    print(min([k for k in [f for f in files if f] if k >= deficit]))


    




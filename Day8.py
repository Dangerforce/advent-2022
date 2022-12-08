with open("input8.txt")as f:
    trees = [[int(y) for y in x.strip()] for x in f.readlines()]

    visible = (2 * len(trees)) + (2 * (len(trees[0]) - 2))
    distance = 0

    for y, row in enumerate(trees):
        if y == 0 or y == (len(trees) - 1):
            continue
        for x, col in enumerate(row):
            if x == 0 or x == (len(row) - 1):
                continue
            tree = trees[y][x]
            up = [tree > row[x] for row in trees[:y]]
            uDirec = sorted((y - i) if tree <= row[x] else y for i, row in enumerate(trees[:y]))
            down = [tree > row[x] for row in trees[y + 1:]]
            dDirec = sorted((i + 1) if tree <= row[x] else (len(trees) - y - 1) for i, row in enumerate(trees[y + 1:]))
            left = [tree > col for col in trees[y][:x]]
            lDirec = sorted((x - i) if tree <= col else x for i, col in enumerate(trees[y][:x]))
            right = [tree > col for col in trees[y][x + 1:]]
            rDirec =sorted((i + 1) if tree <= col else (len(trees[0]) - x - 1) for i, col in enumerate(trees[y][x + 1:]))
            if all(up) or all(down) or all(left) or all(right):
                visible += 1
            if uDirec[0] * dDirec[0] * lDirec[0] * rDirec[0] > distance:
                distance = uDirec[0] * dDirec[0] * lDirec[0] * rDirec[0]

    print(f"Part one: {visible} | Part two: {distance}")

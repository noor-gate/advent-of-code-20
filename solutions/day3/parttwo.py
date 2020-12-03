def calc_trees(right, down):
    f = open("input.txt", "r")
    lines = f.readlines()
    trees = 0
    pos = 0
    for c, line in enumerate(lines):
        if c % down == 0:
            line = line.strip()
            if line[pos] == '#':
                trees += 1
            pos += right
            pos = pos % len(line)
        else:
            continue
    return trees    
    
print(calc_trees(1, 2) * calc_trees(1, 1) * calc_trees(3, 1) * calc_trees(5, 1) * calc_trees(7, 1))

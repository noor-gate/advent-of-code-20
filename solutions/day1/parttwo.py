file = open("input.txt", "r");
lines = file.readlines();
sums = {}
finished = False

for line in lines:
    curr = int(line)
    value = 2020 - curr
    for line in lines:
        key = int(line)
        sums[key] = value - key
    for line in lines:
        key = int(line)
        if sums[key] in sums:
            print(sums[key] * key * curr)
            finished = True
            break
    if finished:
        break
    sums = {}    


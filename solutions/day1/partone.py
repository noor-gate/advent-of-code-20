file = open("input.txt", "r");
lines = file.readlines();
sums = {}

for line in lines:
    key = int(line)
    sums[key] = 2020 - key

for line in lines:
    key = int(line)
    if sums[key] in sums:
        print(sums[key] * key)
        break

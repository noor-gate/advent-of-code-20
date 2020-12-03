f = open("input.txt", "r")
lines = f.readlines()

pos = 3
trees = 0

for c, line in enumerate(lines):
    if c == 0:
        continue
    while pos >= len(line):
        line = line.rstrip('\n') + line
    if line[pos] == '#':
        trees += 1
    pos += 3
print(trees)

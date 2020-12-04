f = open("input.txt", "r")
lines = f.readlines()

fields = {}
valid = 0

for line in lines:
    if line == '\n':
        if len(fields) == 8 or (len(fields) == 7 and 'cid' not in fields):
            valid += 1
        fields = {}
        continue
    vals = line.split(" ")
    for val in vals:
        fields[val.split(":")[0]] = val.split(":")[1]

if len(fields) == 8 or (len(fields) == 7 and 'cid' not in fields):
            valid += 1
print(valid)
        

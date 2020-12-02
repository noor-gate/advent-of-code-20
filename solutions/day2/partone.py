def get_bounds(s):
    nums = s.split("-")
    return nums[0], nums[1]

def get_letter(s):
    return s[:1]

f = open("input.txt", "r")
lines = f.readlines()
valid = 0
for line in lines:
    split_line = line.split(" ")
    low, high = get_bounds(split_line[0])
    letter = get_letter(split_line[1])
    pw = split_line[2]
    count = 0
    for p in pw:
        if p == letter:
            count += 1
    if count <= int(high) and count >= int(low):
        valid += 1
print(valid)        


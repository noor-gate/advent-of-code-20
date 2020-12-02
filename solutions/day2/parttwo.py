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
    first, second = get_bounds(split_line[0])
    letter = get_letter(split_line[1])
    pw = split_line[2]
    count = 0
    if pw[int(first) - 1] == letter:
        count += 1
    if pw[int(second) - 1] == letter:
        count += 1
    if count == 1:
        valid += 1
print(valid)        


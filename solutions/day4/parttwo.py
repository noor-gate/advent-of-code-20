import re

def ch_hgt(height):
    height = height.strip()
    num = int(height[:len(height) - 2])
    if height[-2:] == "cm":
        return num >= 150 and num <= 193
    if height[-2:] == "in":
        return num >= 59 and num <= 76
    return False

def ch_pres(fields):
    return len(fields) == 8 or (len(fields) == 7 and 'cid' not in fields)

def ch_byr(year):
    return year >= 1920 and year <= 2002

def ch_iyr(year):
    return year >= 2010 and year <= 2020

def ch_eyr(year):
    return year >= 2020 and year <= 2030

def ch_hcl(color):
    color = color.strip()
    if len(color) != 7:
        return False
    for i, c in enumerate(color):
        if i == 0 and c != '#':
            return False
        if i > 0 and (not re.compile("[a-f0-9]").fullmatch(c)):
            return False
    return True

def ch_ecl(color):
    color = color.strip()
    return color in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

def ch_pid(pid):
    pid = pid.strip()
    return len(pid) <= 9 and pid.isnumeric()
     
f = open("input.txt", "r")
lines = f.readlines()

fields = {}
valid = 0

for line in lines:
    if line == '\n':
        if ch_pres(fields):        
            if ch_byr(int(fields['byr'])) and ch_iyr(int(fields['iyr'])) and ch_eyr(int(fields['eyr'])) and ch_hgt(fields['hgt']) and ch_hcl(fields['hcl']) and ch_ecl(fields['ecl']) and ch_pid(fields['pid']):
                valid += 1
        fields = {}
        continue
    vals = line.split(" ")
    for val in vals:
        fields[val.split(":")[0]] = val.split(":")[1].rstrip("\n")

if ch_pres(fields):
    if ch_byr(int(fields['byr'])) and ch_iyr(int(fields['iyr'])) and ch_eyr(int(fields['eyr'])) and ch_hgt(fields['hgt']) and ch_hcl(fields['hcl']) and ch_ecl(fields['ecl']) and ch_pid(fields['pid']):
        valid += 1 

print(valid)
        

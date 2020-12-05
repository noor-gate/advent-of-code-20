f = open("input.txt", "r")
lines = f.readlines()

highest_id = 0

for line in lines:
    lr = 0
    hr = 127
    lc = 0
    hc = 7
    for i in range(6):
        if line[i] == 'F':
            hr = lr + (hr - lr) // 2
        if line[i] == 'B':
            lr = hr - (hr - lr) // 2
    if line[6] == 'F':
        row = lr
    else:
        row = hr

    for i in range(7, 9):
        if line[i] == 'L':
            hc = lc + (hc - lc) // 2
        if line[i] == 'R':
            lc = hc - (hc - lc) // 2
    if line[9] == 'L':
        col = lc
    else:
        col = hc

    seat_id = row * 8 + col
    if seat_id > highest_id:
        highest_id = seat_id

print(highest_id)

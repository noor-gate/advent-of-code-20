f = open("input.txt", "r")
lines = f.readlines()

highest_id = 0
rows = {}
cols = {}

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

    if row in rows:
        rows[row] = rows[row] + 1
    else:
        rows[row] = 1

    for i in range(7, 9):
        if line[i] == 'L':
            hc = lc + (hc - lc) // 2
        if line[i] == 'R':
            lc = hc - (hc - lc) // 2
    if line[9] == 'L':
        col = lc
    else:
        col = hc

    if col in cols:
        cols[col] = cols[col] + 1
    else:
        cols[col] = 1

for row in rows:
    if rows[row] == 7:
        print("row: " + str(row) + ", " + str(rows[row]))

for col in cols:
    if cols[col] < 128:
        print("col: " + str(col) + ", " + str(cols[col]))

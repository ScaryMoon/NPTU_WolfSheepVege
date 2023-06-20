
n = int(input("輸入維度n:"))

row = 0
col = int(n/2)
m[row][col] = 1
for i in range(2,  n * n + 1):
    rowtest = (row-1) % n
    coltest = (col+1) % n
    if m[rowtest][coltest] == 0:
        row = rowtest
        col = coltest
        m[row][col] = i
    else:
        row = row+1
        m[row][col] = i
for i in range(n):
    print(f"{m[i]}")

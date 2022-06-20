p = input("input n*n shape n=")
n = int(p)
ss = []
for i in range(n + 1):
    ss.append([0] * (n + 1))
i = 0
j = (n + 1) // 2
for key in range(1, n ** 2 + 1):
    if key % n == 1:
        i += 1
    else:
        i -= 1
        j += 1
    if i == 0:
        i = n
    if j > n:
        j = 1
    ss[i][j] = key
m = []
for i in range(n):
    m.append([0] * n)
for k in range(len(m)):
    for l in range(len(m[0])):
        m[k][l] = ss[k + 1][l + 1]

print(m)

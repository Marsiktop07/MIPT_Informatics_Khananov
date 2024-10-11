n, m =map(int, input().split())
a = [[0 for i in range(m)] for j in range(n)]
for i in range(n):
    a[i] = list(map(int, input().split()))

max_ = 0

for i in range(n-2, 0, -1):
    for j in range(m - 2, 0, -1):
        if a[i][j] != 0:
            a[i][j] = min(a[i + 1][j] + 1, a[i + 1][j + 1] + 1, a[i][j + 1] + 1)
        max_ = max(a[i][j], max_)
print(max_)


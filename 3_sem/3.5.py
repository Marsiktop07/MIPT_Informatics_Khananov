import numpy as np
import sys
sys.setrecursionlimit(10**6)
n, m = list(map(int, input().split()))
k = m
a = np.array([[0] * n] * m)
def f(a, n, m, nn = 0, mn = 0, j = 1):
    for i in range(nn, n):
        if a[nn][i] != 0:
            return
        a[nn][i] = j
        j += 1
    mn += 1
    for i in range(mn, m):
        if a[i][n - 1] != 0:
            return
        a[i][n - 1] = j
        j += 1
    n -= 1
    for i in range(n - 1, nn - 1, -1):
        if a[m - 1][i] != 0:
            return
        a[m - 1][i] = j
        j += 1
    m -= 1
    for i in range(m - 1, mn - 1, -1):
        if a[i][nn] != 0:
            return
        a[i][nn] = j
        j += 1
    nn += 1
    if a.all():
        return
    f(a, n, m, nn = nn, mn = mn, j = j)
f(a, n, m)
for i in range(k):
    a[i] = a[i] * (i + 1)

print(a)
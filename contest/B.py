import sys
sys.setrecursionlimit(10**6)
min_ = []
min_2 = float('inf')
def f(n, k, l = 0, s = ''):
    global min_2
    if k == n:
        min_.append(s)
        min_2 = min(min_2, len(s))
        return len(s)
    elif k > n:
        return float('inf')
    elif len(s) >= min_2:
        return float('inf')
    return min(f(n, k * 3, s = s + '3'), f(n, k * 2, s = s + '2'), f(n, k + 1, s = s + '1'))

print(f(int(input()), 1))
k = list(str(min(min_, key=lambda x: len(x))))
c = 1
ans = [c]
for i in k:
    if i == '1':
        c += 1
        ans.append(c)
    elif i == '2':
        c *= 2
        ans.append(c)
    elif i == '3':
        c *= 3
        ans.append(c)

print(*ans)


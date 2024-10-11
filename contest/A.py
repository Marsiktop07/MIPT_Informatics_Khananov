def f(n, k):
    if n == 1 and k == 1:
        return 1
    if n < 1 or k < 1:
        return 0
    return f(n - 1, k - 2) + f(n - 2, k - 1)

n, k = list(map(int, input().split()))
print(f(n, k))
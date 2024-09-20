N = int(input())
b = int(input())
c = int(input())

def f(N, b, c):
    n = str(N)[::-1]
    ans = 0
    k = ''
    for i in range(len(n)):
        ans += int(n[i]) * (b ** i)
    while ans != 0:
        k += str(ans % c)
        ans //= c
    return k[::-1]

print(int(f(N, b, c)))
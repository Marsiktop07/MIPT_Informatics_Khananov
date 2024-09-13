f = open('input2.txt', 'r')
a = list(map(int, f.readline().split()))
s = list(map(str, f.readline()))
s = s[0]
z = int(f.readline())
print(z)
print(s)

def toten(N, c):
    n = str(N)[::-1]
    ans = 0
    for i in range(len(n)):
        ans += int(n[i]) * (c ** i)
    return ans

def tcs(ans, c):
    k = ''
    while ans != 0:
        k += str(ans % c)
        ans //= c
    return k[::-1]

f = open('output.txt', 'w')
for i in range(len(a)):
    a[i] = toten(a[i], z)
if s == '+':
    ans = sum(a)
    f.write(tcs(ans, z))
    print(tcs(ans, z))
elif s == '-':
    ans = a[0]
    for i in range(1, len(a)):
        ans -= a[i]
    f.write(tcs(ans, z))
    print(tcs(ans, z))
elif s == '*':
    ans = 1
    for i in a:
        ans *= i
    f.write(tcs(ans, z))
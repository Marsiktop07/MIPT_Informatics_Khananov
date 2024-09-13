g = open('input.txt', 'r')
a = list(map(int, g.readline().split()))
s = str(g.readline())
f = open('output.txt', 'w')
if s == '+':
    e = 0
    for i in a:
        e += i
        print(i, e)
    f.write(str(e))
elif s == '-':
    ans = a[0]
    for i in range(1, len(a)):
        ans -= a[i]
    f.write(str(ans))
elif s == '*':
    print(1)
    ans = 1
    for i in a:
        ans *= i
    f.write(str(ans))
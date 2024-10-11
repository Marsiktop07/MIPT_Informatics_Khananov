ch = list(map(int, input().split()))
n = ch[0]
del ch[0]
a = (i for i in range(1, 55))
a = set(a)
ch = set(ch)
print(min(a - ch))
ch, s = input().split()
ch = int(ch)
ans = ''
for i in range(0, len(s), ch):
    ans += s[i: ch+i][::-1]
print(ans)
import math
a = list(map(int, input().split()))
ans = 1
for i in a:
    ans *= i
print(ans ** (1 / len(a)))
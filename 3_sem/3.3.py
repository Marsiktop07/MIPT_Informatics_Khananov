a, b = list(map(int, input().split()))
k1, k2 = a, b

while k1 != 0 and k2 != 0:
    if k1 > k2:
        k1 = k1 % k2
    else:
        k2 = k2 % k1
d = k1 + k2
x1, y1, x2, y2 = 0, 0, 0, 0
while (a * x1 + b * y1 != d) or (y1 != int(y1)):
    x1 += 1
    y1 = (d - a * x1) / b

while (a * x2 + b * y2 != d) or (x2 != int(x2)):
    y2 += 1
    x2 = (d - b * y2) / a

if abs(x1) + abs(y1) < abs(x2) + abs(y2):
    print(x1, int(y1), d)
else:
    print(int(x2), y2, d)
a = int(input())
b = list(map(int, input().split()))
if sum(b) % 3 != 0:
    print(0)
else:
    b.sort()
    print(b)

# Задача о рюкзаке
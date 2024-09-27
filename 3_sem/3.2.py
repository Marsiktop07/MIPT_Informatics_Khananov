import time, sys
sys.setrecursionlimit(10**9)
a = int(input())

t = time.time()
def simple(a, i = 2):
    if a == 1:
        return
    if a % i == 0:
        print(i)
        simple(a // i, i)
    elif a % i != 0:
        return simple(a, i = i + 1)
simple(a)
print(time.time() - t)

# i = 2
# while a != 1:
#     while a % i == 0:
#         print(i)
#         a = a // i
#     i += 1
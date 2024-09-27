a, b = list(input().split())
a = int(a)

def triangle(h, symbol, depth = 1):
    if h % 2 != 0 and depth == h // 2 + 1:
        print(symbol * depth)
        return
    if h % 2 == 0 and depth == h // 2:
        print(symbol * depth)
        print(symbol * depth)
        return
    print(symbol * depth)

    triangle(h, symbol, depth = depth + 1)

    print(symbol * depth)
    return

triangle(a, b)
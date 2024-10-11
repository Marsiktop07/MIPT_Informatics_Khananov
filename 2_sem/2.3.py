s = 'AHIMOTUVWXY18EJSZ'
a = str(input())
ans = a
a = a.replace('3', 'E')
a = a.replace('L', 'J')
a = a.replace('2', 'S')
a = a.replace('5', 'Z')


is_palindrom = False
if len(a) % 2 == 0:
    if ans[:len(a) // 2] == ans[len(a) // 2:]:
        is_palindrom = True
elif len(a) % 2 == 1:
    if (ans[:len(a) // 2] == ans[len(a) // 2 + 1:]):
        is_palindrom = True
for i in list(a):
    is_mirrored = True
    if i not in s:
        is_mirrored = False
        break
if is_mirrored and is_palindrom:
    print(f'{ans} is a mirrored palindrome.')
elif is_palindrom and not(is_mirrored):
    print(f'{ans} is a regular palindrome.')
elif not(is_palindrom) and is_mirrored:
    print(f'{ans} is a mirrored string.')
elif not(is_mirrored) and not(is_palindrom):
    print(f'{ans} is not a palindrome.')
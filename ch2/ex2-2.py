x = int(input())
y = int(input())
z = int(input())

ans = 0
if x % 2 != 0 and x > ans:
    ans = x
if y % 2 != 0 and y > ans:
    ans = y
if z % 2 != 0 and z > ans:
    ans = z

if ans != 0:
    print(ans)
else:
    print('no positive odd numbers')


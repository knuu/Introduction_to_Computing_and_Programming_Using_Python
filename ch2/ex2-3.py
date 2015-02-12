ans = 0
i = 0
while i < 10:
    num = int(input())
    if num % 2 != 0 and num > ans:
        ans = num
    i = i + 1

if ans != 0:
    print(ans)
else:
    print('no positive odd numbers')

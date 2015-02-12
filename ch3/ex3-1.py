n = int(input())
i = 5
while i > 0:
    root = 1
    while root ** i < n:
        root = root + 1
    if root ** i == n:
        print(root, i)
    i = i - 1

s = input()
i = 0
ans = 0
while i < len(s):
    start = i
    end = i
    while end < len(s) and s[end] != ',':
        end = end + 1
    ans = ans + float(s[start:end])
    i = end + 1
print(ans)

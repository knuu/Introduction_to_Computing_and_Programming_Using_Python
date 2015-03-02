# 立方根を求める
x = -257
n = 3
epsilon = 0.01
numGuess = 0
if x < 0:
    low = min(x, -1.0)
high = max(1.0, x)
ans = (high + low) / 2.0
while abs(ans ** n - x) >= epsilon:
    print('low =', low, 'high =', high, 'ans =', ans) 
    if ans ** n < x:
        low = ans
    else:
        high = ans
    ans = (high + low) / 2.0
    numGuess += 1
print(ans, 'is close to', n, '- th root of', x)

x = 25
epsilon = 0.01
numGuess = 0
low = 0.0
high = max(1.0, x)
ans = (high + low) / 2.0
while abs(ans ** 2 - x) >= epsilon:
    print('low =', low, 'high =', high, 'ans =', ans) 
    if ans ** 2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low) / 2.0
    numGuess += 1
print(ans, 'is close to square root of', x)

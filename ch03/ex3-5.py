# Newton法と二分法の比較

x = 100.0
epsilon = 0.01

# Newton法(2次)
guess = x / 2.0
newton = 0 # Newton法の試行回数
while abs(guess ** 2 - x) >= epsilon:
    guess = guess - (guess ** 2 - x) / (2 * guess)
    newton += 1
print('Square root of', x, 'is about', guess)



# 二分法
numGuess = 0
low = 0.0
high = max(1.0, x)
ans = (high + low) / 2.0
while abs(ans ** 2 - x) >= epsilon:
    if ans ** 2 < x:
        low = ans
    else:
        high = ans
    ans = (high + low) / 2.0
    numGuess += 1
print(ans, 'is close to square root of', x)

print('Newton Method:', newton)
print('Bisection Search:', numGuess)

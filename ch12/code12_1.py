import random

def rollDie():
    """1 から 6 までの整数を無作為に選んで出力する"""
    return random.choice([1,2,3,4,5,6])
def rollN(n):
    result = ''.join(str(rollDie()) for _ in range(n))
    print(result)

rollN(10)
                     
                         

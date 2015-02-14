def findAnEven(l):
    """lをint型の要素を持つリストとする
       lに最初に現れる偶数を返す
       lが偶数を含まなければValueErrorを引き起こす"""
    for x in l:
        if x % 2 == 0:
            return x
    raise ValueError


print(findAnEven([1,2,3]))
try:
    findAnEven([1,3,5])
except ValueError:
    print('ValueError')

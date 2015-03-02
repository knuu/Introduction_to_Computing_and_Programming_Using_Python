def sumDigit(s):
    """sを文字列とする.
       sの中の数字の合計を返す.
       例えば, sが'a2b3c'ならば5を返す"""
    ret = 0
    for d in s:
        try:
            ret += int(d)
        except ValueError:
            pass
    return ret

print(sumDigit('a2b3c') == 5)
            

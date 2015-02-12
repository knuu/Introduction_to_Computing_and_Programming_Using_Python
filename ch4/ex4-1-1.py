def isIn(s, t):
    if len(s) > len(t):
        s, t = t, s
    for i in range(0, len(t)-len(s)+1):
        if s == t[i:i+len(s)]:
            return True
    return False

if __name__ == '__main__':
    print(isIn('hogefugafoobar', 'foobar'))
    print(isIn('hoge', 'foo'))

          
        

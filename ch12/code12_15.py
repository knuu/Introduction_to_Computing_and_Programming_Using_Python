import random, pylab

#Page 196
def collisionProb(n, k):
    prob = 1.0
    for i in range(1, k):
        prob = prob * ((n - i)/float(n))
    return 1 - prob

#Page 197, Figure 12.15
def simInsertions(numIndices, numInsertions):
    """numIndices と numInsertions は正の整数
       衝突が起これば 1 そうでなければ 0 を出力する"""
    choices = range(numIndices) # キーの候補となるリスト 
    used = []
    for i in range(numInsertions):
        hashVal = random.choice(choices)
        if hashVal in used: # 衝突あり
            return 1
        else:
            used.append(hashVal)
    return 0

def findProb(numIndices, numInsertions, numTrials):
    collisions = 0.0
    for t in range(numTrials):
        collisions += simInsertions(numIndices, numInsertions)
    return collisions/numTrials

#Page 197
print('Actual probability of a collision =', collisionProb(1000, 50))
print('Est. probability of a collision =', findProb(1000, 50, 10000))
print('Actual probability of a collision =', collisionProb(1000, 200))
print('Est. probability of a collision =', findProb(1000, 200, 10000))

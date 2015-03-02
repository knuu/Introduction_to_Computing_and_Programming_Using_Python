import pylab, random

#Page 179
def stdDev(X):
    """X を数のリストとする
       Xの標準偏差を出力する"""
    mean = float(sum(X))/len(X)
    tot = 0.0
    for x in X:
        tot += (x - mean)**2
    return (tot/len(X))**0.5 # 平均との差の二乗根

#Page 182
def CV(X):
    """X を数のリストとする
       Xの変動係数を出力する"""
    mean = sum(X)/len(X)
    try:
        return stdDev(X)/mean
    except ZeroDivisionError:
        return float('nan')

#Page 201
class Location(object):

    def __init__(self, x, y):
        """x and y are floats"""
        self.x = x
        self.y = y

    def move(self, deltaX, deltaY):
        """deltaX and deltaY are floats"""
        return Location(self.x + deltaX, self.y + deltaY)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def distFrom(self, other):
        ox = other.x
        oy = other.y
        xDist = self.x - ox
        yDist = self.y - oy
        return (xDist**2 + yDist**2)**0.5

    def __str__(self):
        return '<' + str(self.x) + ', ' + str(self.y) + '>'

#Page 202
class Field(object):
    
    def __init__(self):
        self.drunks = {}
        
    def addDrunk(self, drunk, loc):
        if drunk in self.drunks:
            raise ValueError('Duplicate drunk')
        else:
            self.drunks[drunk] = loc
            
    def moveDrunk(self, drunk):
        if drunk not in self.drunks:
            raise ValueError('Drunk not in field')
        xDist, yDist = drunk.takeStep()
        currentLocation = self.drunks[drunk]
        # Loaction クラスの move メソッドを用いて, 新しい位置情報を得る
        self.drunks[drunk] = currentLocation.move(xDist, yDist)
        
    def getLoc(self, drunk):
        if drunk not in self.drunks:
            raise ValueError('Drunk not in field')
        return self.drunks[drunk]

#Page 202
class Drunk(object):
    def __init__(self, name = None):
        """name は文字列とする"""
        self.name = name

    def __str__(self):
        if self != None:
            return self.name
        return 'Anonymous'

class UsualDrunk(Drunk):
    def takeStep(self):
        stepChoices = [(0.0,1.0), (0.0,-1.0), (1.0, 0.0), (-1.0, 0.0)]
        return random.choice(stepChoices)

#Page 203(バグなし)
def walk(f, d, numSteps):
    """f: Field クラスのオブジェクト
       d: Drunk クラスのオブジェクト
       numSteps: 0 以上の整数
       dをnumSteps回移動し, 酔歩の初期位置と最終位置との差を出力する. """
    start = f.getLoc(d)
    for s in range(numSteps):
        f.moveDrunk(d)
    return start.distFrom(f.getLoc(d))

def simWalks(numSteps, numTrials, dClass):
    """numSteps: 0 以上の整数
       numTrials: 正の整数
       dClass: Drunk型のサブクラス
       各実験の初期位置と最終位置との差をリストにして出力する. """
    Homer = dClass()
    origin = Location(0.0, 0.0)
    distances = []
    for t in range(numTrials):
        f = Field()
        f.addDrunk(Homer, origin)
        distances.append(walk(f, Homer, numSteps))
    return distances

def drunkTest(walkLengths, numTrials, dClass):
    """walkLength: 0 以上の整数シークエンス
       numTrials: 正の整数
       dClass: Drunk型のサブクラス
       walkLength の各要素を酔歩の移動回数として, numTrials 回の酔歩を
       シミュレートする simWalks を実行し, 結果を出力する. """
    means = []
    for numSteps in walkLengths:
        distances = simWalks(numSteps, numTrials, dClass)
        print(dClass.__name__, 'random walk of', numSteps, 'steps')
        print(' Mean =', sum(distances)/len(distances), 'CV =', CV(distances))
        print(' Max =', max(distances), 'Min =', min(distances))
        means.append(sum(distances)/len(distances))

    styleChoice = styleIterator(('b-', 'r:', 'm-.'))
    curStyle = styleChoice.nextStyle()
    pylab.plot(walkLengths, means, curStyle,
               label = 'Distance form origin')
    pylab.plot(walkLengths, [pow(x, 0.5) for x in walkLengths],
               styleChoice.nextStyle(),
               label = 'Square root of steps')
    pylab.title('Average Distance from Origine ({} trials)'.format(numTrials))
    pylab.xlabel('Number of Steps')
    pylab.ylabel('Distance from Origin')
    pylab.legend(loc = 'best')
    pylab.semilogx()
    pylab.semilogy()
    pylab.show()
    
        
#Page 207
class styleIterator(object):
    def __init__(self, styles):
        self.index = 0
        self.styles = styles

    def nextStyle(self):
        result = self.styles[self.index]
        if self.index == len(self.styles) - 1:
            self.index = 0
        else:
            self.index += 1
        return result

drunkTest((10, 100, 1000, 10000, 100000), 100, UsualDrunk)


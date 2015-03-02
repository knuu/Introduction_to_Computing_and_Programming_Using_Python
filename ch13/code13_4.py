#Page 203, Figure 13.4(バグなし)
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
    for numSteps in walkLengths:
        distances = simWalks(numSteps, numTrials, dClass)
        print(dClass.__name__, 'random walk of', numSteps, 'steps')
        print(' Mean =', sum(distances)/len(distances), 'CV =', CV(distances))
        print(' Max =', max(distances), 'Min =', min(distances))

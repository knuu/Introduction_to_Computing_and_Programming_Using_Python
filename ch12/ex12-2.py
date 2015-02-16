import random
import pylab

def flipPlot(minExp, maxExp):
    """minExp と maxExp は minExp < maxExp を満たす正の整数とする
       2**minExp から 2**maxExp 回のコイン投げの結果をプロットする"""

    ratios = []
    diffs = []
    xAxis = []
    for exp in range(minExp, maxExp + 1):
        xAxis.append(2**exp)
    for numFlips in xAxis:
        numHeads = 0
        for n in range(numFlips):
            if random.random() < 0.5:
                numHeads += 1
        numTails = numFlips - numHeads
        ratios.append(numHeads/float(numTails))
        diffs.append(abs(numHeads - numTails))
    pylab.title('Difference Between Heads and Tails')
    pylab.xlabel('Number of Flips')
    pylab.ylabel('Abs(#Heads - #Tails)')
    pylab.semilogx()
    pylab.semilogy()
    pylab.plot(xAxis, diffs, 'bo')
#    pylab.show()
    pylab.figure()
    pylab.title('Heads/Tails Ratios')
    pylab.xlabel('Number of Flips')
    pylab.ylabel('#Heads/#Tails')
    pylab.semilogx()
    pylab.plot(xAxis, ratios, 'bo')
#    pylab.show()

random.seed(0)
flipPlot(4, 20)

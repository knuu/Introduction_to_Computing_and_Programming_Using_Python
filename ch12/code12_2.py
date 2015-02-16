import random

def flip(numFlips):
    heads = sum([1 for _ in range(numFlips) if random.random() < 0.5])
    return heads / numFlips

def flipSim(numFlipsPerTrial, numTrial):
    fracHeads = [flip(numFlipsPerTrial) for _ in range(numTrial)]
    mean = sum(fracHeads) / len(fracHeads)
    return mean

print(flipSim(100,1), flipSim(100, 1))
print(flipSim(100,100), flipSim(100, 100))
print(flipSim(100,100000), flipSim(100, 100000))

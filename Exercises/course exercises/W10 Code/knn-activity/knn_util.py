import random
import sample

def genDistribution(xMean, xSD, yMean, ySD, n, namePrefix):
    samples = []
    for s in range(n):
        x = random.gauss(xMean, xSD)
        y = random.gauss(yMean, ySD)
        samples.append(sample.Sample(namePrefix+str(s), [x, y]))
    return samples

def label(E):
    return E.getLabel()

def make_cmap():
    colors = ('b', 'g', 'r', 'c', 'm', 'y', 'k')
    return colors

def make_cmarkers():
    markers = ('o', 'v', '^', '<', '>', '8', 
               's', 'p', '*', 'h', 'H', 'D', 'd')
    return markers


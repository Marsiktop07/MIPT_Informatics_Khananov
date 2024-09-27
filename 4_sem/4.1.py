from numpy import mean, array
import matplotlib.pyplot as plt

f = open('U(I).txt')
f = f.readlines()

def MNK(x, y):
    k = (mean(x * y) - mean(x) * mean(y)) / (mean(x ** 2) - mean(x) ** 2)
    b = mean(y) - k * mean(x)
    return k, b


for i in f:
    x, y = list(map(str, i.split('A')))
    x = array(list((map(int, x.split()))))
    y = array(list((map(int, y.split()))))
    plt.scatter(x, y)
    k, b = MNK(x, y)
    plt.plot(x, x * k + b)


plt.show()
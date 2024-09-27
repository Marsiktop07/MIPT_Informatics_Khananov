from numpy import mean, array
import matplotlib.pyplot as plt


x = array(list(map(int, input().split())))
y = array(list(map(int, input().split())))

def MNK(x, y):
    k = (mean(x * y) - mean(x) * mean(y)) / (mean(x ** 2) - mean(x) ** 2)
    b = mean(y) - k * mean(x)
    return k, b

k, b = MNK(x, y)
plt.scatter(x, y)
plt.plot(x, x * k + b)
plt.show()
print(k, b)
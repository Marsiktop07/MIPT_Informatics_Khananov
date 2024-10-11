import pandas as pd
import matplotlib.pyplot as plt
from numpy import mean, array


df = pd.read_csv('iris_data.csv')
sl = array(df['SepalLengthCm'])
sw = array(df['SepalWidthCm'])
pl = array(df['PetalLengthCm'])
pw = array(df['PetalWidthCm'])
sp = array(df['Species'])

def MNK(x, y):
    k = (mean(x * y) - mean(x) * mean(y)) / (mean(x ** 2) - mean(x) ** 2)
    b = mean(y) - k * mean(x)
    return k, b

fig = plt.figure(figsize = (16,9))
ax1 = fig.add_subplot(611)
ax2 = fig.add_subplot(612)
ax3 = fig.add_subplot(613)
ax4 = fig.add_subplot(614)
ax5 = fig.add_subplot(615)
ax6 = fig.add_subplot(616)

ax1.scatter(sl, sw)
k, b = MNK(sl, sw)
ax1.plot(sl, sl * k + b)
print(f'SepalLengthCm - SepalWidthCm: {float(k), float(b)}')

ax2.scatter(sl, pl)
k, b = MNK(sl, pl)
ax2.plot(sl, sl * k + b)
print(f'SepalLengthCm - PetalLengthCm: {float(k), float(b)}')

ax3.scatter(sl, pw)
k, b = MNK(sl, pw)
ax3.plot(sl, sl * k + b)
print(f'SepalLengthCm - PetalWidthCm: {float(k), float(b)}')

ax4.scatter(sw, pl)
k, b = MNK(sw, pl)
ax4.plot(sw, sw * k + b)
print(f'SepalWidthCm - PetalLengthCm: {float(k), float(b)}')

ax5.scatter(sw, pw)
k, b = MNK(sw, pw)
ax5.plot(sw, sw * k + b)
print(f'SepalWidthCm - PetalWidthCm: {float(k), float(b)}')

ax6.scatter(pl, pw)
k, b = MNK(pl, pw)
ax6.plot(pl, pl * k + b)
print(f'PetalLengthCm - PetalWidthCm: {float(k), float(b)}')


plt.show()





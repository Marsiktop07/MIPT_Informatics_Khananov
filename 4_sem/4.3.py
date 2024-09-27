import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('iris_data.csv')
sl = df['SepalLengthCm']
sw = df['SepalWidthCm']
pl = df['PetalLengthCm']
pw = df['PetalWidthCm']
sp = df['Species']

spdict = {}
for i in sp:
    if i not in spdict:
        spdict[i] = 1
    else:
        spdict[i] += 1

plls = [0, 0, 0]
for i in pl:
    if i < 1.2:
        plls[0] += 1
    elif 1.2 <= i <= 1.5:
        plls[1] += 1
    else:
        plls[2] += 1
fig = plt.figure(figsize = (16,9))
ax1 = fig.add_subplot(211)
ax2 = fig.add_subplot(212)

ax1.pie(list(spdict.values()), labels = list(spdict.keys()))
ax1.set_title('Доля разных видов (Species) ирисов в датасете')

ax2.pie(plls, labels = ['<1.2Cm', '>=1.2Cm and <=1.5Cm', '>1.5Cm'])
ax2.set_title('Ширина')
plt.show()
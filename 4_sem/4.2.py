import matplotlib.pyplot as plt
import numpy as np

pos = 0

# параметр отвечающий за разброс
scale = 10

# размер массива случайных чисел (сколько их сгенерируем)
size1 = 1000
size2 = size1 * 10
size3 = size2 * 10

# используем функцию из подраздела random библиотеки numpy и передадим наши параметры
values1 = np.random.normal(pos, scale*6, size1)
values2 = np.random.normal(pos, scale*3, size2)
values3 = np.random.normal(pos, scale, size3)

# строим гистограмму с 100 блоков
plt.hist(values1, 100)
plt.hist(values2, 1000)
plt.hist(values3, 10000)


plt.show()
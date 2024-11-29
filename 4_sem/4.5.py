import pandas as pd
import matplotlib.pyplot as plt
from numpy import array


df = pd.read_csv('BTC_data.csv')
cl = array(df['close'])
t = array(df['time'])
fig = plt.figure(figsize=(16, 9))
ax = fig.add_subplot(111)
# ax.scatter(t, cl)
ax.set_title('BTC Price')
ax.set_xlabel('Time')
ax.set_ylabel('Price')
ax.plot(t, cl)
plt.show()
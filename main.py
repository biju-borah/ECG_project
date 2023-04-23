import pandas as pd
import matplotlib.pyplot as plt

heartbeat = pd.read_csv('ecg_data.csv')
heartbeat.reset_index(drop=True)
# print(heartbeat['a'])

print(heartbeat.iloc[:, 0:2][0:129])
plt.plot(heartbeat['a'], heartbeat['b'])
plt.show()

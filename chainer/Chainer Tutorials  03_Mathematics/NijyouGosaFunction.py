import numpy as np
import matplotlib.pyplot as plt

np.random.seed(114514)

# 長さ
length = 100
# ノイズ
noise = np.r_[np.zeros(50), (np.random.rand(50) - 0.5) * 0.5]
print('Noise info')
print('Mean: ', str(np.mean(noise)))
print('Var: ', str(np.var(noise)))
print('Std: ', str(np.std(noise)))
# 実測データ
y = np.array([np.sin(2 * np.pi * i * 0.01) for i in range(length)]) + noise + 2
# 予測データ
y_pred = np.array([np.sin(2 * np.pi * i * 0.01) for i in range(length)]) + 2

# 可視化
plt.plot(y_pred)
plt.plot(y)
plt.show()

import matplotlib.pyplot as plt
import numpy as np


def line(x):
    return -2 * x + -50


n = 100

x = np.random.rand(n)

y = line(x) + np.random.random(n)

plt.scatter(x, y)

x_mean = x.mean()
y_mean = y.mean()

# 直線の傾き

# 分子
denominator = (x * y).sum() - n * x_mean * y_mean
# 分母
numerator = (x ** 2).sum() - n * x_mean ** 2

b = denominator / numerator

a = y_mean - b * x_mean

new_y = b * x + a

# xの標準偏差
x_sd = (((x ** 2).sum() - n * x_mean ** 2) / n) ** 0.5
# yの標準偏差
y_sd = (((y ** 2).sum() - n * y_mean ** 2) / n) ** 0.5
print(b, x_sd, y_sd)
# 相関係数
r = b * x_sd / y_sd
print(r)

# 相関係数を定義通りに計算したr
# 分子
denominator = ((x - x_mean) * (y - y_mean)).sum()
# 分母
numerator = (((x - x_mean) ** 2).sum()) ** 0.5 * (((y - y_mean) ** 2).sum()) ** 0.5

print(denominator / numerator)
plt.plot(x, new_y, color="g")
plt.show()
print(b, a)

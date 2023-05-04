import math
import numpy as np

n = 1000
p = 0.002
num_iter = 10000

lam = n * p
# 確率計算
# n件中何件取れるか
total = 0
for i in range(min(n, 40)):
    temp_p = np.exp(-lam) * lam ** i / math.factorial(i)
    total += temp_p
    print(f"{i}回:{round(temp_p, 5)} 累計:{total}")

result = np.zeros(n + 1)
for i in range(num_iter):
    result[(np.random.random(n) < p).sum()] += 1

print(f"期待値:{lam}")

print(f"実測値:{(result * np.arange(n + 1)).sum() / num_iter}")

import math
import random
import numpy as np

n = 10000
choice = 50
num_iter = 10000
p = 0.2

correct = int(n * p)
wrong = int(n * (1 - p))

base = [1] * correct + [0] * wrong

# 確率計算
cumulative = 0
all_combi = math.comb(n, choice)
for i in range(choice + 1):
    temp_p = math.comb(correct, i) * math.comb(wrong, choice - i) / all_combi
    cumulative += temp_p
    print(f"{i}個:{round(temp_p, 7)} 累計:{cumulative}")

# 実験
result = np.zeros(choice + 1)
for i in range(num_iter):
    c = random.sample(base, choice)
    result[sum(c)] += 1
print((result / num_iter).round(2))
print(f"期待値:{choice * correct / n}")
print(f"実測値平均:{(result[result != 0] * np.arange(choice + 1)[result != 0]).sum() / num_iter}")

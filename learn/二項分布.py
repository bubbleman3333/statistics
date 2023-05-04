import math

n = 50
p = 0.03
num_iter = 10000
# 確率計算

total = 0
for i in range(min(50, n + 1)):
    this_p = math.comb(n, i) * (p ** i) * ((1 - p) ** (n - i))
    total += this_p
    print(f"{i}回:{round(this_p, 5)} 累計:{total}")

import numpy as np

num_iter = 10000
p = 0.03

# 確率計算

total = 0
for i in range(1, 21):
    this_p = (1 - p) ** (i - 1) * p
    total += this_p
    print(f"{i}回目:{round(this_p, 2)},累計:{total}")

result = np.zeros(1000)

for i in range(num_iter):
    count = 0
    while True:
        count += 1
        if np.random.random() < p:
            result[count] += 1
            break
print((result / num_iter).round(2))

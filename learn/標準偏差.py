import math
import random


def print_value(t, val):
    print(f"{t}:{val}")


# とりあえずのデータ
x = [random.randint(1, 100) for _ in range(100000)]
print_value("データ", x)

# 平均
mean = round(sum(x) / len(x), 3)
print_value("平均", mean)

# 第一～第三分位点
temp = list(sorted(x))
p = len(x) / 4
for i in range(1, 4):
    print_value(f"第{i}分位点", temp[int(p * i)])

# 　分散
s2 = round((sum([k ** 2 for k in x]) - len(x) * (mean ** 2)) / len(x), 2)
print_value("分散", s2)

# 標準偏差
s1 = round(math.sqrt(s2), 2)
print_value("標準偏差", s1)

# 変動係数
cv = round(s1 / mean, 2)
print_value("変動係数", cv)
# 標準得点化
a = 1 / s1
b = mean / s1
z = [round(a * k - b, 2) for k in x]
# print_value("標準化", z)

standard_mean = round(sum(z) / len(z), 2)
print_value("標準化後平均", standard_mean)

standard_dispersion = round((sum([k ** 2 for k in z]) - len(z) * (standard_mean ** 2)) / len(z), 2)
print_value("標準化後分散", standard_dispersion)

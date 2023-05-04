import numpy as np

x = np.random.randint(1, 10, (2, 2))
y = np.random.randint(1, 10, (3, 2))

print(x)
print(y)

x = x[:, np.newaxis, :]
y = y[np.newaxis, :, :]

# print(x)
# print(y)
s = x + y
print(s)
print(s.shape)
print(s.sum(axis=2))

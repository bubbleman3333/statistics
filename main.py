import time

start = time.time()
temp = int(((10 ** 12) / 12) ** 0.5) + 1
print((temp ** 2) * 2 * 2 * 3 > 10 ** 12)
print(temp)
lim = temp ** 0.5
ll = list(range(2, temp + 1))
prime = []
while True:
    base = ll[0]
    if base > lim:
        break
    prime.append(base)
    ll = [k for k in ll if k % base != 0]

prime += ll
print(len(prime))
print(time.time() - start)

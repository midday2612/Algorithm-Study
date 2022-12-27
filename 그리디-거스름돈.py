N = 1260
coinType = [500, 100, 50, 10]
count = 0

for coin in coinType:
    count += N//coin
    N %= coin
print(count)

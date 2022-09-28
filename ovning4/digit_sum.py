def digi_sum(x):
    if x // 10 == 0:
        # x är ensiffrigt
        return x
    else:
        return x % 10 + digi_sum(x//10)

print(digi_sum(194))
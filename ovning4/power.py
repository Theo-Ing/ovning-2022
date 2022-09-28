def dumb_power(x, n):
    if n == 0:
        return 1
    else:
        return x * dumb_power(x, n-1)


def smart_power(x, n):
    if n == 0:
        return 1
    else:
        temp = smart_power(x, n // 2)
        if n % 2 == 1:
            rest = x
        else:
            rest = 1
        return temp*temp*rest


print(smart_power(2, 1000))

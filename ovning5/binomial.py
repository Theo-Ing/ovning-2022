PASCACHE = {}

def pascal(n, k):
    if k == n or k == 0:
        return 1
    if (n, k) in PASCACHE:
        return PASCACHE[(n, k)]
    value = pascal(n-1, k-1) + pascal(n-1, k)
    PASCACHE[(n, k)] = value
    return value

n = 6
for k in range(0, n+1):
    print(pascal(n, k))

import functools

cache = {}
def fib(n):
    if n == 1 or n == 0:
        return 1
    if n in cache:
        return cache[n]
    value = fib(n-1) + fib(n-2)
    cache[n] = value
    return value


@functools.lru_cache()
def cool_fib(n):
    if n == 0 or n == 1:
        return 1
    return cool_fib(n-1) + cool_fib(n-2)


print(cool_fib(70))
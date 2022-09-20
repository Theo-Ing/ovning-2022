def sin(x):
    limit = 0.00000001
    term = x
    summa = 0
    n = 1
    tecken = 1
    while term > limit:
        summa += tecken * term
        n += 2
        term = term * x*x / (n*(n-1))
        tecken *= -1
    print("Final term degree:", n-2)
    return summa

def main():
    value = float(input("x = "))
    result = sin(value)
    print("sin(x) =", result)

main()

def fakultet(n):
    produkt = 1
    for i in range(1, n+1):
        produkt *= i # produkt = produkt * i
    return produkt

def main():
    value = int(input("n="))
    result = fakultet(value)
    print("n! =", result)

main()

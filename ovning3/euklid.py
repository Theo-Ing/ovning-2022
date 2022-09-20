def euk(a, b):
    if b > a:
        a, b = b, a

    while b != 0:
        c = a % b
        a = b
        b = c

    return a

def main():
    a = int(input("a = "))
    b = int(input("b = "))
    result = euk(a, b)
    print("Största gemensamma nämnare:", result)

main()

# Be om a, b och c
a = float(input("Första sidlängd: "))
b = float(input("Andra sidlängd: "))
c = float(input("Tredje sidlängd: "))

# Kolla om giltig triangel
# a + b > c
# b + c > a
# c + a > b
if (a + b > c) and (b + c > a) and (c + a > b):
    # Om giltig triangel beräkna area
    s = (a + b + c) / 2
    A = (s*(s-a)*(s-b)*(s-c))**(1/2)
    print("Triangel area:", A)
else:
    print("Inte giltig triangel, gör bättre.")

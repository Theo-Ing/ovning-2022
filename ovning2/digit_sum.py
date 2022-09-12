n = int(input("Ge talet: ")) # Tal vars siffersumma ska beräknas

if 0 < n < 1000:
    ental = n % 10
    tot_tiotal = n // 10
    tiotal = tot_tiotal % 10
    hundratal = tot_tiotal // 10
    print("Siffersumma:", ental + tiotal + hundratal)
else:
    # Mer än tresiffrigt
    temp = n
    sum = 0
    while temp > 0:
        sum += temp % 10
        temp = temp // 10
    print("Siffersumma:", sum)

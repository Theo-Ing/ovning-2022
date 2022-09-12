limit = float(input("Gräns som ska överskridas: "))

sum = 0
counter = 0
while sum < limit:
    counter += 1
    sum += 1/counter
print("Antal termer:", counter)

terms = int(input("Antal termer: "))

sum = 0
for i in range(1, terms + 1):
    sum += 1/i
print("Harmonic sum:", sum)

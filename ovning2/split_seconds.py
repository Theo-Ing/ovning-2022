tot_seconds = int(input("Totala sekunder: "))

# Totala minuter
tot_minutes = tot_seconds // 60
rest_seconds = tot_seconds % 60 # kvarvarande sekunder

# Totala timmar
tot_hours = tot_minutes // 60
rest_minutes = tot_minutes % 60

# Totala dagar
tot_days = tot_hours // 24
rest_hours = tot_hours % 24

print("Dagar:", tot_days)
print("Timmar:", rest_hours)
print("Minuter:", rest_minutes)
print("Sekunder:", rest_seconds)

a = int(input("Erste Zahl: "))
b = int(input("Zweite Zahl: "))
c = int(input("Dritte Zahl: "))

if a < b < c or c < b < a:
    print("Die zweite Zahl liegt dazwischen.")
else:
    print("Die zweite Zahl liegt nicht dazwischen.")
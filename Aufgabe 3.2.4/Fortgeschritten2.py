jahr = int(input("Gib ein Jahr ein: "))

if (jahr % 4 == 0 and jahr % 100 != 0) or (jahr % 400 == 0):
    print("Schaltjahr")
else:
    print("Kein Schaltjahr")
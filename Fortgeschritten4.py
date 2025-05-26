betrag = float(input("Einkaufswert (€): "))

if betrag > 100:
    betrag *= 0.9
    print("10 % Rabatt angewendet.")

print("Endpreis:", round(betrag, 2), "€")

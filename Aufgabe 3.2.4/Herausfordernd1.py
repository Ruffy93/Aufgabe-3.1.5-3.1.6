farbe = input("Farbe der Ampel (rot, gelb, grün): ").lower()

if farbe == "rot":
    print("Stehen.")
elif farbe == "gelb":
    print("Bereit machen.")
elif farbe == "grün":
    print("Gehen.")
else:
    print("Ungültige Farbe.")
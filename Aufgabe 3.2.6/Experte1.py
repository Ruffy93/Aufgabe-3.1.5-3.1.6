import random

zahl = random.randint(1, 100)
versuche = 5

print("finde die richtige Zahl zwischen 0 und 100")
print(f"Du hast {versuche} Versuche, enttäusch mich nicht!")

while True:
    tipp = int(input("Deine Zahl:"))
    versuche -= 1

    if tipp == zahl:
        print(f"DU HAST DIE RICHTIGE ZAHL, LUCKY BOYYYYY! Versuche: {versuche}")
        break
    elif tipp < zahl:
        print("Deine Zahl ist zu niedrig")
    else:
        print("Deine Zahl ist zu Hoch")

    if versuche == 0:
        print(f"Verloren!!!!!")
    else:
        print(f"Noch {versuche} Versuche übrig")   
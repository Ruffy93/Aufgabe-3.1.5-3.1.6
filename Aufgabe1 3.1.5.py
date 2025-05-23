Hersteller = "Scania"
Farbe = "Blau"
Größe = "Groß"
Anzahl_Türen = "3 Türen"
Kraftstoff = "Diesel"
Fahrzeugart = "LKW"
Baujahr = "2015"
Anzahl_Sitze = "2"
Zuladung = "44"
Getriebe = "Automatik"
Motor_Hubraum = "16,4"
Motor_Typ = "V8"
Leistung = "770"

print ("Vor dem Variablentausch:")
print (f"Farbe {Farbe}")
print (f"Größe {Größe}")
print (f"Türen {Anzahl_Türen}")
print (f"Kraftstoff {Kraftstoff}")
print (f"Typ {Fahrzeugart}")
print (f"Baujahr {Baujahr}")
print (f"Hersteller {Hersteller}")
print (f"Sitze {Anzahl_Sitze}")
print (f"Zuladung {Zuladung} Tonnen")
print (f"Getriebe {Getriebe}")
print (f"Hubraum {Motor_Hubraum} Liter")
print (f"Motorbauform {Motor_Typ}")
print (f"Leistung {Leistung} PS")

Motor_Typ, Motor_Hubraum = Motor_Hubraum, Motor_Typ


print("\nGetauschte Variable")
print(f"Hubraum {Motor_Hubraum}")
print(f"Motorbauform {Motor_Typ}")
gewicht = float(input("Gewicht in kg: "))
groesse = float(input("Größe in m: "))

bmi = gewicht / (groesse ** 2)
print("BMI:", round(bmi, 2))

if bmi <= 18.5:
    print("Untergewicht")
elif bmi <= 24.9:
    print("Normalgewicht")
else:
    print("Übergewicht")
def limpiar():
    print("")
opcion = int(input("1) Kilogramos a Libras.\n2) Kilogramos a Onzas.\n3) Kilogramos a Slugs\nSelecciona la opción a realizar: "))
if opcion == 1:
    kg = float(input("Ingrese los Kilogramos para ser convertidos a Libras: "))
    lb = kg * 2.20462
    print(f"{kg} kilogramos es igual a {lb} libras.")
    limpiar()
elif opcion == 2:
    kg = float(input("Ingrese los Kilogramos para ser convertidos a Onzas: "))
    oz = kg * 28.70
    print(f"{kg} kilogramos son {oz} onzas.")
    limpiar()
elif opcion == 3:
    kg = float(input("Ingrese los Kilogramos para ser convertidos a Slugs: "))
    s = kg*0.06852
    print(f"{kg} Kg es igual a {s} slug")
    limpiar()
import math

# Función de área de un cuadrado
def calcular_area_cuadrado(lado):
    area = lado * lado
    return area

# Función para calcular el área de un círculo
def calcular_area_circulo(radio):
    area = math.pi * radio ** 2
    return area

# Función para calcular el área de un triángulo
def calcular_area_triangulo(base, altura):
    area = base * altura / 2
    return area

# Función para calcular el área de un rombo
def calcular_area_rombo(DM, Dm):
    area = DM * Dm / 2
    return area

# Función para calcular el área de un trapecio
def calcular_area_trapecio(BASE, base, altura):
    area = BASE + base * altura / 2
    return area

# Función para calcular el área de un pentágono
def calcular_area_pentagono(peri, apo):
    area = peri * apo / 2
    return area 

def limpiar_resultado():
    print("\nResultados limpiados. Puedes seleccionar otra opción")
    
    # Loop principal
    while True:
        # Seleccionar figura
        print("Selecciona la figura para calcular su área:")
        print(" 1. cuadrado")
        print(" 2. circulo")
        print(" 3. triangulo")
        print(" 4. rombo")
        print(" 5. trapecio")
        print(" 6. pentagono")
        print(" 7. limpiar resultados y seleccionar otra opcion")
        print(" 8. salir")

        try:
            opcion = int(input("Ingresa el numero de la figura o una opcion adicional: "))
        except ValueError:
            print("Error: ingresa un numero valido. ")
            continue

        # Switch para calcular y mostrar el área según la figura seleccionada
        if opcion == 1:
            lado = float(input("Ingresa la longitud del lado del cuadrado: "))
            area = calcular_area_cuadrado(lado)
            print(f"El area del cuadrado con lado {lado} es: {area}")
        elif opcion == 2:
            radio = float(input("Ingresa el radio del circulo: "))
            area = calcular_area_circulo(radio)
            print(f"El area del circulo con radio {radio} es: {area}")
        elif opcion == 3:
            base = float(input("Ingresa la base del triangulo: "))
            altura = float(input("Ingresa la altura del triangulo: "))
            area = calcular_area_triangulo(base, altura)
            print(f"El area del triangulo con base {base} y altura {altura} es: {area}")
        elif opcion == 4:
            DM = float(input("Ingresa la diagonal mayor: "))
            Dm = float(input("Ingresa la diagonal menor: "))
            area = calcular_area_rombo(DM, Dm)
            print(f"El area del rombo con diagonal mayor {DM} y diagonal menor {Dm} es: {area}")
        elif opcion == 5:
            BASE = float(input("Ingresa la primer base del trapecio: "))
            base = float(input("Ingresa la sgunda base del trapecio: "))
            altura = float(input("Ingresa la altura del trapecio: "))
            area = calcular_area_trapecio(BASE, base, altura)
            print(f"El area del trapecio con base 1 {BASE} base 2 {base} y altura {altura} es: {area}")
        elif opcion == 6:
            peri = float(input("Ingresa el perimetro del pentagono: "))
            apo = float(input("Ingresa la apotema del pentagono: "))
            area = calcular_area_pentagono(peri, apo)
            print(f"El area del pentagono con perimetro {peri} y apotema {apo} es: {area}")
        elif opcion == 7:
            print("¡Sale BYE!")
            break
        else:
            print("Ingrese numeros del 1 al 7")
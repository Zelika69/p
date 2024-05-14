import math

def calcular_area_cuadrado(lado):
    area = lado * lado
    return area

def calcular_area_circulo(radio):
    area = math.pi * radio**2
    return area

def calcular_area_triangulo(base, altura):
    area = 0.5 * base * altura
    return area

def calcular_area_rombo(diagonal_mayor, diagonal_menor):
    area = (diagonal_mayor * diagonal_menor) / 2
    return area

def calcular_area_pentagono(lado, apotema):
    area = (5 * lado * apotema) / 2
    return area

def calcular_area_trapecio(base_mayor, base_menor, altura):
    area = ((base_mayor + base_menor) / 2) * altura
    return area

def calcular_area_romboide(base, altura):
    area = base * altura
    return area

def limpiar_consola():
    print("\nResultados limpiados. Puedes seleccionar otra opción")

while True:
    # selecciona la figura
    print("Selecciona la figura para calcular área.")
    print("1) Cuadrado.")
    print("2) Círculo")
    print("3) Triángulo")
    print("4) Rombo")
    print("5) Pentágono")
    print("6) Trapecio")
    print("7) Romboide")
    print("8) Salir")
    try:
        opcion = int(input("Ingrese una opción del menú: "))
    except ValueError:
        print("Error: Ingresar un número valido.")
        continue
        #Área del cuadrado
    if opcion == 1:
        lado = float(input("Digite el tamaño de uno de los lados del cuadrado: "))
        area = calcular_area_cuadrado(lado)
        print(f"El área del cuadrado con lado {lado} es: {area} u²")
        limpiar_consola()
        #Area del circulo
    elif opcion == 2:
        radio = float(input("Ingresa el radio del círculo: "))
        area = calcular_area_circulo(radio)
        print(f"El área del círculo con radio {radio} es: {area} u²")
        limpiar_consola()
        #Área del triangulo
    elif opcion == 3:
        base = float(input("Ingresa la base del triángulo: "))
        altura = float(input("Ingresa la altura del triángulo: "))
        area = calcular_area_triangulo(base, altura)
        print(f"El área del triángulo con base {base} y altura {altura} es: {area} u²")
        limpiar_consola()
        #Área del rombo
    elif opcion == 4:
        diagonal_mayor = float(input("Ingresa la diagonal mayor del rombo: "))
        diagonal_menor = float(input("Ingresa la diagonal menor del rombo: "))
        area = calcular_area_rombo(diagonal_mayor, diagonal_menor)
        print(f"El área del rombo con diagonal mayor: {diagonal_mayor} y diagonal menor: {diagonal_menor} es: {area} u²")
        limpiar_consola()
        #Área del pentágono
    elif opcion == 5:
        lado = float(input("Ingresa el lado del pentágono: "))
        apotema = float(input("Ingresa la apotema del pentágono: "))
        area = calcular_area_pentagono(lado, apotema)
        print(f"El área del pentágono con lado: {lado} y apotema: {apotema} es: {area} u²")
        limpiar_consola()
        #Área del trapecio
    elif opcion == 6:
        base_mayor = float(input("Ingresa la base mayor del trapecio: "))
        base_menor = float(input("Ingresa la base menor del trapecio: "))
        altura = float(input("Ingresa la altura del trapecio: "))
        area = calcular_area_trapecio(base_mayor, base_menor, altura)
        print(f"El área del trapecio con base mayor: {base_mayor}, base menor: {base_menor} y altura: {altura} es: {area} u²")
        limpiar_consola()
        #Área del romboide
    elif opcion == 7:
        base = float(input("Ingresa la base del romboide: "))
        altura = float(input("Ingresa la altura del romboide: "))
        area = calcular_area_romboide(base, altura)
        print(f"El área del romboide con base {base} y altura {altura} es: {area} u²")
        limpiar_consola()
    elif opcion == 8:
        print("Sale vato!")
        break
    else:
        print("Opción no válida. Por favor, elige un número entre 1 y 8.")

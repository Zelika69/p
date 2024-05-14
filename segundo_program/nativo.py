def clasificar_triangulo(a, b, c):
    if a + b > c and b + c > a and a + c > b:
        if a == b == c:
            return "Triángulo equilátero"
        elif a == b or b == c or a == c:
            return "Triángulo isósceles"
        else:
            return "Triángulo escaleno"
    else:
        return "No es un triángulo"

def clasificar_angulos(a1, a2, a3):
    if (a1 == 90 and (a2 + a3 == 120)) or (a2 == 90 and (a1 + a3 == 120)) or (a3 == 90 and (a1 + a2 == 120)):
        return "Triángulo Rectángulo"
    elif a1 > 90 or a2 > 90 or a3 > 90:
        return "Triángulo Obtusángulo"
    elif a1 < 90 and a2 < 90 and a3 < 90 and (a1 + a2 + a3 == 180):
        return "Triángulo Acutángulo"
    elif a1 + a2 > a3:
        return "No es un triángulo"
    else:
        return "no es un triangulo"

while True:
    pregunta = input("1) Clasificar por lados\n2) Clasificar por ángulos\n  1 / 2: ")
    if pregunta == "1":
        a = float(input("Ingrese el lado a: "))
        b = float(input("Ingrese el lado b: "))
        c = float(input("Ingrese el lado c: "))
        print(clasificar_triangulo(a, b, c))
    elif pregunta == "2":
        a1 = float(input("Ingrese el primer ángulo en grados: "))
        a2 = float(input("Ingrese el segundo ángulo en grados: "))
        a3 = float(input("Ingrese el tercer ángulo en grados: "))
        print(clasificar_angulos(a1, a2, a3))
    else:
        print("Adiós!")
        break

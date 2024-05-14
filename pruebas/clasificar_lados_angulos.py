def validar_triangulo(angulo1, angulo2, angulo3):
    # Verificar si la suma de los ángulos es 180 (condición para ser un triángulo)
    if angulo1 + angulo2 + angulo3 == 180:
        return True
    else:
        return False

def clasificar_triangulo(angulo1, angulo2, angulo3):
    # Validar si los ángulos forman un triángulo
    if not validar_triangulo(angulo1, angulo2, angulo3):
        return "No es un triángulo válido."

    # Clasificar según los ángulos
    if angulo1 < 90 and angulo2 < 90 and angulo3 < 90:
        return "Triángulo Acutángulo"
    elif angulo1 > 90 or angulo2 > 90 or angulo3 > 90:
        return "Triángulo Obtusángulo"
    else:
        return "Triángulo Rectángulo"

# Ingresar los ángulos desde el usuario
angulo1 = float(input("Ingrese el primer ángulo: "))
angulo2 = float(input("Ingrese el segundo ángulo: "))
angulo3 = float(input("Ingrese el tercer ángulo: "))

# Obtener la clasificación e imprimir el resultado
resultado = clasificar_triangulo(angulo1, angulo2, angulo3)
print("El triángulo es:", resultado)

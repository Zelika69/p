import math
def validar_angulos(angulo_alpha, angulo_beta):
    if angulo_alpha or angulo_beta > 90:
        return "Lo siento pero el triángulo no puede existir"
    
def calcular_triangulo_rectangulo(opcion):
    
    if opcion == 1:
        cateto_opuesto = float(input("Ingrese la medida del cateto opuesto: "))
        cateto_adyacente = cateto_opuesto
        hipotenusa = math.sqrt((cateto_adyacente**2)+(cateto_opuesto**2))
        angulo_alpha = math.degrees(math.asin(cateto_opuesto/hipotenusa))
        angulo_beta = 90-angulo_alpha
    
    elif opcion == 2:
        hipotenusa = float(input("Ingrese la medida de la Hipotenusa: "))
        cateto_adyacente = hipotenusa/(math.sqrt(2))
        cateto_opuesto = cateto_adyacente
        angulo_alpha = math.degrees(math.asin(cateto_opuesto/hipotenusa))
        angulo_beta = 90-angulo_alpha
        
    elif opcion == 3:  # Cateto Opuesto y ángulo beta β
        cateto_opuesto = float(input("Ingresa el valor del Cateto opuesto: "))
        angulo_beta = float(input("Ingrese el valor del ángulo beta (en grados): "))
        angulo_alpha = 90 -(angulo_beta)
        cateto_adyacente = cateto_opuesto / math.tan(math.radians(angulo_alpha))
        hipotenusa = cateto_opuesto / math.sin(math.radians(angulo_alpha))

    elif opcion == 4:  # Cateto adyacente y ángulo beta β
        cateto_adyacente = float(input("Ingresa el valor del Cateto adyacente: "))
        angulo_beta = float(input("Ingrese el valor del ángulo beta (en grados): "))
        angulo_alpha = 90 -(angulo_beta)
        cateto_opuesto = cateto_adyacente * math.tan(math.radians(angulo_alpha))
        hipotenusa = math.sqrt((cateto_opuesto**2)+(cateto_adyacente**2))

    elif opcion == 5:  # Hipotenusa y ángulo beta β
        hipotenusa = float(input("Ingresa el valor de la hipotenusa: "))
        angulo_beta = float(input("Ingrese el valor del ángulo beta (en grados): "))
        angulo_alpha = 90-angulo_beta
        cateto_opuesto = hipotenusa * math.sin(math.radians(angulo_alpha))
        cateto_adyacente = math.sqrt((hipotenusa**2)-(cateto_opuesto**2))
    
    elif opcion == 6:
        cateto_opuesto = float(input("Ingrese el la medida del cateto opuesto: "))
        angulo_alpha = float(input("Ingrese el valor del ángulo alpha (en grados): "))
        angulo_beta = 90 - angulo_alpha
        cateto_adyacente = angulo_beta * math.cos(math.radians(angulo_alpha))
        hipotenusa = math.sqrt((cateto_adyacente**2)+(cateto_opuesto**2))
        
    elif opcion == 7:
        cateto_adyacente = float(input("Ingrese el valor del cateto  adyacente: "))
        angulo_alpha = float(input("Ingrese el valor del ángulo alpha (en grados): "))
        angulo_beta = 90 - angulo_alpha
        cateto_opuesto = cateto_adyacente *  math.tan(math.radians(angulo_alpha))
        hipotenusa = math.sqrt((cateto_adyacente**2)+(cateto_opuesto**2))
        
    elif opcion == 8:
        hipotenusa = float(input("Ingrese el valor de la Hipotenusa: "))
        angulo_alpha = float(input("Ingrese el valor del ángulo alpha  (en grados): "))
        angulo_beta = 90-angulo_alpha
        cateto_opuesto = hipotenusa * math.sin(math.radians(angulo_alpha))
        cateto_adyacente = math.sqrt((hipotenusa**2)-(cateto_opuesto**2))
        
    elif opcion == 9:
        cateto_opuesto = float(input("Ingrese el valor del cateto opuesto: "))
        cateto_adyacente = float(input("Ingrese el valor del cateto adyacente: "))
        hipotenusa = math.sqrt((cateto_adyacente**2)+(cateto_opuesto**2))
        angulo_alpha = math.degrees(math.asin(cateto_opuesto/hipotenusa))
        angulo_beta = 90-angulo_alpha
        
    elif opcion == 10:
        cateto_adyacente = float(input("Ingrese el valor del cateto adyacente: "))
        hipotenusa  = float(input("Ingrese el valor de la hipotenusa: "))
        cateto_opuesto = math.sqrt((hipotenusa**2)-(cateto_adyacente**2))
        angulo_alpha = math.degrees(math.asin(cateto_opuesto/hipotenusa))
        angulo_beta = 90 - angulo_alpha
        
    elif opcion == 11:
        cateto_opuesto = float(input("Ingrese el valor del cateto opuesto: "))
        hipotenusa  = float(input("Ingrese el valor de la hipotenusa: "))
        cateto_adyacente = math.sqrt((hipotenusa**2)-(cateto_opuesto**2))
        angulo_alpha = math.degrees(math.asin(cateto_opuesto/hipotenusa))
        angulo_beta = 90-angulo_alpha
        
    elif opcion == 12:
        cateto_opuesto = float(input("Ingrese el valor del cateto opuesto: "))
        cateto_adyacente = float(input("Ingrese el valor del cateto adyacente: "))
        hipotenusa  = float(input("Ingrese el valor de la hipotenusa: "))
        angulo_alpha = math.degrees(math.asin(cateto_opuesto/hipotenusa))
        angulo_beta = 90-angulo_alpha
        
    elif opcion == 13:
        cateto_opuesto = float(input("Ingrese el valor del cateto opuesto: "))
        cateto_adyacente = float(input("Ingrese el valor del cateto adyacente: "))
        hipotenusa  = float(input("Ingrese el valor de la hipotenusa: "))
        angulo_alpha = float(input("Ingrese el valor del ángulo alpha (en grados): "))
        angulo_beta = 90 - angulo_alpha
        
    elif opcion == 14:
        cateto_opuesto = float(input("Ingrese el valor del cateto opuesto: "))
        cateto_adyacente = float(input("Ingrese el valor del cateto adyacente: "))
        hipotenusa  = float(input("Ingrese el valor de la hipotenusa: "))
        angulo_beta = float(input("Ingrese el valor del ángulo beta (en grados): "))
        angulo_alpha = 90-angulo_beta
        
    elif opcion == 15:
        cateto_opuesto = float(input("Ingrese el valor del cateto opuesto: "))
        cateto_adyacente = float(input("Ingrese el valor del cateto adyacente: "))
        angulo_alpha = float(input("Ingrese el valor del ángulo alpha (en grados): "))
        hipotenusa = math.sqrt((cateto_adyacente**2)+(cateto_opuesto**2))
        angulo_beta = 90-angulo_alpha
        
    elif opcion == 16:
        cateto_opuesto = float(input("Ingrese el valor del cateto opuesto: "))
        cateto_adyacente = float(input("Ingrese el valor del cateto adyacente: "))
        angulo_beta = float(input("Ingrese el valor del ángulo beta (en grados): "))
        hipotenusa = math.sqrt((cateto_adyacente**2)+(cateto_opuesto**2))
        angulo_alpha = 90-angulo_beta
        
    elif opcion == 17:
        cateto_opuesto = float(input("Ingrese el valor del cateto opuesto: "))
        hipotenusa  = float(input("Ingrese el valor de la hipotenusa: "))
        angulo_alpha = float(input("Ingrese el valor del ángulo alpha (en grados): "))
        cateto_adyacente = math.sqrt((hipotenusa**2)-(cateto_opuesto**2))
        angulo_beta = 90-angulo_alpha
        
    elif opcion == 18:
        cateto_adyacente = float(input("Ingrese el valor del cateto adyacente: "))
        hipotenusa  = float(input("Ingrese el valor de la hipotenusa: "))
        cateto_opuesto = math.sqrt((hipotenusa**2)-(cateto_adyacente**2))
        angulo_beta = float(input("Ingrese el valor del ángulo beta (en grados): "))
        angulo_alpha = 90-angulo_beta
        
    else:
        print("Opción no válida.")
        return None

    return cateto_opuesto, cateto_adyacente, hipotenusa, angulo_alpha, angulo_beta

while True:
    print("Menú:")
    print("1) Un cateto.")
    print("2) Hipotenusa.")
    print("3) Cateto Opuesto y ángulo beta β.")
    print("4) Cateto adyacente y ángulo beta β.")
    print("5) Hipotenusa y ángulo beta β.")
    print("6) Cateto opuesto y ángulo alpha α.")
    print("7) Cateto adyacente y ángulo alpha α.")
    print("8) Hipotenusa y ángulo alpha α.")
    print("9) Cateto opuesto y Cateto adyacente.")
    print("10) Cateto adyacente e Hipotenusa.")
    print("11) Cateto opuesto e Hipotenusa. ")
    print("12) Cateto opuesto, cateto adyacente e Hipotenusa.")
    print("13) Cateto opuesto, cateto adyacente, Hipotenusa y angulo alpha.")
    print("14) Cateto opuesto, cateto adyacente, Hipotenusa y angulo beta.")
    print("15) Cateto opuesto, cateto adyacente y angulo alpha. ")
    print("16) Cateto opuesto, cateto adyacente y angulo beta. ")
    print("17) Cateto opuesto, hipotenusa y angulo alpha.")
    print("18) Cateto adyacente, hipotenusa y angulo beta. ")
    
    opcion = int(input("Ingrese el número de la opción deseada: "))
    unidades = input("Unidades del triángulo: ")

    resultados = calcular_triangulo_rectangulo(opcion)

    if resultados:
        print("\nResultados:")
        print(f"Cateto Opuesto: {resultados[0]:.4f} {unidades}")
        print(f"Cateto Adyacente: {resultados[1]:.4f} {unidades}")
        print(f"Hipotenusa: {resultados[2]:.4f} {unidades}")
        print(f"Ángulo Alpha: {resultados[3]:.4f}°")
        print(f"Ángulo Beta: {resultados[4]:.4f}°")
        print(f"Ángulo Theta: 90.0000°\n")
    input("Enter para contunuar....")

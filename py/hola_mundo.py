import math

# Función del área de un cuadrado 
def calcular_area_Cuadrado(lado):
    area=lado*lado 
    return area

#  Función para calcular el área de un circulo
def calcular_area_Circulo(radio):
    area = math.pi * radio ** 2
    return area 

# Función para calcular el área de un triangulo 
def calcular_area_Triangulo(base, altura): 
  area = 0.5 * base * altura 
  return area 

# Función para calcular el área de un rombo 
def calcular_area_trapecio(base_mayor, base_menor, altura):
    area = 0.5 * (base_mayor + base_menor) * altura
    return area
#Función para calcular el área de un Pentagono 
def calcular_area_pentagono(lado):
    area = 0.25 * math.sqrt(5 * (5 + 2 * math.sqrt(5))) * lado**2
    return area

# Función para calcular el área de un Trapecio
def calcular_area_trapecio(base_mayor, base_menor, altura):
    area = 0.5 * (base_mayor + base_menor) * altura
    return area

# Función para calcular el área de un Romboide
def calcular_area_romboide(base, altura):
    area = base * altura
    return area

# Función para limpiar los resultados 
def limpiar_resultados():
    print("\nResultados limpiados. puedes seleccionar otra opción.")
    
while True:
        #selecciona la figura
        print(" Selecciona la figura para calcular área.")
        print("1) Cuadrado.")
        print("2) Circulo")
        print("3) Triangulo")
        print("4) Rombo")
        print("5) Pentagono")
        print("6) Trapecio")
        print("7) Romboide")
        print("8) Rectangulo")
        print("9) Salir ")
        try:
            opcion=int(input("Ingrese una opción del menú: "))
        except ValueError:
            print("Error: Ingresar un número valido.")
            continue
        
        # Switch para calcular y mostrar el área según la figura seleccionada 
        if opcion == 1:
            lado=float(input("Digite el tamaño de uno de los lados del cuadrado: "))
            area = calcular_area_cuadrado(lado)
            print(f"El área del cuadrado con lado {lado} es: {area}")
        elif opcion == 2:
            radio = float(input("Ingresa el radio del circulo: "))
            area = calcular_area_circulo(radio)
            print(f"El area del circulo con radio es: {area}")
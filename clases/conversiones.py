
def limpiar():
    print("")
    
while True:
    print(''
          'efesfes',
          'husdbcshyudy'
          '')
    opcion = int(input("Selecciona la opción a realizar: "))
    if opcion == 1 :
        c_grados = float(input("Ingresa la cantidad de grados celcius: "))
        f_grados = (c_grados * 9/5) + 32
        print(f"{c_grados}° Grados Celsius es igual a {f_grados}° Fahreheit.")
        limpiar()
        
    elif opcion == 2:
        f_grados = float(input("Ingresa la cantidad de grados Fahrenheit: "))
        c_grados = (f_grados - 32) * 5/9
        print(f"{f_grados}° Grados Fahrenheit es igual a {c_grados}° Celsius.")
        limpiar()
        
    elif opcion == 3:
        c_grados = float(input("Ingresa la cantidad de grados Celsius: "))
        k_grados = c_grados + 273.15
        print(f"{c_grados}° Grados Celsius es igual a {k_grados}° Kelvin.")
        limpiar()
        
    elif opcion == 4:
        k_grados = float(input("Ingresa la cantidad de grados Kelvin: "))
        c_grados = k_grados - 273.15
        print(f"{k_grados}° Grados Kelvin es igual a {c_grados}° Celsius.")
        limpiar()
        
    elif opcion == 5:
        f_grados = float(input("Ingresa la cantidad de grados Fahrenheit: "))
        k_grados = (f_grados - 32) * 5/9 + 273.15
        print(f"{f_grados}° Grados Fahrenheit es igual a {k_grados}° Kelvin.")
        limpiar()
        
    elif opcion == 6:
        k_grados = float(input("Ingresa la cantidad de grados Kelvin: "))
        f_grados = (k_grados - 273.15) * 9/5 + 32
        print(f"{k_grados}° Grados Kelvin es igual a {f_grados}° Fahrenheit.")
        limpiar()
        
    elif opcion ==7:
        print("sale hommie!")
        break
    
    #conversioes de
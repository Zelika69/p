import tkinter as tk

def clasificar_triangulo(a, b, c):
    if a == b == c:
        return "Triángulo equilátero"
    elif a == b or b == c or a == c:
        return "Triángulo isósceles"
    elif a + b > c and b + c > a and a + c > b:
        return "Triángulo escaleno"
    else:
        return "No es un triángulo"

            
a = float(input("Ingrese un número: "))
b = float(input("Ingrese un número: "))
c = float(input("Ingrese un número: "))

print(clasificar_triangulo(a, b, c))


def realizar_clasificacion():
    # Obtiene los valores de los cuadros de texto.
    a = float(entry_a.get())
    b = float(entry_b.get())
    c = float(entry_c.get())

    # Clasifica el triángulo utilizando la función clasificar_triangulo.
    clasificacion = clasificar_triangulo(a, b, c)

    # Muestra la clasificación del triángulo en una etiqueta.
    label_clasificacion.config(text=clasificacion)

# Define la función clasificar_triangulo.
def clasificar_triangulo(a, b, c):
    # Comprueba si todos los lados son iguales, lo cual indica un triángulo equilátero.
    if a == b == c:
        return "Triángulo equilátero"
    # Comprueba si al menos dos lados son iguales, lo cual indica un triángulo isósceles.
    elif a == b or b == c or a == c:
        return "Triángulo isósceles"
    # Comprueba si los lados cumplen con la desigualdad triangular, lo cual indica un triángulo escaleno.
    elif a + b > c and b + c > a and a + c > b:
        return "Triángulo escaleno"
    # Si no se cumple ninguna de las condiciones anteriores, el triángulo no es válido.
    else:
        return "No es un triángulo"

# Crea la ventana principal de Tkinter.
ventana = tk.Tk()

# Crea un encabezado.
label_encabezado = tk.Label(ventana, text="Clasificador de triángulos")
label_encabezado.grid(row=0, column=0, columnspan=3)

# Crea cuadros de texto para ingresar los lados del triángulo.
entry_a = tk.Entry(ventana)
entry_a.grid(row=1, column=0)
entry_b = tk.Entry(ventana)
entry_b.grid(row=1, column=1)
entry_c = tk.Entry(ventana)
entry_c.grid(row=1, column=2)

# Crea un botón para clasificar el triángulo.
boton_clasificar = tk.Button(ventana, text="Clasificar", command=realizar_clasificacion)
boton_clasificar.grid(row=2, column=0, columnspan=3)

# Crea una etiqueta para mostrar la clasificación del triángulo.
label_clasificacion = tk.Label(ventana, text="")
label_clasificacion.grid(row=3, column=0, columnspan=3)

# Inicia el bucle principal de Tkinter.
ventana.mainloop()
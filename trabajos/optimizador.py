import tkinter as tk

def clasificar_triangulo(a, b, c):
    lados = [a, b, c]
    lados_ordenados = sorted(lados)
    
    if lados_ordenados[0] + lados_ordenados[1] <= lados_ordenados[2]:
        return "No es un triángulo"
    elif a == b == c:
        return "Triángulo equilátero"
    elif a == b or b == c or a == c:
        return "Triángulo isósceles"
    else:
        return "Triángulo escaleno"

def realizar_clasificacion():
    try:
        a, b, c = map(float, (entry_a.get(), entry_b.get(), entry_c.get()))
        clasificacion = clasificar_triangulo(a, b, c)
        label_clasificacion.config(text=clasificacion)
    except ValueError:
        label_clasificacion.config(text="Ingrese valores numéricos válidos")

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
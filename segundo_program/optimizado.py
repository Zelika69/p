import tkinter as tk
from tkinter import ttk

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
    if a1 == 90 or a2 == 90 or a3 == 90:
        return "Triángulo Rectángulo"
    elif a1 > 90 or a2 > 90 or a3 > 90:
        return "Triángulo Obtusángulo"
    elif a1 < 90 and a2 < 90 and a3 < 90:
        return "Triángulo Acutángulo"
    elif a1 + a2 + a3 < 0 or a1 + a2 + a3 < 180:
        return "Error"
    elif a1 

def clasificar():
    tipo_seleccionado = tipo_combobox.get()
    
    if tipo_seleccionado == "Lados":
        a = int(lado_a_entry.get())
        b = int(lado_b_entry.get())
        c = int(lado_c_entry.get())
        resultado_label.config(text=clasificar_triangulo(a, b, c))
    elif tipo_seleccionado == "Ángulos":
        a1 = int(angulo_a_entry.get())
        a2 = int(angulo_b_entry.get())
        a3 = int(angulo_c_entry.get())
        resultado_label.config(text=clasificar_angulos(a1, a2, a3))

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Clasificador de Triángulos")

# Crear variables de control para los Entry widgets
lado_a = tk.StringVar()
lado_b = tk.StringVar()
lado_c = tk.StringVar()
angulo_a = tk.StringVar()
angulo_b = tk.StringVar()
angulo_c = tk.StringVar()

# Crear y configurar widgets
tipo_combobox = ttk.Combobox(ventana, values=["Lados", "Ángulos"])
tipo_combobox.set("Lados")
tipo_combobox.grid(row=0, column=0, padx=10, pady=10)

# Widgets para la entrada de lados
lado_a_label = tk.Label(ventana, text="Lado a:")
lado_a_label.grid(row=1, column=0)
lado_a_entry = tk.Entry(ventana, textvariable=lado_a)
lado_a_entry.grid(row=1, column=1)

lado_b_label = tk.Label(ventana, text="Lado b:")
lado_b_label.grid(row=2, column=0)
lado_b_entry = tk.Entry(ventana, textvariable=lado_b)
lado_b_entry.grid(row=2, column=1)

lado_c_label = tk.Label(ventana, text="Lado c:")
lado_c_label.grid(row=3, column=0)
lado_c_entry = tk.Entry(ventana, textvariable=lado_c)
lado_c_entry.grid(row=3, column=1)

# Widgets para la entrada de ángulos
angulo_a_label = tk.Label(ventana, text="Ángulo a:")
angulo_a_label.grid(row=1, column=2)
angulo_a_entry = tk.Entry(ventana, textvariable=angulo_a)
angulo_a_entry.grid(row=1, column=3)

angulo_b_label = tk.Label(ventana, text="Ángulo b:")
angulo_b_label.grid(row=2, column=2)
angulo_b_entry = tk.Entry(ventana, textvariable=angulo_b)
angulo_b_entry.grid(row=2, column=3)

angulo_c_label = tk.Label(ventana, text="Ángulo c:")
angulo_c_label.grid(row=3, column=2)
angulo_c_entry = tk.Entry(ventana, textvariable=angulo_c)
angulo_c_entry.grid(row=3, column=3)

# Botón de clasificación
clasificar_button = tk.Button(ventana, text="Clasificar", command=clasificar)
clasificar_button.grid(row=4, column=0, columnspan=4, pady=10)

# Resultado
resultado_label = tk.Label(ventana, text="")
resultado_label.grid(row=5, column=0, columnspan=4, pady=10)

# Iniciar el bucle principal
ventana.mainloop()

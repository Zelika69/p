import tkinter as tk
from tkinter import messagebox
import math
# Configurar fuente y tamaño
font_style = ("Arial", 30)
def mostrar_ventana(opcion):
    ventana_input = tk.Toplevel(ventana_principal)
    ventana_input.title(f"Ingrese datos para {opcion}")


    if opcion == "Cateto Opuesto":
        tk.Label(ventana_input, text="Ingrese la medida del cateto opuesto: ", font=font_style).pack()
        cateto_opuesto_entry = tk.Entry(ventana_input, font=font_style)
        cateto_opuesto_entry.pack()

        tk.Button(ventana_input, text="Calcular", font=font_style, command=lambda: calcular(opcion, cateto_opuesto_entry.get())).pack()

    elif opcion == "Hipotenusa":
        tk.Label(ventana_input, text="Ingrese la medida de la hipotenusa: ", font=font_style).pack()
        hipotenusa_entry = tk.Entry(ventana_input, font=font_style)
        hipotenusa_entry.pack()

        tk.Button(ventana_input, text="Calcular", font=font_style, command=lambda: calcular(opcion, hipotenusa_entry.get())).pack()

    # Agrega más bloques similares para otras opciones...

def calcular(opcion, valor):
    try:
        valor = float(valor)
        ventana_resultados = tk.Toplevel(ventana_principal)
        ventana_resultados.title("Resultados")

        if opcion == "Cateto Opuesto":
            cateto_adyacente = valor
            hipotenusa = math.sqrt((cateto_adyacente**2) + (valor**2))
            angulo_alpha = math.degrees(math.asin(valor / hipotenusa))
            angulo_beta = 90 - angulo_alpha

            lbl_resultado = tk.Label(ventana_resultados, text=f"Cateto Adyacente: {cateto_adyacente:.4f}\nHipotenusa: {hipotenusa:.4f}\nÁngulo Alpha: {angulo_alpha:.4f}°\nÁngulo Beta: {angulo_beta:.4f}°\nÁngulo theta: 90", font=font_style)
            lbl_resultado.pack()

        # Agrega más bloques similares para otras opciones...

    except ValueError:
        messagebox.showerror("Error", f"Ingresa un valor numérico válido para {opcion}.")

# Crear la ventana principal
ventana_principal = tk.Tk()
ventana_principal.title("Calculadora de Triángulos Rectángulos")

# Crear menú de opciones
menu_opciones = tk.Menu(ventana_principal)
ventana_principal.config(menu=menu_opciones)

submenu = tk.Menu(menu_opciones, tearoff=0)
menu_opciones.add_cascade(label="Opciones", menu=submenu)

# Agregar opciones al menú
opciones = ["Cateto Opuesto", "Hipotenusa", "Cateto Opuesto y Ángulo Beta", "Cateto Adyacente y Ángulo Beta",
            "Hipotenusa y Ángulo Beta", "Cateto Opuesto y Ángulo Alpha", "Cateto Adyacente y Ángulo Alpha",
            "Hipotenusa y Ángulo Alpha", "Cateto Opuesto y Cateto Adyacente", "Cateto Adyacente e Hipotenusa",
            "Cateto Opuesto e Hipotenusa", "Cateto Opuesto, Cateto Adyacente e Hipotenusa",
            "Cateto Opuesto, Cateto Adyacente, Hipotenusa y Ángulo Alpha",
            "Cateto Opuesto, Cateto Adyacente, Hipotenusa y Ángulo Beta",
            "Cateto Opuesto, Cateto Adyacente y Ángulo Alpha",
            "Cateto Opuesto, Cateto Adyacente y Ángulo Beta",
            "Cateto Opuesto, Hipotenusa y Ángulo Alpha",
            "Cateto Adyacente, Hipotenusa y Ángulo Beta"]

for opcion in opciones:
    submenu.add_command(label=opcion, command=lambda op=opcion: mostrar_ventana(op))

# Función para cerrar la aplicación
def salir():
    ventana_principal.destroy()

# Agregar opción para salir en el menú
menu_opciones.add_command(label="Salir", command=salir)

# Iniciar el bucle principal
ventana_principal.mainloop()

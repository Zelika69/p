import tkinter as tk
from tkinter import ttk, messagebox

def clasificar_triangulo_por_lados(lado1, lado2, lado3):
    # Lógica para clasificar por lados (pendiente)
    return "Clasificación por lados no implementada."

def clasificar_triangulo_por_angulos(angulo1, angulo2, angulo3):
    # Validar si los ángulos forman un triángulo
    if angulo1 + angulo2 + angulo3 != 180:
        return "No es un triángulo válido."

    # Clasificar según los ángulos
    if all(angulo < 90 for angulo in [angulo1, angulo2, angulo3]):
        return "Triángulo Acutángulo"
    elif any(angulo > 90 for angulo in [angulo1, angulo2, angulo3]):
        return "Triángulo Obtusángulo"
    else:
        return "Triángulo Rectángulo"

def on_seleccionar_opcion(event):
    opcion_seleccionada = combo_opciones.get()
    
    if opcion_seleccionada == "Lados":
        # Ocultar campos de ángulos y mostrar campos de lados
        label_angulo1.grid_remove()
        label_angulo2.grid_remove()
        label_angulo3.grid_remove()
        entry_angulo1.grid_remove()
        entry_angulo2.grid_remove()
        entry_angulo3.grid_remove()

        label_lado1.grid(row=4, column=0, pady=5)
        label_lado2.grid(row=5, column=0, pady=5)
        label_lado3.grid(row=6, column=0, pady=5)
        entry_lado1.grid(row=4, column=1, pady=5)
        entry_lado2.grid(row=5, column=1, pady=5)
        entry_lado3.grid(row=6, column=1, pady=5)

    elif opcion_seleccionada == "Ángulos":
        # Ocultar campos de lados y mostrar campos de ángulos
        label_lado1.grid_remove()
        label_lado2.grid_remove()
        label_lado3.grid_remove()
        entry_lado1.grid_remove()
        entry_lado2.grid_remove()
        entry_lado3.grid_remove()

        label_angulo1.grid(row=4, column=0, pady=5)
        label_angulo2.grid(row=5, column=0, pady=5)
        label_angulo3.grid(row=6, column=0, pady=5)
        entry_angulo1.grid(row=4, column=1, pady=5)
        entry_angulo2.grid(row=5, column=1, pady=5)
        entry_angulo3.grid(row=6, column=1, pady=5)

def on_calcular():
    opcion_seleccionada = combo_opciones.get()

    if opcion_seleccionada == "Lados":
        lado1 = entry_lado1.get()
        lado2 = entry_lado2.get()
        lado3 = entry_lado3.get()

        # Validar campos de entrada vacíos
        if not lado1 or not lado2 or not lado3:
            campos_vacios = ", ".join([campo for campo, valor in zip(["Lado 1", "Lado 2", "Lado 3"], [lado1, lado2, lado3]) if not valor])
            messagebox.showerror("Error", f"Por favor, complete los siguientes campos: {campos_vacios}")
            return

        try:
            # Convertir los lados a números
            lado1 = float(lado1)
            lado2 = float(lado2)
            lado3 = float(lado3)

            # Obtener la clasificación e imprimir el resultado en un cuadro de diálogo
            resultado = clasificar_triangulo_por_lados(lado1, lado2, lado3)
            messagebox.showinfo("Resultado", f"El triángulo es: {resultado}")

        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese lados válidos.")

    elif opcion_seleccionada == "Ángulos":
        angulo1 = entry_angulo1.get()
        angulo2 = entry_angulo2.get()
        angulo3 = entry_angulo3.get()

        # Validar campos de entrada vacíos
        if not angulo1 or not angulo2 or not angulo3:
            campos_vacios = ", ".join([campo for campo, valor in zip(["Ángulo 1", "Ángulo 2", "Ángulo 3"], [angulo1, angulo2, angulo3]) if not valor])
            messagebox.showerror("Error", f"Por favor, complete los siguientes campos: {campos_vacios}")
            return

        try:
            # Convertir los ángulos a números
            angulo1 = float(angulo1)
            angulo2 = float(angulo2)
            angulo3 = float(angulo3)

            # Obtener la clasificación e imprimir el resultado en un cuadro de diálogo
            resultado = clasificar_triangulo_por_angulos(angulo1, angulo2, angulo3)
            messagebox.showinfo("Resultado", f"El triángulo es: {resultado}")

        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese ángulos válidos.")

# Crear la interfaz gráfica
root = tk.Tk()
root.title("Clasificador de Triángulos")

# Ajustar tamaño de la ventana
root.geometry("400x300")

# Crear y posicionar etiquetas y campos de entrada
tk.Label(root, text="Clasificación mediante:").grid(row=0, column=0, columnspan=2, pady=10)

# Menú desplegable
opciones = ["Lados", "Ángulos"]
combo_opciones = ttk.Combobox(root, values=opciones)
combo_opciones.set(opciones[0])
combo_opciones.grid(row=1, column=0, columnspan=2, pady=5)
combo_opciones.bind("<<ComboboxSelected>>", on_seleccionar_opcion)

label_lado1 = tk.Label(root, text="Lado 1:")
label_lado2 = tk.Label(root, text="Lado 2:")
label_lado3 = tk.Label(root, text="Lado 3:")

entry_lado1 = tk.Entry(root)
entry_lado2 = tk.Entry(root)
entry_lado3 = tk.Entry(root)

label_angulo1 = tk.Label(root, text="Ángulo 1:")
label_angulo2 = tk.Label(root, text="Ángulo 2:")
label_angulo3 = tk.Label(root, text="Ángulo 3:")

entry_angulo1 = tk.Entry(root)
entry_angulo2 = tk.Entry(root)
entry_angulo3 = tk.Entry(root)

# Botón para calcular
btn_calcular = tk.Button(root, text="Calcular", command=on_calcular)
btn_calcular.grid(row=7, column=0, columnspan=2, pady=10)

# Iniciar el bucle de eventos
root.mainloop()

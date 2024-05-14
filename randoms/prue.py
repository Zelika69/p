import tkinter as tk
from tkinter import ttk, messagebox

def validar_triangulo(angulo1, angulo2, angulo3):
    # Verificar si la suma de los ángulos es 180 (condición para ser un triángulo)
    return angulo1 + angulo2 + angulo3 == 180

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

def on_seleccionar_opcion(event):
    # Limpiar las entradas al cambiar la opción seleccionada
    entry_lado1.delete(0, tk.END)
    entry_lado2.delete(0, tk.END)
    entry_lado3.delete(0, tk.END)
    entry_angulo1.delete(0, tk.END)
    entry_angulo2.delete(0, tk.END)
    entry_angulo3.delete(0, tk.END)
    # Limpiar el mensaje de salida
    lbl_resultado.config(text="")

    opcion_seleccionada = combo_opciones.get()

    if opcion_seleccionada == "-------":
        # Ocultar campos de lados y ángulos
        label_lado1.grid_forget()
        entry_lado1.grid_forget()
        label_lado2.grid_forget()
        entry_lado2.grid_forget()
        label_lado3.grid_forget()
        entry_lado3.grid_forget()
        label_angulo1.grid_forget()
        entry_angulo1.grid_forget()
        label_angulo2.grid_forget()
        entry_angulo2.grid_forget()
        label_angulo3.grid_forget()
        entry_angulo3.grid_forget()

    elif opcion_seleccionada == "Lados":
        # Mostrar campos de lados y ocultar campos de ángulos
        label_angulo1.grid_forget()
        entry_angulo1.grid_forget()
        label_angulo2.grid_forget()
        entry_angulo2.grid_forget()
        label_angulo3.grid_forget()
        entry_angulo3.grid_forget()

        label_lado1.grid(row=3, column=0, pady=5, sticky="e")
        entry_lado1.grid(row=3, column=1, pady=5, padx=5)
        label_lado2.grid(row=4, column=0, pady=5, sticky="e")
        entry_lado2.grid(row=4, column=1, pady=5, padx=5)
        label_lado3.grid(row=5, column=0, pady=5, sticky="e")
        entry_lado3.grid(row=5, column=1, pady=5, padx=5)

    elif opcion_seleccionada == "Ángulos":
        # Mostrar campos de ángulos y ocultar campos de lados
        label_lado1.grid_forget()
        entry_lado1.grid_forget()
        label_lado2.grid_forget()
        entry_lado2.grid_forget()
        label_lado3.grid_forget()
        entry_lado3.grid_forget()

        label_angulo1.grid(row=3, column=0, pady=5, sticky="e")
        entry_angulo1.grid(row=3, column=1, pady=5, padx=5)
        label_angulo2.grid(row=4, column=0, pady=5, sticky="e")
        entry_angulo2.grid(row=4, column=1, pady=5, padx=5)
        label_angulo3.grid(row=5, column=0, pady=5, sticky="e")
        entry_angulo3.grid(row=5, column=1, pady=5, padx=5)

def on_calcular():
    opcion_seleccionada = combo_opciones.get()

    if opcion_seleccionada == "-------":
        messagebox.showinfo("Advertencia", "Por favor, seleccione una opción válida.")
        return

    elif opcion_seleccionada == "Lados":
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
            resultado = clasificar_triangulo(lado1, lado2, lado3)
            lbl_resultado.config(text=resultado, font=("Arial", 70))

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
            resultado = clasificar_triangulo(angulo1, angulo2, angulo3)
            lbl_resultado.config(text=resultado, font=("Arial", 70))

        except ValueError:
            messagebox.showerror("Error", "Por favor, ingrese ángulos válidos.")

# Crear la interfaz gráfica
root = tk.Tk()
root.title("Clasificador de Triángulos")

# Ajustar tamaño de la ventana y centrar
window_width = 300
window_height = 300
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x_coordinate = (screen_width - window_width) // 2
y_coordinate = (screen_height - window_height) // 2
root.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

# Configuración del estilo
style = ttk.Style()
style.configure("TLabel", padding=5, font=("Arial", 12))
style.configure("TEntry", padding=5, font=("Arial", 12))
style.configure("TButton", padding=5, font=("Arial", 12))
style.configure("TCombobox", padding=5, font=("Arial", 12))

# Crear y posicionar etiquetas y campos de entrada
tk.Label(root, text="Clasificación mediante:").grid(row=0, column=0, pady=10)

# Menú desplegable
opciones = ["-------", "Lados", "Ángulos"]
combo_opciones = ttk.Combobox(root, values=opciones, state="readonly")
combo_opciones.set(opciones[0])
combo_opciones.grid(row=0, column=1, pady=5)
combo_opciones.bind("<<ComboboxSelected>>", on_seleccionar_opcion)

label_lado1 = ttk.Label(root, text="Lado 1:")
entry_lado1 = ttk.Entry(root)

label_lado2 = ttk.Label(root, text="Lado 2:")
entry_lado2 = ttk.Entry(root)

label_lado3 = ttk.Label(root, text="Lado 3:")
entry_lado3 = ttk.Entry(root)

label_angulo1 = ttk.Label(root, text="Ángulo 1:")
entry_angulo1 = ttk.Entry(root)

label_angulo2 = ttk.Label(root, text="Ángulo 2:")
entry_angulo2 = ttk.Entry(root)

label_angulo3 = ttk.Label(root, text="Ángulo 3:")
entry_angulo3 = ttk.Entry(root)

# Etiqueta para el mensaje de resultado
lbl_resultado = tk.Label(root, text="", font=("Arial", 70), pady=10)
lbl_resultado.grid(row=3, column=2, rowspan=5, padx=10)

# Botón para calcular
btn_calcular = ttk.Button(root, text="Calcular", command=on_calcular)
btn_calcular.grid(row=6, column=0, columnspan=2, pady=10)

# Iniciar el bucle de eventos
root.mainloop()
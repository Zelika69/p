import tkinter as tk
from tkinter import ttk, messagebox
import math

def calcular_trianguo():
    try:
        # Obtener los valores de las entradas
        angulo1 = float(entry_angulo1.get())
        angulo2 = float(entry_angulo2.get())
        angulo3 = float(entry_angulo3.get())
        lado1 = float(entry_lado1.get())
        lado2 = float(entry_lado2.get())
        lado3 = float(entry_lado3.get())

        # Contar la cantidad de valores ingresados
        valores_ingresados = sum(1 for valor in [angulo1, angulo2, angulo3, lado1, lado2, lado3] if valor != 0)

        # Validar que se haya ingresado al menos un dato
        if valores_ingresados == 0:
            messagebox.showerror("Error", "Ingrese al menos un dato.")
            return

        # Validar que la suma de ángulos sea 180 (condición para ser un triángulo)
        if valores_ingresados == 3 and angulo1 + angulo2 + angulo3 != 180:
            messagebox.showerror("Error", "La suma de los ángulos debe ser 180 para formar un triángulo.")
            return

        # Validar que los lados sean positivos
        if any(lado <= 0 for lado in [lado1, lado2, lado3]):
            messagebox.showerror("Error", "Los lados deben ser números positivos.")
            return

        # Calcular los valores restantes en función de los datos proporcionados
        if valores_ingresados == 3:  # Se ingresaron todos los ángulos
            if lado1 == 0:
                lado1 = math.sqrt((lado2 ** 2 + lado3 ** 2 - 2 * lado2 * lado3 * math.cos(math.radians(angulo1))))
                entry_lado1.delete(0, tk.END)
                entry_lado1.insert(0, f"{lado1:.2f}")

            elif lado2 == 0:
                lado2 = math.sqrt((lado1 ** 2 + lado3 ** 2 - 2 * lado1 * lado3 * math.cos(math.radians(angulo2))))
                entry_lado2.delete(0, tk.END)
                entry_lado2.insert(0, f"{lado2:.2f}")

            elif lado3 == 0:
                lado3 = math.sqrt((lado1 ** 2 + lado2 ** 2 - 2 * lado1 * lado2 * math.cos(math.radians(angulo3))))
                entry_lado3.delete(0, tk.END)
                entry_lado3.insert(0, f"{lado3:.2f}")

        elif valores_ingresados == 1:  # Se ingresó un lado y dos ángulos
            # Calcular el ángulo restante
            if angulo1 == 0:
                angulo1 = 180 - angulo2 - angulo3
                entry_angulo1.delete(0, tk.END)
                entry_angulo1.insert(0, f"{angulo1:.2f}")

            elif angulo2 == 0:
                angulo2 = 180 - angulo1 - angulo3
                entry_angulo2.delete(0, tk.END)
                entry_angulo2.insert(0, f"{angulo2:.2f}")

            elif angulo3 == 0:
                angulo3 = 180 - angulo1 - angulo2
                entry_angulo3.delete(0, tk.END)
                entry_angulo3.insert(0, f"{angulo3:.2f}")

        elif valores_ingresados == 2:  # Se ingresó un ángulo y dos lados
            # Calcular el lado restante
            if lado1 == 0:
                lado1 = math.sqrt(lado2 ** 2 + lado3 ** 2 - 2 * lado2 * lado3 * math.cos(math.radians(angulo1)))
                entry_lado1.delete(0, tk.END)
                entry_lado1.insert(0, f"{lado1:.2f}")

            elif lado2 == 0:
                lado2 = math.sqrt(lado1 ** 2 + lado3 ** 2 - 2 * lado1 * lado3 * math.cos(math.radians(angulo2)))
                entry_lado2.delete(0, tk.END)
                entry_lado2.insert(0, f"{lado2:.2f}")

            elif lado3 == 0:
                lado3 = math.sqrt(lado1 ** 2 + lado2 ** 2 - 2 * lado1 * lado2 * math.cos(math.radians(angulo3)))
                entry_lado3.delete(0, tk.END)
                entry_lado3.insert(0, f"{lado3:.2f}")

    except ValueError:
        messagebox.showerror("Error", "Ingrese valores numéricos válidos.")

# Crear la interfaz gráfica
root = tk.Tk()
root.title("Calculadora de Triángulos")

# Configuración del estilo
style = ttk.Style()
style.configure("TLabel", padding=5, font=("Arial", 12))
style.configure("TEntry", padding=5, font=("Arial", 12))
style.configure("TButton", padding=5, font=("Arial", 12))

# Crear y posicionar etiquetas y campos de entrada
tk.Label(root, text="Ángulo 1 (°):").grid(row=0, column=0, pady=5, padx=5, sticky="e")
entry_angulo1 = ttk.Entry(root)
entry_angulo1.grid(row=0, column=1, pady=5, padx=5)

tk.Label(root, text="Ángulo 2 (°):").grid(row=1, column=0, pady=5, padx=5, sticky="e")
entry_angulo2 = ttk.Entry(root)
entry_angulo2.grid(row=1, column=1, pady=5, padx=5)

tk.Label(root, text="Ángulo 3 (°):").grid(row=2, column=0, pady=5, padx=5, sticky="e")
entry_angulo3 = ttk.Entry(root)
entry_angulo3.grid(row=2, column=1, pady=5, padx=5)

tk.Label(root, text="Lado 1:").grid(row=3, column=0, pady=5, padx=5, sticky="e")
entry_lado1 = ttk.Entry(root)
entry_lado1.grid(row=3, column=1, pady=5, padx=5)

tk.Label(root, text="Lado 2:").grid(row=4, column=0, pady=5, padx=5, sticky="e")
entry_lado2 = ttk.Entry(root)
entry_lado2.grid(row=4, column=1, pady=5, padx=5)

tk.Label(root, text="Lado 3:").grid(row=5, column=0, pady=5, padx=5, sticky="e")
entry_lado3 = ttk.Entry(root)
entry_lado3.grid(row=5, column=1, pady=5, padx=5)

# Botón para calcular
btn_calcular = ttk.Button(root, text="Calcular", command=calcular_trianguo)
btn_calcular.grid(row=6, column=0, columnspan=2, pady=10)

# Iniciar el bucle de eventos
root.mainloop()

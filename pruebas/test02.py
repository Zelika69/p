import tkinter as tk
from tkinter import ttk, messagebox
import math

def calcular_resultados():
    # Obtener los datos de las entradas
    try:
        CO = float(entry_co.get())
        CA = float(entry_ca.get())
    except ValueError:
        messagebox.showerror("Error", "Ingrese valores numéricos válidos para CO y CA.")
        return

    # Calcular la hipotenusa H
    H = math.sqrt(CO**2 + CA**2)

    # Calcular ángulo agudo θ en radianes
    theta_rad = math.asin(CO / H)
    theta_deg = math.degrees(theta_rad)

    # Calcular ángulo complementario α en radianes
    alpha_rad = math.asin(CA / H)
    alpha_deg = math.degrees(alpha_rad)

    # Calcular ángulo recto β en radianes
    beta_rad = math.asin(CO / CA)
    beta_deg = math.degrees(beta_rad)

    # Mostrar los resultados en las entradas correspondientes
    entry_resultados_theta.delete(0, tk.END)
    entry_resultados_theta.insert(0, f"{theta_deg:.2f} grados")

    entry_resultados_alpha.delete(0, tk.END)
    entry_resultados_alpha.insert(0, f"{alpha_deg:.2f} grados")

    entry_resultados_beta.delete(0, tk.END)
    entry_resultados_beta.insert(0, f"{beta_deg:.2f} grados")

    entry_resultados_co.delete(0, tk.END)
    entry_resultados_co.insert(0, CO)

    entry_resultados_ca.delete(0, tk.END)
    entry_resultados_ca.insert(0, CA)

    entry_resultados_h.delete(0, tk.END)
    entry_resultados_h.insert(0, f"{H:.2f}")

# Crear la interfaz gráfica
root = tk.Tk()
root.title("Cálculos Triángulo Rectángulo")

# Crear y posicionar etiquetas y campos de entrada
tk.Label(root, text="CO:").grid(row=0, column=0, pady=5, padx=10)
entry_co = ttk.Entry(root)
entry_co.grid(row=0, column=1, pady=5, padx=10)

tk.Label(root, text="CA:").grid(row=1, column=0, pady=5, padx=10)
entry_ca = ttk.Entry(root)
entry_ca.grid(row=1, column=1, pady=5, padx=10)

# Botón para calcular
btn_calcular = ttk.Button(root, text="Calcular", command=calcular_resultados)
btn_calcular.grid(row=2, column=0, columnspan=2, pady=10)

# Etiquetas para los resultados
tk.Label(root, text="Ángulo agudo θ:").grid(row=3, column=0, pady=5, padx=10)
entry_resultados_theta = ttk.Entry(root)
entry_resultados_theta.grid(row=3, column=1, pady=5, padx=10)

tk.Label(root, text="Ángulo complementario α:").grid(row=4, column=0, pady=5, padx=10)
entry_resultados_alpha = ttk.Entry(root)
entry_resultados_alpha.grid(row=4, column=1, pady=5, padx=10)

tk.Label(root, text="Ángulo recto β:").grid(row=5, column=0, pady=5, padx=10)
entry_resultados_beta = ttk.Entry(root)
entry_resultados_beta.grid(row=5, column=1, pady=5, padx=10)

tk.Label(root, text="Lado CO:").grid(row=6, column=0, pady=5, padx=10)
entry_resultados_co = ttk.Entry(root)
entry_resultados_co.grid(row=6, column=1, pady=5, padx=10)

tk.Label(root, text="Lado CA:").grid(row=7, column=0, pady=5, padx=10)
entry_resultados_ca = ttk.Entry(root)
entry_resultados_ca.grid(row=7, column=1, pady=5, padx=10)

tk.Label(root, text="Lado H:").grid(row=8, column=0, pady=5, padx=10)
entry_resultados_h = ttk.Entry(root)
entry_resultados_h.grid(row=8, column=1, pady=5, padx=10)

# Iniciar el bucle de eventos
root.mainloop()

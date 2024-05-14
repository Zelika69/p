import tkinter as tk
from tkinter import ttk, messagebox
import math

class TrianguloRectanguloCalculator:
    def __init__(self, root):
        self.root = root
        root.title("Cálculos Triángulo Rectángulo")

        # Crear y posicionar etiquetas y campos de entrada
        tk.Label(root, text="CO:").grid(row=0, column=0, pady=5, padx=10)
        self.var_co = tk.StringVar(value="")
        self.entry_co = ttk.Entry(root, textvariable=self.var_co)
        self.entry_co.grid(row=0, column=1, pady=5, padx=10)

        tk.Label(root, text="CA:").grid(row=1, column=0, pady=5, padx=10)
        self.var_ca = tk.StringVar(value="")
        self.entry_ca = ttk.Entry(root, textvariable=self.var_ca)
        self.entry_ca.grid(row=1, column=1, pady=5, padx=10)

        tk.Label(root, text="Hipotenusa H:").grid(row=2, column=0, pady=5, padx=10)
        self.var_h = tk.StringVar(value="")
        self.entry_h = ttk.Entry(root, textvariable=self.var_h)
        self.entry_h.grid(row=2, column=1, pady=5, padx=10)

        tk.Label(root, text="Ángulo θ:").grid(row=3, column=0, pady=5, padx=10)
        self.var_theta = tk.StringVar(value="")
        self.entry_theta = ttk.Entry(root, textvariable=self.var_theta)
        self.entry_theta.grid(row=3, column=1, pady=5, padx=10)

        tk.Label(root, text="Ángulo α:").grid(row=4, column=0, pady=5, padx=10)
        self.var_alpha = tk.StringVar(value="")
        self.entry_alpha = ttk.Entry(root, textvariable=self.var_alpha)
        self.entry_alpha.grid(row=4, column=1, pady=5, padx=10)

        tk.Label(root, text="Ángulo β:").grid(row=5, column=0, pady=5, padx=10)
        self.var_beta = tk.StringVar(value="")
        self.entry_beta = ttk.Entry(root, textvariable=self.var_beta)
        self.entry_beta.grid(row=5, column=1, pady=5, padx=10)

        # Botón para calcular
        btn_calcular = ttk.Button(root, text="Calcular", command=self.calcular_resultados)
        btn_calcular.grid(row=6, column=0, columnspan=2, pady=10)

        # Etiquetas para los resultados
        self.lbl_resultados_theta = tk.Label(root, text="")
        self.lbl_resultados_theta.grid(row=7, column=0, columnspan=2, pady=5, padx=10)

        self.lbl_resultados_alpha = tk.Label(root, text="")
        self.lbl_resultados_alpha.grid(row=8, column=0, columnspan=2, pady=5, padx=10)

        self.lbl_resultados_beta = tk.Label(root, text="")
        self.lbl_resultados_beta.grid(row=9, column=0, columnspan=2, pady=5, padx=10)

        self.lbl_resultados_co = tk.Label(root, text="")
        self.lbl_resultados_co.grid(row=10, column=0, columnspan=2, pady=5, padx=10)

        self.lbl_resultados_ca = tk.Label(root, text="")
        self.lbl_resultados_ca.grid(row=11, column=0, columnspan=2, pady=5, padx=10)

        self.lbl_resultados_h = tk.Label(root, text="")
        self.lbl_resultados_h.grid(row=12, column=0, columnspan=2, pady=5, padx=10)

    def calcular_resultados(self):
        # Obtener los datos de las entradas
        try:
            CO = float(self.var_co.get())
            CA = float(self.var_ca.get())
            H = float(self.var_h.get())
            theta = float(self.var_theta.get())
            alpha = float(self.var_alpha.get())
            beta = float(self.var_beta.get())
        except ValueError:
            messagebox.showerror("Error", "Ingrese valores numéricos válidos.")
            return

        # Verificar si se proporcionaron suficientes datos
        lados_ingresados = sum([1 for lado in [CO, CA, H] if lado])
        angulos_ingresados = sum([1 for angulo in [theta, alpha, beta] if angulo])

        if lados_ingresados >= 2 and angulos_ingresados == 0:
            # Calcular los ángulos
            if CO and CA:
                theta = math.degrees(math.atan(CA/CO))
                alpha = 90 - theta
                beta = 90
            elif CO and H:
                theta = math.degrees(math.acos(CO/H))
                alpha = 90 - theta
                beta = 90
            elif CA and H:
                theta = math.degrees(math.asin(CA/H))
                alpha = 90 - theta
                beta = 90

        elif angulos_ingresados >= 1 and lados_ingresados == 0:
            # Calcular los lados
            if theta and CA:
                CO = CA / math.tan(math.radians(theta))
                H = CA / math.sin(math.radians(theta))
            elif alpha and CA:
                CO = CA * math.tan(math.radians(alpha))
                H = CA / math.cos(math.radians(alpha))
            elif beta and CO:
                CA = CO * math.tan(math.radians(beta))
                H = CO / math.sin(math.radians(beta))

        elif lados_ingresados == 1 and angulos_ingresados == 1:
            # Calcular el lado y el ángulo restante
            if CO and theta:
                CA = CO * math.tan(math.radians(theta))
                H = CO / math.cos(math.radians(theta))
                alpha = 90 - theta
                beta = 90
            elif CA and theta:
                CO = CA / math.tan(math.radians(theta))
                H = CA / math.sin(math.radians(theta))
                alpha = 90 - theta
                beta = 90
            elif CO and alpha:
                CA = CO * math.tan(math.radians(alpha))
                H = CO / math.cos(math.radians(alpha))
                theta = 90 - alpha
                beta = 90
            elif CA and alpha:
                CO = CA / math.tan(math.radians(alpha))
                H = CA / math.sin(math.radians(alpha))
                theta = 90 - alpha
                beta = 90
            elif CO and beta:
                CA = CO / math.tan(math.radians(beta))
                H = CO / math.sin(math.radians(beta))
                alpha = 90 - beta
                theta = 90
            elif CA and beta:
                CO = CA * math.tan(math.radians(beta))
                H = CA / math.cos(math.radians(beta))
                alpha = 90 - beta
                theta = 90

        else:
            messagebox.showerror("Error", "Ingrese la cantidad correcta de valores (2 lados o 1 lado y 1 ángulo).")
            return

        # Actualizar las entradas con los resultados
        self.var_co.set(f"{CO:.2f}")
        self.var_ca.set(f"{CA:.2f}")
        self.var_h.set(f"{H:.2f}")
        self.var_theta.set(f"{theta:.2f}")
        self.var_alpha.set(f"{alpha:.2f}")
        self.var_beta.set(f"{beta:.2f}")

        # Mostrar los resultados en las etiquetas correspondientes
        self.lbl_resultados_theta.config(text=f"Ángulo agudo θ: {theta:.2f} grados")
        self.lbl_resultados_alpha.config(text=f"Ángulo complementario α: {alpha:.2f} grados")
        self.lbl_resultados_beta.config(text=f"Ángulo recto β: {beta:.2f} grados")
        self.lbl_resultados_co.config(text=f"Lado CO: {CO:.2f}")
        self.lbl_resultados_ca.config(text=f"Lado CA: {CA:.2f}")
        self.lbl_resultados_h.config(text=f"Lado H: {H:.2f}")

# Crear la interfaz gráfica
root = tk.Tk()
calculator = TrianguloRectanguloCalculator(root)

# Iniciar el bucle de eventos
root.mainloop()

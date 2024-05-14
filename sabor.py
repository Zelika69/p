import math
import tkinter as tk
from tkinter import simpledialog, messagebox, ttk

def solicitar_valor(titulo, prompt):
    valor = None

    def guardar_valor():
        nonlocal valor
        valor = float(entry.get())
        ventana.destroy()

    ventana = tk.Toplevel()
    ventana.title(titulo)
    
    label_prompt = tk.Label(ventana, text=prompt, font=("Arial", 14))  # Aquí puedes ajustar el tamaño del texto
    label_prompt.pack(padx=10, pady=5)

    entry = tk.Entry(ventana, font=("Arial", 12))  # Aquí puedes ajustar el tamaño del texto
    entry.pack(padx=10, pady=5)

    boton_aceptar = tk.Button(ventana, text="Aceptar", command=guardar_valor, font=("Arial", 12))  # Aquí puedes ajustar el tamaño del texto
    boton_aceptar.pack(padx=10, pady=5)

    ventana.mainloop()

    return valor    

class UnidadesDialog(tk.Toplevel):
    def __init__(self, parent, title=None, prompt=None, options=None):
        super().__init__(parent)
        self.transient(parent)
        self.title(title)
        self.prompt = prompt
        self.options = options
        self.result = None

        self.body()

        self.grab_set()
        self.protocol("WM_DELETE_WINDOW", self.cancel)
        self.wait_window(self)

    def body(self):
        self.label = tk.Label(self, text=self.prompt)
        self.label.pack()
        self.var = tk.StringVar(self)
        self.var.set(self.options[0])
        for option in self.options:
            rb = tk.Radiobutton(self, text=option, variable=self.var, value=option)
            rb.pack(anchor="w")

        self.button_ok = tk.Button(self, text="OK", command=self.ok)
        self.button_ok.pack(side=tk.LEFT, padx=5, pady=5)
        self.button_cancel = tk.Button(self, text="Cancelar", command=self.cancel)
        self.button_cancel.pack(side=tk.LEFT, padx=5, pady=5)

    def ok(self):
        self.result = self.var.get()
        self.destroy()

    def cancel(self):
        self.result = None
        self.destroy()

def validar_angulos(angulo_alpha, angulo_beta):
    if angulo_alpha or angulo_beta > 90:
        return "Lo siento pero el triángulo no puede existir"

def calcular_triangulo_rectangulo(opcion):
    while True:
        if opcion == 1:
            cateto_opuesto = simpledialog.askfloat("Cateto Opuesto", "Ingrese la medida del cateto opuesto: ")
            if cateto_opuesto is None or cateto_opuesto == 0:
                messagebox.showerror("Error", "Ingrese un valor válido.")
                continue
            cateto_adyacente = cateto_opuesto
            hipotenusa = math.sqrt((cateto_adyacente**2)+(cateto_opuesto**2))
            angulo_alpha = math.degrees(math.asin(cateto_opuesto/hipotenusa))
            angulo_beta = 90-angulo_alpha
            break
    
        elif opcion == 2:
            hipotenusa = simpledialog.askfloat("Hipotenusa", "Ingrese la medida de la Hipotenusa: ")
            if hipotenusa is None or hipotenusa == 0:
                messagebox.showerror("Error", "Ingrese un valor válido.")
                continue
            cateto_adyacente = hipotenusa/(math.sqrt(2))
            cateto_opuesto = cateto_adyacente
            angulo_alpha = math.degrees(math.asin(cateto_opuesto/hipotenusa))
            angulo_beta = 90-angulo_alpha
            break
        
        elif opcion == 3:
            cateto_opuesto = solicitar_valor("Cateto Opuesto", "Ingrese la medida del cateto opuesto:")
            while True:
                cateto_opuesto = solicitar_valor("Cateto Opuesto", "Ingrese la medida del cateto opuesto:")
                if cateto_opuesto is None or cateto_opuesto == 0:
                    messagebox.showerror("Error", "Ingrese un valor válido.")
                    cateto_opuesto = solicitar_valor("Cateto Opuesto", "Ingrese la medida del cateto opuesto:")
                else:
                    break
            while True:
                angulo_beta = simpledialog.askfloat("Ángulo Beta", "Ingrese el valor del ángulo beta (en grados): ")
                if angulo_beta is None or angulo_beta == 0 or angulo_beta > 90 or angulo_beta == 90:
                    messagebox.showerror("Error", "Ingrese un valor válido.")
                else:
                    break
            angulo_alpha = 90 -(angulo_beta)
            cateto_adyacente = cateto_opuesto / math.tan(math.radians(angulo_alpha))
            hipotenusa = cateto_opuesto / math.sin(math.radians(angulo_alpha))
            if cateto_opuesto + cateto_adyacente > hipotenusa and cateto_opuesto + hipotenusa > cateto_adyacente and cateto_adyacente + hipotenusa > cateto_opuesto:  
                nota = '''
    Nota: Estos son los  valores calculados 
    para el triángulo rectangulo.'''
            else:
                nota = "Nota: No es posible hacer estos calculos."
                angulo_alpha = 0
                angulo_beta = 0
                cateto_adyacente = 0
                cateto_opuesto = 0
                hipotenusa = 0
                
            break

        elif opcion == 4:
            cateto_adyacente = simpledialog.askfloat("Cateto Adyacente", "Ingrese la medida del cateto adyacente: ")
            angulo_beta = simpledialog.askfloat("Ángulo Beta", "Ingrese el valor del ángulo beta (en grados): ")
            angulo_alpha = 90 -(angulo_beta)
            cateto_opuesto = cateto_adyacente * math.tan(math.radians(angulo_alpha))
            hipotenusa = math.sqrt((cateto_opuesto**2)+(cateto_adyacente**2))
            break

        elif opcion == 5:
            hipotenusa = simpledialog.askfloat("Hipotenusa", "Ingrese la medida de la hipotenusa: ")
            angulo_beta = simpledialog.askfloat("Ángulo Beta", "Ingrese el valor del ángulo beta (en grados): ")
            angulo_alpha = 90-angulo_beta
            cateto_opuesto = hipotenusa * math.sin(math.radians(angulo_alpha))
            cateto_adyacente = math.sqrt((hipotenusa**2)-(cateto_opuesto**2))
            break

        elif opcion == 6:
            cateto_opuesto = simpledialog.askfloat("Cateto Opuesto", "Ingrese la medida del cateto opuesto: ")
            angulo_alpha = simpledialog.askfloat("Ángulo Alpha", "Ingrese el valor del ángulo alpha (en grados): ")
            angulo_beta = 90 -(angulo_alpha)
            cateto_adyacente = cateto_opuesto / math.tan(math.radians(angulo_alpha))
            hipotenusa = cateto_opuesto / math.sin(math.radians(angulo_alpha))
            break

        elif opcion == 7:
            cateto_adyacente = simpledialog.askfloat("Cateto Adyacente", "Ingrese la medida del cateto adyacente: ")
            angulo_alpha = simpledialog.askfloat("Ángulo Alpha", "Ingrese el valor del ángulo alpha (en grados): ")
            angulo_beta = 90 -(angulo_alpha)
            cateto_opuesto = cateto_adyacente * math.tan(math.radians(angulo_alpha))
            hipotenusa = math.sqrt((cateto_opuesto**2)+(cateto_adyacente**2))
            break

        elif opcion == 8:
            hipotenusa = simpledialog.askfloat("Hipotenusa", "Ingrese la medida de la hipotenusa: ")
            angulo_alpha = simpledialog.askfloat("Ángulo Alpha", "Ingrese el valor del ángulo alpha (en grados): ")
            angulo_beta = 90-angulo_alpha
            cateto_opuesto = hipotenusa * math.sin(math.radians(angulo_alpha))
            cateto_adyacente = math.sqrt((hipotenusa**2)-(cateto_opuesto**2))
            break

        elif opcion == 9:
            cateto_opuesto = simpledialog.askfloat("Cateto Opuesto", "Ingrese la medida del cateto opuesto: ")
            cateto_adyacente = simpledialog.askfloat("Cateto Adyacente", "Ingrese la medida del cateto adyacente: ")
            hipotenusa = math.sqrt((cateto_opuesto**2)+(cateto_adyacente**2))
            angulo_alpha = math.degrees(math.asin(cateto_opuesto/hipotenusa))
            angulo_beta = 90-angulo_alpha
            break

        elif opcion == 10:
            cateto_adyacente = simpledialog.askfloat("Cateto Adyacente", "Ingrese la medida del cateto adyacente: ")
            hipotenusa = simpledialog.askfloat("Hipotenusa", "Ingrese la medida de la hipotenusa: ")
            cateto_opuesto = math.sqrt((hipotenusa**2)-(cateto_adyacente**2))
            angulo_alpha = math.degrees(math.acos(cateto_adyacente/hipotenusa))
            angulo_beta = 90-angulo_alpha
            break

        elif opcion == 11:
            cateto_opuesto = simpledialog.askfloat("Cateto Opuesto", "Ingrese la medida del cateto opuesto: ")
            hipotenusa = simpledialog.askfloat("Hipotenusa", "Ingrese la medida de la hipotenusa: ")
            cateto_adyacente = math.sqrt((hipotenusa**2)-(cateto_opuesto**2))
            angulo_alpha = math.degrees(math.asin(cateto_opuesto/hipotenusa))
            angulo_beta = 90-angulo_alpha
            break

        elif opcion == 12:
            cateto_opuesto = simpledialog.askfloat("Cateto Opuesto", "Ingrese la medida del cateto opuesto: ")
            cateto_adyacente = simpledialog.askfloat("Cateto Adyacente", "Ingrese la medida del cateto adyacente: ")
            hipotenusa = simpledialog.askfloat("Hipotenusa", "Ingrese la medida de la hipotenusa: ")
            angulo_alpha = math.degrees(math.asin(cateto_opuesto/hipotenusa))
            angulo_beta = 90-angulo_alpha
            break

        elif opcion == 13:
            cateto_opuesto = simpledialog.askfloat("Cateto Opuesto", "Ingrese la medida del cateto opuesto: ")
            cateto_adyacente = simpledialog.askfloat("Cateto Adyacente", "Ingrese la medida del cateto adyacente: ")
            hipotenusa = simpledialog.askfloat("Hipotenusa", "Ingrese la medida de la hipotenusa: ")
            angulo_alpha = simpledialog.askfloat("Ángulo Alpha", "Ingrese el valor del ángulo alpha (en grados): ")
            angulo_beta = 90 -(angulo_alpha)
            break

        elif opcion == 14:
            cateto_opuesto = simpledialog.askfloat("Cateto Opuesto", "Ingrese la medida del cateto opuesto: ")
            cateto_adyacente = simpledialog.askfloat("Cateto Adyacente", "Ingrese la medida del cateto adyacente: ")
            hipotenusa = simpledialog.askfloat("Hipotenusa", "Ingrese la medida de la hipotenusa: ")
            angulo_beta = simpledialog.askfloat("Ángulo Beta", "Ingrese el valor del ángulo beta (en grados): ")
            angulo_alpha = 90 -(angulo_beta)
            break

        elif opcion == 15:
            cateto_opuesto = simpledialog.askfloat("Cateto Opuesto", "Ingrese la medida del cateto opuesto: ")
            cateto_adyacente = simpledialog.askfloat("Cateto Adyacente", "Ingrese la medida del cateto adyacente: ")
            angulo_alpha = simpledialog.askfloat("Ángulo Alpha", "Ingrese el valor del ángulo alpha (en grados): ")
            hipotenusa = math.sqrt((cateto_opuesto**2)+(cateto_adyacente**2))
            angulo_beta = 90 -(angulo_alpha)
            break

        elif opcion == 16:
            cateto_opuesto = simpledialog.askfloat("Cateto Opuesto", "Ingrese la medida del cateto opuesto: ")
            cateto_adyacente = simpledialog.askfloat("Cateto Adyacente", "Ingrese la medida del cateto adyacente: ")
            angulo_beta = simpledialog.askfloat("Ángulo Beta", "Ingrese el valor del ángulo beta (en grados): ")
            angulo_alpha = 90 -(angulo_beta)
            hipotenusa = math.sqrt((cateto_opuesto**2)+(cateto_adyacente**2))
            break

        elif opcion == 17:
            cateto_opuesto = simpledialog.askfloat("Cateto Opuesto", "Ingrese la medida del cateto opuesto: ")
            hipotenusa = simpledialog.askfloat("Hipotenusa", "Ingrese la medida de la hipotenusa: ")
            angulo_alpha = simpledialog.askfloat("Ángulo Alpha", "Ingrese el valor del ángulo alpha (en grados): ")
            angulo_beta = 90-angulo_alpha
            break

        elif opcion == 18:
            cateto_adyacente = simpledialog.askfloat("Cateto Adyacente", "Ingrese la medida del cateto adyacente: ")
            hipotenusa = simpledialog.askfloat("Hipotenusa", "Ingrese la medida de la hipotenusa: ")
            angulo_beta = simpledialog.askfloat("Ángulo Beta", "Ingrese el valor del ángulo beta (en grados): ")
            angulo_alpha = 90-angulo_beta
            break

        else:
            messagebox.showerror("Error", "Opción no válida.")
            return None

    return cateto_opuesto, cateto_adyacente, hipotenusa, angulo_alpha, angulo_beta, nota

def mostrar_resultados(resultados, unidades):
    if resultados:
        ventana_resultados = tk.Toplevel()
        ventana_resultados.title("Resultados")

        label_resultados = tk.Label(ventana_resultados, text="Resultados", font=("Arial", 30, "bold"))
        label_resultados.pack()

        frame_resultados = tk.Frame(ventana_resultados)
        frame_resultados.pack(padx=20, pady=10)

        label_cateto_opuesto = tk.Label(frame_resultados, text=f"Cateto Opuesto: {resultados[0]:.8f} {unidades}", font=("Arial", 20))
        label_cateto_opuesto.grid(row=0, column=0, sticky="w", padx=10, pady=5)

        label_cateto_adyacente = tk.Label(frame_resultados, text=f"Cateto Adyacente: {resultados[1]:.8f} {unidades}", font=("Arial", 20))
        label_cateto_adyacente.grid(row=1, column=0, sticky="w", padx=10, pady=5)

        label_hipotenusa = tk.Label(frame_resultados, text=f"Hipotenusa: {resultados[2]:.8f} {unidades}", font=("Arial", 20))
        label_hipotenusa.grid(row=2, column=0, sticky="w", padx=10, pady=5)

        label_angulo_alpha = tk.Label(frame_resultados, text=f"Ángulo Alpha: {resultados[3]:.8f}°", font=("Arial", 20))
        label_angulo_alpha.grid(row=3, column=0, sticky="w", padx=10, pady=5)

        label_angulo_beta = tk.Label(frame_resultados, text=f"Ángulo Beta: {resultados[4]:.8f}°", font=("Arial", 20))
        label_angulo_beta.grid(row=4, column=0, sticky="w", padx=10, pady=5)
        
        label_nota = tk.Label(frame_resultados, text=f"{resultados[5]}", font=("Arial", 20))
        label_nota.grid(row=9, column=0, sticky="w", padx=10, pady=5)

        
        def cambiar_unidades(nuevas_unidades):
            factor = 1
            if unidades == "m" and nuevas_unidades == "cm":
                factor = 100
            elif unidades == "m" and nuevas_unidades == "mm":
                factor = 1000
            elif unidades == "m" and nuevas_unidades == "km":
                factor = 0.001
            elif unidades == "m" and nuevas_unidades == "dm":
                factor = 10
            elif unidades == "m" and nuevas_unidades == "dam":
                factor = 0.1  # 1 metro es igual a 0.1 decámetros
            elif unidades == "m" and nuevas_unidades == "μm":
                factor = 1000000
            elif unidades == "m" and nuevas_unidades == "nm":
                factor = 1000000000
            elif unidades == "m" and nuevas_unidades == "yd":
                factor  = 1.0936133
            elif unidades == "m" and nuevas_unidades == "in":
                factor = 39.3700787
            elif unidades == "m" and nuevas_unidades == "mi":
                factor = 0.00062137
            elif unidades == "m" and nuevas_unidades == "milla nautica":
                factor = (1/1852)
            elif unidades == "m" and nuevas_unidades == "ft":
                factor = 3.2808399
                
            elif unidades == "cm" and nuevas_unidades == "m":
                factor = 0.01
            elif unidades == "cm" and nuevas_unidades == "mm":
                factor = 10
            elif unidades == "cm" and nuevas_unidades == "km":
                factor = 0.00001
            elif unidades == "cm" and nuevas_unidades == "dm":
                factor = 0.1
            elif unidades == "cm" and nuevas_unidades == "dam":
                factor = 0.01  # 1 centímetro es igual a 0.01 decámetros
            elif unidades == "cm" and nuevas_unidades == "μm":
                factor = 10000
            elif unidades == "cm" and nuevas_unidades == "nm":
                factor = 10000000
            elif unidades == "cm" and nuevas_unidades == "yd":
                factor = 0.01093613
            elif unidades == "cm" and nuevas_unidades == "in":
                factor = 0.39370079
            elif unidades == "cm" and nuevas_unidades == "mi":
                factor = 393.700787
            elif  unidades == "cm" and nuevas_unidades == "milla nautica":
                factor = (1/(1852*100))
            elif unidades == "cm" and nuevas_unidades == "ft":
                factor = 0.0328084
    
            elif unidades == "mm" and nuevas_unidades == "m":
                factor = 0.001
            elif unidades == "mm" and nuevas_unidades == "cm":
                factor = 0.1
            elif unidades == "mm" and nuevas_unidades == "km":
                factor = 0.000001
            elif unidades == "mm" and nuevas_unidades == "dm":
                factor = 0.01
            elif unidades == "mm" and nuevas_unidades == "dam":
                factor = 0.0001
            elif unidades == "mm" and nuevas_unidades == "μm":
                factor = 1000
            elif unidades == "mm" and nuevas_unidades == "nm":
                factor = 1000000
            elif unidades == "mm" and nuevas_unidades == "yd":
                factor = 0.0010936132983377
            elif unidades == "mm" and nuevas_unidades == "in":
                factor = 0.039370078740157
            elif unidades == "mm" and nuevas_unidades == "mi":
                factor = 6.2137119223733*(10**-7)
            elif unidades == "mm" and nuevas_unidades == "milla nautica":
                factor = 5.3995680345572*(10**-7)
            elif unidades == "mm" and nuevas_unidades == "ft":
                factor = 0.0032808398950131
                
            elif unidades == "km" and nuevas_unidades == "m":
                factor = 1000
            elif unidades == "km" and nuevas_unidades == "cm":
                factor = 100000
            elif unidades == "km" and nuevas_unidades == "mm":
                factor = 1000000
            elif unidades == "km" and nuevas_unidades == "dm":
                factor = 10000  # 1 kilómetro es igual a 10000 decímetros
            elif unidades == "km" and nuevas_unidades == "dam":
                factor = 1000  # 1 kilómetro es igual a 1000 decámetros
            elif unidades == "km" and nuevas_unidades == "μm":
                factor = 1e9  # 1 kilómetro es igual a 1e9 micrómetros
            elif unidades == "km" and nuevas_unidades == "nm":
                factor = 1e12  # 1 kilómetro es igual a 1e12 nanómetros
            elif unidades == "km" and nuevas_unidades == "yd":
                factor = 1093.6133  # 1 kilómetro es igual a 1093.6133 yardas
            elif unidades == "km" and nuevas_unidades == "in":
                factor = 39370.0787  # 1 kilómetro es igual a 39370.0787 pulgadas
            elif unidades == "km" and nuevas_unidades == "mi":
                factor = 0.621371  # 1 kilómetro es igual a 0.621371 millas
            elif unidades == "km" and nuevas_unidades == "milla nautica":
                factor = 0.539957  # 1 kilómetro es igual a 0.539957 millas náuticas
            elif unidades == "km" and nuevas_unidades == "ft":
                factor = 3280.84  # 1 kilómetro es igual a 3280.84 pies

                
            elif unidades == "yd" and nuevas_unidades == "m":
                factor = 0.9144  # 1 yarda es aproximadamente 0.9144 metros
            elif unidades == "yd" and nuevas_unidades == "cm":
                factor = 91.44  # 1 yarda es aproximadamente 91.44 centímetros
            elif unidades == "yd" and nuevas_unidades == "km":
                factor = 0.0009144  # 1 yarda es igual a 0.0009144 kilómetros
            elif unidades == "yd" and nuevas_unidades == "mm":
                factor = 914.4  # 1 yarda es aproximadamente 914.4 milímetros
            elif unidades == "yd" and nuevas_unidades == "dm":
                factor = 9.144  # 1 yarda es igual a 9.144 decímetros
            elif unidades == "yd" and nuevas_unidades == "dam":
                factor = 0.09144  # 1 yarda es igual a 0.09144 decámetros
            elif unidades == "yd" and nuevas_unidades == "in":
                factor = 36  # 1 yarda es exactamente 36 pulgadas
            elif unidades == "yd" and nuevas_unidades == "mi":
                factor = 0.000568182  # 1 yarda es aproximadamente 0.000568182 millas
            elif unidades == "yd" and nuevas_unidades == "milla nautica":
                factor = 0.000493737  # 1 yarda es aproximadamente 0.000493737 millas náuticas
            elif unidades == "yd" and nuevas_unidades == "μm":
                factor = 914400   # 1 yarda es exactamente 914400000 micrómetros
            elif unidades == "yd" and nuevas_unidades == "nm":
                factor = 914400000  # 1 yarda es igual a 914400000 nanómetros
            elif unidades == "yd" and nuevas_unidades == "ft":
                factor = 3  # 1 yarda es igual a 3 pies
                
            elif unidades == "dm" and nuevas_unidades == "m":
                factor = 0.1  # 1 decímetro es igual a 0.1 metros
            elif unidades == "dm" and nuevas_unidades == "km":
                factor = 0.0001  # 1 decímetro es igual a 0.0001 kilómetros
            elif unidades == "dm" and nuevas_unidades == "cm":
                factor = 10  # 1 decímetro es igual a 10 centímetros
            elif unidades == "dm" and nuevas_unidades == "mm":
                factor = 100  # 1 decímetro es igual a 100 milímetros
            elif unidades == "dm" and nuevas_unidades == "dam":
                factor = 0.01  # 1 decímetro es igual a 0.01 decámetros
            elif unidades == "dm" and nuevas_unidades == "μm":
                factor = 100000  # 1 decímetro es igual a 100000 micrómetros
            elif unidades == "dm" and nuevas_unidades == "nm":
                factor = 100000000  # 1 decímetro es igual a 100000000 nanómetros
            elif unidades == "dm" and nuevas_unidades == "yd":
                factor = 0.1093613  # 1 decímetro es igual a 0.1093613 yardas
            elif unidades == "dm" and nuevas_unidades == "in":
                factor = 3.9370079  # 1 decímetro es igual a 3.9370079 pulgadas
            elif unidades == "dm" and nuevas_unidades == "mi":
                factor = 0.0000621371  # 1 decímetro es igual a 0.0000621371 millas
            elif unidades == "dm" and nuevas_unidades == "milla nautica":
                factor = 0.0000539957  # 1 decímetro es igual a 0.0000539957 millas náuticas
            elif unidades == "dm" and nuevas_unidades == "ft":
                factor = 0.328084  # 1 decímetro es igual a 0.328084 pies
                
            elif unidades == "dam" and nuevas_unidades == "m":
                factor = 10  # 1 decámetro es igual a 10 metros
            elif unidades == "dam" and nuevas_unidades == "km":
                factor = 0.01  # 1 decámetro es igual a 0.01 kilómetros
            elif unidades == "dam" and nuevas_unidades == "cm":
                factor = 1000  # 1 decámetro es igual a 1000 centímetros
            elif unidades == "dam" and nuevas_unidades == "dm":
                factor = 10  # 1 decámetro es igual a 10 decímetros
            elif unidades == "dam" and nuevas_unidades == "mm":
                factor = 10000  # 1 decámetro es igual a 10,000 milímetros
            elif unidades == "dam" and nuevas_unidades == "μm":
                factor = 10000000  # 1 decámetro es igual a 10,000,000 micrómetros
            elif unidades == "dam" and nuevas_unidades == "nm":
                factor = 10000000000  # 1 decámetro es igual a 10,000,000,000 nanómetros
            elif unidades == "dam" and nuevas_unidades == "yd":
                factor = 10.9361  # 1 decámetro es igual a 10.9361 yardas
            elif unidades == "dam" and nuevas_unidades == "in":
                factor = 393.701  # 1 decámetro es igual a 393.701 pulgadas
            elif unidades == "dam" and nuevas_unidades == "mi":
                factor = 0.00621371  # 1 decámetro es igual a 0.00621371 millas
            elif unidades == "dam" and nuevas_unidades == "milla nautica":
                factor = 0.00539957  # 1 decámetro es igual a 0.00539957 millas náuticas
            elif unidades == "dam" and nuevas_unidades == "ft":
                factor = 32.8084  # 1 decámetro es igual a 32.8084 pies
                
            elif unidades == "μm" and nuevas_unidades == "m":
                factor = 1e-6  # 1 micrómetro es igual a 1x10^-6 metros
            elif unidades == "μm" and nuevas_unidades == "cm":
                factor = 1e-4  # 1 micrómetro es igual a 1x10^-4 centímetros
            elif unidades == "μm" and nuevas_unidades == "mm":
                factor = 0.001  # 1 micrómetro es igual a 0.001 milímetros
            elif unidades == "μm" and nuevas_unidades == "km":
                factor = 1e-9  # 1 micrómetro es igual a 1x10^-9 kilómetros
            elif unidades == "μm" and nuevas_unidades == "dam":
                factor = 1e-7  # 1 micrómetro es igual a 1x10^-7 decámetros
            elif unidades == "μm" and nuevas_unidades == "dm":
                factor = 1e-5  # 1 micrómetro es igual a 1x10^-5 decímetros
            elif unidades == "μm" and nuevas_unidades == "nm":
                factor = 1000  # 1 micrómetro es igual a 1000 nanómetros
            elif unidades == "μm" and nuevas_unidades == "yd":
                factor = 1.09361e-6  # 1 micrómetro es igual a 1.09361x10^-6 yardas
            elif unidades == "μm" and nuevas_unidades == "in":
                factor = 3.93701e-5  # 1 micrómetro es igual a 3.93701x10^-5 pulgadas
            elif unidades == "μm" and nuevas_unidades == "mi":
                factor = 6.2137e-10  # 1 micrómetro es igual a 6.2137x10^-10 millas
            elif unidades == "μm" and nuevas_unidades == "milla nautica":
                factor = 5.39957e-10  # 1 micrómetro es igual a 5.39957x10^-10 millas náuticas
            elif unidades == "μm" and nuevas_unidades == "ft":
                factor = 3.28084e-6  # 1 micrómetro es igual a 3.28084x10^-6 pies
                
            elif unidades == "nm" and nuevas_unidades == "m":
                factor = 1e-9  # 1 nanómetro es igual a 1x10^-9 metros
            elif unidades == "nm" and nuevas_unidades == "cm":
                factor = 1e-7  # 1 nanómetro es igual a 1x10^-7 centímetros
            elif unidades == "nm" and nuevas_unidades == "mm":
                factor = 1e-6  # 1 nanómetro es igual a 1x10^-6 milímetros
            elif unidades == "nm" and nuevas_unidades == "km":
                factor = 1e-12  # 1 nanómetro es igual a 1x10^-12 kilómetros
            elif unidades == "nm" and nuevas_unidades == "μm":
                factor = 0.001  # 1 nanómetro es igual a 0.001 micrómetros
            elif unidades == "nm" and nuevas_unidades == "dam":
                factor = 1e-8  # 1 nanómetro es igual a 1x10^-8 decámetros
            elif unidades == "nm" and nuevas_unidades == "dm":
                factor = 1e-6  # 1 nanómetro es igual a 1x10^-6 decímetros
            elif unidades == "nm" and nuevas_unidades == "yd":
                factor = 1.09361e-9  # 1 nanómetro es igual a 1.09361x10^-9 yardas
            elif unidades == "nm" and nuevas_unidades == "in":
                factor = 3.93701e-8  # 1 nanómetro es igual a 3.93701x10^-8 pulgadas
            elif unidades == "nm" and nuevas_unidades == "mi":
                factor = 6.2137e-13  # 1 nanómetro es igual a 6.2137x10^-13 millas
            elif unidades == "nm" and nuevas_unidades == "milla nautica":
                factor = 5.39957e-13  # 1 nanómetro es igual a 5.39957x10^-13 millas náuticas
            elif unidades == "nm" and nuevas_unidades == "ft":
                factor = 3.28084e-9  # 1 nanómetro es igual a 3.28084x10^-9 pies
                
            elif unidades == "in" and nuevas_unidades == "m":
                factor = 0.0254  # 1 pulgada es igual a 0.0254 metros
            elif unidades == "in" and nuevas_unidades == "cm":
                factor = 2.54  # 1 pulgada es igual a 2.54 centímetros
            elif unidades == "in" and nuevas_unidades == "mm":
                factor = 25.4  # 1 pulgada es igual a 25.4 milímetros
            elif unidades == "in" and nuevas_unidades == "km":
                factor = 2.54e-5  # 1 pulgada es igual a 2.54x10^-5 kilómetros
            elif unidades == "in" and nuevas_unidades == "dam":
                factor = 0.00254  # 1 pulgada es igual a 0.00254 decámetros
            elif unidades == "in" and nuevas_unidades == "dm":
                factor = 0.254  # 1 pulgada es igual a 0.254 decímetros
            elif unidades == "in" and nuevas_unidades == "nm":
                factor = 25400000  # 1 pulgada es igual a 25400000 nanómetros
            elif unidades == "in" and nuevas_unidades == "yd":
                factor = 0.0277778  # 1 pulgada es igual a 0.0277778 yardas
            elif unidades == "in" and nuevas_unidades == "μm":
                factor = 25400  # 1 pulgada es igual a 25400 micrómetros
            elif unidades == "in" and nuevas_unidades == "mi":
                factor = 1.5783e-5  # 1 pulgada es igual a 1.5783x10^-5 millas
            elif unidades == "in" and nuevas_unidades == "milla nautica":
                factor = 1.3715e-5  # 1 pulgada es igual a 1.3715x10^-5 millas náuticas
            elif unidades == "in" and nuevas_unidades == "ft":
                factor = 0.0833333  # 1 pulgada es igual a 0.0833333 pies
                
            elif unidades == "mi" and nuevas_unidades == "m":
                factor = 1609.34  # 1 milla es igual a 1609.34 metros
            elif unidades == "mi" and nuevas_unidades == "cm":
                factor = 160934  # 1 milla es igual a 160934 centímetros
            elif unidades == "mi" and nuevas_unidades == "mm":
                factor = 1.609e+6  # 1 milla es igual a 1.609x10^6 milímetros
            elif unidades == "mi" and nuevas_unidades == "km":
                factor = 1.60934  # 1 milla es igual a 1.60934 kilómetros
            elif unidades == "mi" and nuevas_unidades == "dam":
                factor = 160.934  # 1 milla es igual a 160.934 decámetros
            elif unidades == "mi" and nuevas_unidades == "dm":
                factor = 16093.4  # 1 milla es igual a 16093.4 decímetros
            elif unidades == "mi" and nuevas_unidades == "nm":
                factor = 1.609e+12  # 1 milla es igual a 1.609x10^12 nanómetros
            elif unidades == "mi" and nuevas_unidades == "yd":
                factor = 1760  # 1 milla es igual a 1760 yardas
            elif unidades == "mi" and nuevas_unidades == "μm":
                factor = 1.609e+9  # 1 milla es igual a 1.609x10^9 micrómetros
            elif unidades == "mi" and nuevas_unidades == "in":
                factor = 63360  # 1 milla es igual a 63360 pulgadas
            elif unidades == "mi" and nuevas_unidades == "milla nautica":
                factor = 0.868976  # 1 milla es igual a 0.868976 millas náuticas
            elif unidades == "mi" and nuevas_unidades == "ft":
                factor = 5280  # 1 milla es igual a 5280 pies
                
            elif unidades == "milla nautica" and nuevas_unidades == "m":
                factor = 1852  # 1 milla náutica es igual a 1852 metros
            elif unidades == "milla nautica" and nuevas_unidades == "cm":
                factor = 185200  # 1 milla náutica es igual a 185200 centímetros
            elif unidades == "milla nautica" and nuevas_unidades == "mm":
                factor = 1.852e+6  # 1 milla náutica es igual a 1.852x10^6 milímetros
            elif unidades == "milla nautica" and nuevas_unidades == "km":
                factor = 1.852  # 1 milla náutica es igual a 1.852 kilómetros
            elif unidades == "milla nautica" and nuevas_unidades == "dam":
                factor = 0.1852  # 1 milla náutica es igual a 0.1852 decámetros
            elif unidades == "milla nautica" and nuevas_unidades == "dm":
                factor = 18.52  # 1 milla náutica es igual a 18.52 decímetros
            elif unidades == "milla nautica" and nuevas_unidades == "nm":
                factor = 1.852e+12  # 1 milla náutica es igual a 1.852x10^12 nanómetros
            elif unidades == "milla nautica" and nuevas_unidades == "yd":
                factor = 2025.37  # 1 milla náutica es igual a 2025.37 yardas
            elif unidades == "milla nautica" and nuevas_unidades == "μm":
                factor = 1.852e+9  # 1 milla náutica es igual a 1.852x10^9 micrómetros
            elif unidades == "milla nautica" and nuevas_unidades == "in":
                factor = 72913.4  # 1 milla náutica es igual a 72913.4 pulgadas
            elif unidades == "milla nautica" and nuevas_unidades == "mi":
                factor = 1.15078  # 1 milla náutica es igual a 1.15078 millas
            elif unidades == "milla nautica" and nuevas_unidades == "ft":
                factor = 6076.12  # 1 milla náutica es igual a 6076.12 pies
                
            elif unidades == "ft" and nuevas_unidades == "m":
                factor = 0.3048  # 1 pie es igual a 0.3048 metros
            elif unidades == "ft" and nuevas_unidades == "cm":
                factor = 30.48  # 1 pie es igual a 30.48 centímetros
            elif unidades == "ft" and nuevas_unidades == "mm":
                factor = 304.8  # 1 pie es igual a 304.8 milímetros
            elif unidades == "ft" and nuevas_unidades == "km":
                factor = 0.0003048  # 1 pie es igual a 0.0003048 kilómetros
            elif unidades == "ft" and nuevas_unidades == "dam":
                factor = 0.03048  # 1 pie es igual a 0.03048 decámetros
            elif unidades == "ft" and nuevas_unidades == "dm":
                factor = 3.048  # 1 pie es igual a 3.048 decímetros
            elif unidades == "ft" and nuevas_unidades == "nm":
                factor = 304800000  # 1 pie es igual a 304800000 nanómetros
            elif unidades == "ft" and nuevas_unidades == "yd":
                factor = 0.333333  # 1 pie es igual a 0.333333 yardas
            elif unidades == "ft" and nuevas_unidades == "μm":
                factor = 304800  # 1 pie es igual a 304800 micrómetros
            elif unidades == "ft" and nuevas_unidades == "in":
                factor = 12  # 1 pie es igual a 12 pulgadas
            elif unidades == "ft" and nuevas_unidades == "milla nautica":
                factor = 0.000164579  # 1 pie es igual a 0.000164579 millas náuticas
            elif unidades == "ft" and nuevas_unidades == "mi":
                factor = 0.000189394  # 1 pie es igual a 0.000189394 millas


            label_cateto_opuesto.config(text=f"Cateto Opuesto: {resultados[0] * factor:.9f} {nuevas_unidades}")
            label_cateto_adyacente.config(text=f"Cateto Adyacente: {resultados[1] * factor:.9f} {nuevas_unidades}")
            label_hipotenusa.config(text=f"Hipotenusa: {resultados[2] * factor:.9f} {nuevas_unidades}")
        def volver_al_menu():
            ventana_resultados.destroy()

        opciones_unidades = ["m", "cm", "mm", "km", "dam", "dm", "μm", "nm", "yd", "in", "mi", "milla nautica", "ft"]
        seleccion_unidades = unidades
        menu_unidades = ttk.Combobox(frame_resultados, values=opciones_unidades, font=("Arial", 20))
        menu_unidades.grid(row=5, column=0, padx=10, pady=5)
        menu_unidades.set(seleccion_unidades)
        menu_unidades.config(state="readonly")

        button_cambiar = tk.Button(frame_resultados, text="Cambiar UNID", command=lambda: cambiar_unidades(menu_unidades.get()), font=("Arial", 20))
        button_cambiar.grid(row=5, column=1, padx=10, pady=5)

        button_volver = tk.Button(frame_resultados, text="Volver al Menú Principal", command=volver_al_menu, font=("Arial", 20))
        button_volver.grid(row=6, column=0, columnspan=2, padx=10, pady=5)
       
    else:
        messagebox.showerror("Error", "No se han encontrado resultados.")

def main():
    def abrir_ventana():
        ventana_nueva = tk.Toplevel(ventana_principal)
        ventana_nueva.title("Ventana nueva")
        label_nueva = tk.Label(ventana_nueva, text="Esta es una ventana nueva", font=("Arial", 30))
        label_nueva.pack()
        ventana_principal.withdraw()  # Ocultar la ventana principal

    ventana_principal = tk.Tk()
    ventana_principal.title("Teorema de Pitágoras")

    label_menu = tk.Label(ventana_principal, text="Menú:", font=("Arial", 30, "bold"))
    label_menu.pack()

    opciones_menu = [
        "Un cateto.",
        "Hipotenusa.",
        "Cateto Opuesto y ángulo beta β.",
        "Cateto adyacente y ángulo beta β.",
        "Hipotenusa y ángulo beta β.",
        "Cateto opuesto y ángulo alpha α.",
        "Cateto adyacente y ángulo alpha α.",
        "Hipotenusa y ángulo alpha α.",
        "Cateto opuesto y Cateto adyacente.",
        "Cateto adyacente e Hipotenusa.",
        "Cateto opuesto e Hipotenusa.",
        "Cateto opuesto, cateto adyacente e Hipotenusa.",
        "Cateto opuesto, cateto adyacente, Hipotenusa y angulo alpha.",
        "Cateto opuesto, cateto adyacente, Hipotenusa y angulo beta.",
        "Cateto opuesto, cateto adyacente y angulo alpha.",
        "Cateto opuesto, cateto adyacente y angulo beta.",
        "Cateto opuesto, hipotenusa y angulo alpha.",
        "Cateto adyacente, hipotenusa y angulo beta."
    ]

    seleccion_menu = tk.StringVar()
    seleccion_menu.set(opciones_menu[0])

    menu = tk.OptionMenu(ventana_principal, seleccion_menu, *opciones_menu)
    menu.config(font=("Arial", 30))
    menu.pack()

    def calcular():
        opcion = opciones_menu.index(seleccion_menu.get()) + 1
        resultados = calcular_triangulo_rectangulo(opcion)
        if resultados:
            dialogo_unidades = UnidadesDialog(ventana_principal, title="Unidades", prompt="Seleccione las unidades del triángulo:", options=["m", "cm", "mm", "km", "dam", "dm", "μm", "nm", "yd", "in", "mi", "milla nautica", "ft"])
            unidades = dialogo_unidades.result
            if unidades:
                mostrar_resultados(resultados, unidades)
        else:
            messagebox.showerror("Error", "No se han encontrado resultados.")

    button_calcular = tk.Button(ventana_principal, text="Calcular", command=calcular, font=("Arial", 30))
    button_calcular.pack()



    ventana_principal.mainloop()

if __name__ == "__main__":
    main()
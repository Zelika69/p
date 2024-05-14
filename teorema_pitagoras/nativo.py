import math
import tkinter as tk
from tkinter import simpledialog, messagebox

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
        
        # Resto de las opciones omitidas por brevedad...
        else:
            messagebox.showerror("Error", "Opción no válida.")
            return None

    return cateto_opuesto, cateto_adyacente, hipotenusa, angulo_alpha, angulo_beta

def mostrar_resultados(resultados, unidades):
    if resultados:
        ventana_resultados = tk.Tk()
        ventana_resultados.title("Resultados")

        label_resultados = tk.Label(ventana_resultados, text="Resultados", font=("Arial", 16, "bold"))
        label_resultados.pack()

        frame_resultados = tk.Frame(ventana_resultados)
        frame_resultados.pack(padx=10, pady=5)

        label_cateto_opuesto = tk.Label(frame_resultados, text=f"Cateto Opuesto: {resultados[0]:.4f} {unidades}")
        label_cateto_opuesto.grid(row=0, column=0, sticky="w")

        label_cateto_adyacente = tk.Label(frame_resultados, text=f"Cateto Adyacente: {resultados[1]:.4f} {unidades}")
        label_cateto_adyacente.grid(row=1, column=0, sticky="w")

        label_hipotenusa = tk.Label(frame_resultados, text=f"Hipotenusa: {resultados[2]:.4f} {unidades}")
        label_hipotenusa.grid(row=2, column=0, sticky="w")

        label_angulo_alpha = tk.Label(frame_resultados, text=f"Ángulo Alpha: {resultados[3]:.4f}°")
        label_angulo_alpha.grid(row=3, column=0, sticky="w")

        label_angulo_beta = tk.Label(frame_resultados, text=f"Ángulo Beta: {resultados[4]:.4f}°")
        label_angulo_beta.grid(row=4, column=0, sticky="w")

        label_angulo_theta = tk.Label(frame_resultados, text="Ángulo Theta: 90.0000°")
        label_angulo_theta.grid(row=5, column=0, sticky="w")

        ventana_resultados.mainloop()
    else:
        messagebox.showerror("Error", "No se han encontrado resultados.")

def main():
    ventana_principal = tk.Tk()
    ventana_principal.title("Teorema de Pitágoras")

    label_menu = tk.Label(ventana_principal, text="Menú:", font=("Arial", 16, "bold"))
    label_menu.pack()

    opciones_menu = [
        "Un cateto.",
        "Hipotenusa."
    ]

    seleccion_menu = tk.StringVar()
    seleccion_menu.set(opciones_menu[0])

    menu = tk.OptionMenu(ventana_principal, seleccion_menu, *opciones_menu)
    menu.pack()

    def calcular():
        opcion = opciones_menu.index(seleccion_menu.get()) + 1
        resultados = calcular_triangulo_rectangulo(opcion)
        if resultados:
            unidades = simpledialog.askstring("Unidades", "Seleccione las unidades del triángulo:", initialvalue="m")
            mostrar_resultados(resultados, unidades)
        else:
            messagebox.showerror("Error", "No se han encontrado resultados.")

    button_calcular = tk.Button(ventana_principal, text="Calcular", command=calcular)
    button_calcular.pack()

    ventana_principal.mainloop()

if __name__ == "__main__":
    main()

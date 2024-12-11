import tkinter as tk
from tkinter import ttk
from clase import paquete

def calcularCosto():

    try:
        peso = int(input_calculo.get())
        if peso < 0:  
            raise ValueError("Introduce un valor positivo:")

        peso = int(input_calculo.get())
        etiqueta_error_peso1.config(text=f"")
    
        costoPaquete = paquete()
        costo = costoPaquete.calcularCosto(peso)
        
        etiqueta_monto.config(text=f"El costo del paquete es:{costo}")

    except ValueError as ve:
        if "could not convert" in str(ve):
            etiqueta_error_peso1.config(text="Introduce un valor numérico.")
        else:
            etiqueta_error_peso2.config(text=str(ve))
    
ventana = tk.Tk()
ventana.title("Calculo De Tarifa")
ventana.config(width=470, height=170)  

etiqueta_peso = ttk.Label(text="Introduce el peso del paquete:")
etiqueta_peso.place(x=10, y=10)

input_calculo = ttk.Entry()
input_calculo.place(x=200, y= 10, width=80)

# etiqueta errores
etiqueta_error_peso1 = ttk.Label(text="")
etiqueta_error_peso1.place(x=300, y=10)
etiqueta_error_peso2 = ttk.Label(text="")
etiqueta_error_peso2.place(x=300, y=30)
#boton para calcular
boton_calcular = ttk.Button(ventana, text="Calcular", command=calcularCosto)
boton_calcular.place(x=200, y=40)

etiqueta_monto = ttk.Label(ventana, text="El costo total es:")
etiqueta_monto.place(x=10, y=99)

# ejecutar la aplicacion
ventana.mainloop()
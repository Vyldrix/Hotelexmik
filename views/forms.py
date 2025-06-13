import tkinter as tk

def crear_formulario(ventana):
    etiqueta = tk.Label(ventana, text="Nombre del huésped:")
    etiqueta.pack()

    entrada = tk.Entry(ventana)
    entrada.pack()

    boton = tk.Button(ventana, text="Guardar", command=lambda: print(f"Huésped: {entrada.get()}"))
    boton.pack()
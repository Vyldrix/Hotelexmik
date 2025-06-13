import tkinter as tk
from views.forms import crear_formulario

def iniciar_app():
    ventana = tk.Tk()
    ventana.title("Sistema Hotelero")
    ventana.geometry("600x400")

    crear_formulario(ventana)

    ventana.mainloop()
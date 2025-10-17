# pseudocodigo primero crear mi primeraventana tk, luego crear un label que diga Bienvenido ingresa tu usuario y contraseña
import tkinter as tk
from funciones import usuarios

first_ventana = tk.Tk()
first_ventana.title("Proyecto1")
first_ventana.geometry("1920x1080")


def registrar_usuario():
    usuario = entrada1.get()
    contraseña = entrada2.get()
    sesion = usuarios(usuario, contraseña)
    sesion.regristar_usuario()


label1 = tk.Label(
    first_ventana, text="Bienvenido ingresa tu usuario y contraseña")
label1.config(font=("arial", 24, "bold"))
label1.pack()


label2 = tk.Label(first_ventana, text="Ingresa tu usuario")
label2.pack()


entrada1 = tk.Entry(bg="gray", fg="blue")
entrada1.pack()


label3 = tk.Label(first_ventana, text="Ingresa tu contraseña")
label3.pack()


entrada2 = tk.Entry(bg="gray", fg="blue")
entrada2.pack()


button1 = tk.Button(text="Iniciar sesion", command=registrar_usuario)
button1.pack()


button2 = tk.Button(text="Registarse")
button2.pack()


first_ventana.mainloop()

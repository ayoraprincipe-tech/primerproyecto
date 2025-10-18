# pseudocodigo primero crear mi primeraventana tk, luego crear un label que diga Bienvenido ingresa tu usuario y contraseña
import tkinter as tk
from funciones import usuarios
from tkinter import messagebox

first_ventana = tk.Tk()
first_ventana.title("Proyecto1")
first_ventana.geometry("1920x1080")


def registrar_user():
    if (aceptarpoliticas.get()):
        usuario = entrada1.get()
        contraseña = entrada2.get()
        sesion = usuarios(usuario, contraseña)
        return sesion.regristar_usuario()
    else:
        return messagebox.showinfo("Información", "acepte las politicas de privacidad")


label1 = tk.Label(
    first_ventana, text="Bienvenido ingresa tu usuario y contraseña")
label1.config(font=("arial", 24, "bold"))
label1.pack()


label2 = tk.Label(first_ventana, text="Ingresa tu usuario",
                  font=("arial", 12, "bold"))
label2.pack()


entrada1 = tk.Entry(bg="gray", fg="black", font=(
    "arial", 12), text="user here:")
entrada1.pack()


label3 = tk.Label(first_ventana, text="Ingresa tu contraseña",
                  font=("arial", 12, "bold"))
label3.pack()


entrada2 = tk.Entry(bg="gray", fg="black", font=("arial", 12))
entrada2.pack()

aceptarpoliticas = tk.BooleanVar()
Politicas_check = tk.Checkbutton(
    first_ventana, text="Acepta las politicas de privacidad", font=("arial", 12, "bold"), variable=aceptarpoliticas)
Politicas_check.pack()

Iniciar_sesion = tk.Button(
    text="Iniciar sesion", font=("arial", 12, "bold"))
Iniciar_sesion.pack()


Regristate_buton = tk.Button(
    text="Registarse", command=registrar_user, font=("arial", 12, "bold"))
Regristate_buton.pack()


first_ventana.mainloop()

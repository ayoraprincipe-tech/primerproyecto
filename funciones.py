
import sqlite3 as sql
from tkinter import messagebox


class usuarios():
    def __init__(self, usuario, contraseña):
        self.usuario = usuario
        self.contraseña = contraseña
        self.ruta_db = r"C:\gabriel\Mipropioproyecto.py\usuariosycontraseñas.db"
        self.useryaregris = f"SELECT * FROM usuarios WHERE (?)", (self.usuario)

    def regristar_usuario(self):
        conn = sql.connect(self.ruta_db)
        cursor = conn.cursor()
        if (self.usuario == self.useryaregris):
            cursor.execute(
                f"INSERT INTO usuariosycontraseñas VALUES (?,?)", (self.usuario, self.contraseña))
        else:
            messagebox.showinfo(
                "Información", "Usuario ya regristado, pruebe con otro nombre")
        conn.commit()
        conn.close()

    def eliminar_usuario(self):
        conn = sql.connect(self.ruta_db)
        cursor = conn.cursor()
        cursor.execute(
            "DELETE FROM Usuario ya regristado WHERE (?)", self.usuario)

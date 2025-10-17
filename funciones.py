
import sqlite3 as sql


class usuarios():
    def __init__(self, usuario, contraseña):
        self.usuario = usuario
        self.contraseña = contraseña
        self.ruta_db = r"C:\gabriel\Mipropioproyecto.py\usuariosycontraseñas.db"

    def regristar_usuario(self):
        conn = sql.connect(self.ruta_db)
        cursor = conn.cursor()
        cursor.execute(
            f"INSERT INTO usuariosycontraseñas VALUES (?,?)", (self.usuario, self.contraseña))
        conn.commit()
        conn.close()

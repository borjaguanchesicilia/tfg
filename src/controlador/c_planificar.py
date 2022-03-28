import os
from tkinter import filedialog
from tkinter.messagebox import showerror
from src.controlador.c_lectura_fichero import FicheroCsv


class Planificar:
    def __init__(self):

        ruta = str(os.path.dirname(os.path.abspath(__file__)))
        self.ruta_fichero = str(
            filedialog.askopenfilename(
                initialdir=ruta, title="Abrir fichero vuelos"
            )
        )

        self.obtener_nombre()

        try:
            if ".csv" not in self.nombre_fichero:
                raise NameError()
        except:
            print(showerror("ERROR", "El fichero no es .csv"))
        else:
            self.fichero = FicheroCsv(self.nombre_fichero)
            print(self.fichero.get_columnas())

    def obtener_nombre(self):

        nombre_fichero = self.ruta_fichero[::-1]

        indice = 0
        while nombre_fichero[indice] != "/":
            indice += 1

        nombre_fichero = nombre_fichero[0:indice][::-1]

        self.nombre_fichero = nombre_fichero

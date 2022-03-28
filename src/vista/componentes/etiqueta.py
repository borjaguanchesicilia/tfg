from src.controlador.librerias import *


class Etiqueta:
    def __init__(self, frame, texto, fila, columna):

        self.__etiqueta = Label(frame, text=texto)

        self.__etiqueta.config(
            font=("Adobe Caslon Pro", 15, "bold"), fg="#FFFFFF", bg="#333333"
        )

        self.__etiqueta.grid(
            pady=10,
            padx=10,
            row=fila,
            column=columna,
            columnspan=1,
            sticky=S + N + E + W,
        )

    def set_texto(self, nombre_fichero):
        self.__etiqueta.config(text=f"Fichero: {nombre_fichero}")

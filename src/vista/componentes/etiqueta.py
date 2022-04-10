from src.controlador.librerias import *


class Etiqueta:
    def __init__(self, frame, texto, fila, columna, tam=15):

        self.__etiqueta = Label(frame, text=texto)

        self.__etiqueta.config(
            font=("Adobe Caslon Pro", tam, "bold"), fg="#FFFFFF", bg="#333333"
        )

        self.__etiqueta.grid(
            pady=5,
            padx=5,
            row=fila,
            column=columna,
            columnspan=1,
            sticky=S + N + E + W,
        )

    def set_texto(self, texto):
        self.__etiqueta.config(text=texto)

    def set_fila(self, fila):
        self.__etiqueta.grid(
            pady=5,
            padx=5,
            row=fila,
            column=0,
            columnspan=1,
            sticky=S + N + E + W,
        )
        self.__fila = fila
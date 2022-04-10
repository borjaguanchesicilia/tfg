from src.controlador.librerias import *


class Boton:
    def __init__(self, frame, texto, accion, fila, columna, pady=15):

        self.__boton = Button(frame, text=texto, command=accion)

        self.__boton.config(
            font=("Adobe Caslon Pro", 15, "bold"), fg="#FFFFFF", bg="#333333"
        )

        self.__fila = fila
        self.__columna = columna

        self.__boton.grid(
            pady=pady,
            padx=10,
            row=self.__fila,
            column=self.__columna,
            columnspan=2,
            sticky=S + N + E + W,
        )

    def activar_boton(self):
        self.__boton["state"] = NORMAL

    def desactivar_boton(self):
        self.__boton["state"] = DISABLED

    def set_fila(self, fila):
        self.__boton.grid(
            pady=5, padx=10, row=fila, column=1, columnspan=2, sticky=S + N + E + W
        )
        self.__fila = fila
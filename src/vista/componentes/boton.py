from src.controlador.librerias import *


class Boton:
    def __init__(self, frame, texto, accion, fila, columna, pady=10):

        self.__boton = Button(frame, text=texto, command=accion)

        self.__boton.config(
            font=("Adobe Caslon Pro", 15, "bold"), fg="#FFFFFF", bg="#333333"
        )

        self.__boton.grid(
            pady=pady,
            padx=10,
            row=fila,
            column=columna,
            columnspan=2,
            sticky=S + N + E + W,
        )

    def activar_boton(self):
        self.__boton["state"] = NORMAL

    def desactivar_boton(self):
        self.__boton["state"] = DISABLED

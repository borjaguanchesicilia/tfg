from src.controlador.librerias import *
from src.vista.componentes.boton import *
from src.vista.componentes.etiqueta import Etiqueta


class ParametroDia:
    def __init__(self, vista, ventana_dias, dia, fila):

        self.frame = Frame(vista)

        self.__dia = dia
        self.__ventana_dias = ventana_dias
        self.__fila = fila

        # Atributo etiqueta
        self.__etiqueta = Etiqueta(self.frame, self.__dia, self.__fila, 0)

        # Atributo Boton
        self.__boton = Boton(self.frame, "X", self.borrar_dia, self.__fila, 1, 5)

        self.frame.pack()

    def actualizar_fila(self):
        if self.__fila != 0:
            self.__fila = self.__fila - 1
            self.__etiqueta.set_fila(self.__fila)
            self.__boton.set_fila(self.__fila)

    def get_dia(self):
        return self.__dia

    def get_fila(self):
        return self.__fila

    def borrar_dia(self):
        self.__ventana_dias.borrar_dia(self)
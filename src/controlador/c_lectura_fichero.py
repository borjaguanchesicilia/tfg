from src.controlador.librerias import *


class FicheroCsv:
    def __init__(self, nombre_fichero):

        self.__fichero = pd.read_csv(nombre_fichero, sep=";")
        self.__filas = len(self.__fichero.axes[0])
        self.__columnas = len(self.__fichero.axes[1])
        self.__cabeceras = list(self.__fichero.columns)
        print(self.__fichero)

    def get_filas(self):
        return self.__filas

    def get_columnas(self):
        return self.__columnas

    def get_cabecera(self, indice):
        return self.__cabeceras[indice]

    def get_elemento(self, cabecera, indice):
        return self.__fichero[f"{cabecera}"][indice]

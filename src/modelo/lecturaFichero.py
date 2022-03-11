from src.controlador.librerias import *


class FicheroCsv():

    def __init__(self, nombreFichero):
        
        self.__fichero = pd.read_csv(nombreFichero, sep= ';') 
        self.__filas = len(self.__fichero.axes[0])
        self.__columnas = len(self.__fichero.axes[1])
        self.__cabeceras = list(self.__fichero.columns)


    def getFilas(self):
        return self.__filas


    def getColumnas(self):
        return self.__columnas

    
    def getCabecera(self, indice):
        return self.__cabeceras[indice]

    
    def getElemento(self, cabecera, indice):
        return self.__fichero[f'{cabecera}'][indice]
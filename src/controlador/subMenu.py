from src.controlador.librerias import *


class Submenu:

    def __init__(self, barraMenu, nombre, opciones):

        self.__nOpciones = len(opciones)
        self.__subMenu = Menu(barraMenu)
        
        for i in range(self.__nOpciones):
            if opciones[i][1] == "":
                self.__subMenu.add_command(label= opciones[i][0])
            else:
                self.__subMenu.add_command(label= opciones[i][0], command= opciones[i][1])

        barraMenu.add_cascade(label= nombre, menu= self.__subMenu)
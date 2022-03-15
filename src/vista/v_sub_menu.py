from src.controlador.librerias import *


class Submenu:

    def __init__(self, barra_menu, nombre, opciones):

        self.__num_opciones = len(opciones)
        self.__sub_menu = Menu(barra_menu)
        
        for i in range(self.__num_opciones):
            if opciones[i][1] == "":
                self.__sub_menu.add_command(label= opciones[i][0])
            else:
                self.__sub_menu.add_command(label= opciones[i][0], command= opciones[i][1])

        barra_menu.add_cascade(label= nombre, menu= self.__sub_menu)
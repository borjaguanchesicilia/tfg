from src.controlador.librerias import *
from src.controlador.subMenu import Submenu
from src.controlador.tabla import Tabla
from src.modelo.lecturaFichero import FicheroCsv


class Vista(Frame):

    def __init__(self, app):
        super().__init__(app)

        self.app = app

        # Aspecto de la aplicación
        self.app.geometry('1200x500')
        self.app.title("Aplicacion prueba")
        #self.attributes("-fullscreen", True)
        self.app['bg']='#333333'
        self.app.tk.call("source", "./src/vista/azure.tcl")
        self.app.tk.call("set_theme", "dark")

        # Creación del menu
        self.barraMenu = Menu(self)

        # Submenu Archivo    
        Submenu(self.barraMenu, "Archivo", [("Abrir", ""), ("Guardar como", ""), ("Minimizar", self.app.iconify), ("Salir", self.app.destroy)])

        # Submenu Ver 
        Submenu(self.barraMenu, "Ver", [("Modelos aviones", self.verModelosAviones), ("Vuelos", self.verVuelos), ("Planificacion", "")])

        self.app.config(menu=self.barraMenu)


    def verModelosAviones(self):

        fichero = FicheroCsv("./aviones.csv")
        Tabla(self, "Modelos de aviones", fichero, fichero.getFilas(), fichero.getColumnas(), self.app.winfo_height(), self.app.winfo_width())

    
    def verVuelos(self):

        fichero = FicheroCsv("./ACE.csv")
        Tabla(self, "Planificación vuelos", fichero, fichero.getFilas(), fichero.getColumnas(), self.winfo_height(), self.winfo_width())
from src.controlador.librerias import *
from src.vista.v_sub_menu import Submenu
from src.vista.v_tabla import Tabla
from src.controlador.c_parametros import ControladorParametros
from src.controlador.c_lectura_fichero import FicheroCsv
from src.vista.v_parametros import VistaParametros


class Vista(Frame):

    def __init__(self, app):
        super().__init__(app)

        self.app = app

        # Aspecto de la aplicación
        self.app.geometry('1200x500')
        self.app.title("Aplicacion prueba")
        #self.attributes("-fullscreen", True)
        self.app['bg']='#333333'
        self.app.minsize(670, 500)
        self.app.tk.call("source", "./src/vista/azure.tcl")
        self.app.tk.call("set_theme", "dark")

        # Creación del menu
        self.barra_menu = Menu(self)

        # Submenu Archivo    
        Submenu(
            self.barra_menu, "Archivo", [("Abrir", ""),
            ("Guardar como", ""), ("Minimizar", self.app.iconify),
            ("Salir", self.app.destroy)])

        # Submenu Ver 
        Submenu(
            self.barra_menu, "Ver",
            [("Modelos aviones", self.ver_modelos_aviones),
            ("Vuelos", self.ver_vuelos), ("Planificacion", "")])

        # Submenu Planificar 
        Submenu(
            self.barra_menu, "Planificar",
            [("Parámetros", self.intro_parametros)])


        self.app.config(menu= self.barra_menu)


    def ver_modelos_aviones(self):

        fichero = FicheroCsv("./ficheros/aviones.csv")
        Tabla(
            self, "Modelos de aviones", fichero, fichero.get_filas(),
            fichero.get_columnas(), self.app.winfo_height(),
            self.app.winfo_width())

    
    def ver_vuelos(self):

        fichero = FicheroCsv("./ACE.csv")
        Tabla(
            self, "Planificación vuelos", fichero, fichero.get_filas(),
            fichero.get_columnas(), self.winfo_height(),
            self.winfo_width())

    
    def intro_parametros(self):
        
        vista_parametros = VistaParametros(
            self, "Selector de parámetros")

        controlador = ControladorParametros(vista_parametros)
        vista_parametros.set_controlador(controlador)
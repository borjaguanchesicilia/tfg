from src.controlador.c_planificar import ControladorPlanificar
from src.librerias import *
from src.controlador.c_parametros import ControladorParametros
from src.controlador.c_etl import ControladorEtl
from src.vista.componentes_vistas.boton import Boton
from src.vista.componentes_vistas.etiqueta import Etiqueta
from src.vista.v_etl import VistaEtl
from src.vista.v_parametros import VistaParametros
from src.vista.v_planificar import VistaPlanificar


class Vista(Frame):
    def __init__(self, app):
        super().__init__(app)

        self.app = app
        self.__controlador = None

        # Aspecto de la aplicación
        self.app.geometry("1200x500")
        self.app.title("Planificación FRONTUR-CANARIAS")
        # self.attributes("-fullscreen", True)
        self.app["bg"] = "#333333"
        self.app.minsize(1070, 500)

        # Etiqueta cabecera
        self.__cabecera = Frame(self.app)
        self.__cabecera.config(bg="#333333")

        self.__titulo = Label(
            self.__cabecera,
            text=("Planificador de encuestas FRONTUR-CANARIAS"),
            fg="#FFFFFF",
            bg="#333333",
        )

        self.__titulo.config(font=("Adobe Caslon Pro", 20, "bold"))
        self.__titulo.pack(padx=5, pady=15)

        self.__cabecera.pack(padx=10, pady=20)

        # Menu central
        self.__f_menu = LabelFrame(self.app)
        self.__f_menu.config(
            font=("Adobe Caslon Pro", 15, "bold"),
            fg="#FFFFFF",
            bg="#333333",
            labelanchor="n",
        )

        # Etiqueta "Paso 1"
        self.__etiqueta_paso_1 = Etiqueta(self.__f_menu, "Paso 1:", 0, 0)

        # Botón "Introducir parámetros"
        self.boton_parametros = Boton(
            self.__f_menu, "Introducir parámetros", self.vista_parametros, 0, 2
        )

        # Etiqueta "Paso 2"
        self.__etiqueta_paso_2 = Etiqueta(self.__f_menu, "Paso 2:", 1, 0)

        # Botón "ETL"
        self.boton_etl = Boton(self.__f_menu, "ETL", self.vista_etl, 1, 2)

        # Etiqueta "Paso 3"
        self.__etiqueta_paso_3 = Etiqueta(self.__f_menu, "Paso 3:", 2, 0)

        # Botón "Planificar"
        self.boton_planificar = Boton(
            self.__f_menu, "Planificar", self.vista_planificar, 2, 2
        )

        # Botón "Ayuda"
        self.boton_ayuda = Boton(
            self.__f_menu, "Ayuda", self.ayuda, 3, 2, columnspan=4
        )

        self.__f_menu.pack(padx=10, pady=20)

    def set_controlador(self, controlador):
        self.__controlador = controlador

    def vista_parametros(self):
        vista_parametros = VistaParametros(self.app)
        self.__controlador_parametros = ControladorParametros(
            vista_parametros, self.__controlador
        )
        vista_parametros.set_controlador(self.__controlador_parametros)
        vista_parametros.set_botones()

    def vista_etl(self):
        vista_etl = VistaEtl(self.app)
        self.__controlador_etl = ControladorEtl(
            vista_etl, self.__controlador_parametros, self.__controlador
        )
        vista_etl.set_controlador(self.__controlador_etl)
        vista_etl.set_botones()

    def vista_planificar(self):
        vista_planificar = VistaPlanificar(self.app)
        controlador_planificar = ControladorPlanificar(
            vista_planificar,
            self.__controlador,
            self.__controlador_parametros,
            self.__controlador_etl,
        )
        vista_planificar.set_controlador(controlador_planificar)

    def ayuda(self):
        open_new('https://github.com/borjaguanchesicilia/tfg/blob/master/README.md')    

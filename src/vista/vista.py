from src.controlador.librerias import *
from src.controlador.c_parametros import ControladorParametros
from src.controlador.c_etl import ControladorEtl
from src.vista.componentes.boton import Boton
from src.vista.componentes.etiqueta import Etiqueta
from src.vista.v_etl import VistaEtl
from src.vista.v_parametros import VistaParametros


class Vista(Frame):
    def __init__(self, app):
        super().__init__(app)

        self.app = app

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
            text=(
                "Aplicación para "
                "la planificación de encuestas FRONTUR-CANARIAS"
            ),
            fg="#FFFFFF",
            bg="#333333",
        )

        self.__titulo.config(font=("Adobe Caslon Pro", 20, "bold"))
        self.__titulo.pack(padx=5, pady=15)

        self.__cabecera.pack(padx=10, pady=20)

        # Menu central
        self.__f_menu = LabelFrame(self.app, text="PLANIFICADOR")
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

        # Botones ocultos

        # Botón "Ver parámetros"
        self.boton_ver_parametros = Boton(
            self.__f_menu, "Ver parámetros", self.vista_ver_parametros, 0, 4
        )

        # Botón "Ver fichero"
        self.boton_ver_dataframes = Boton(
            self.__f_menu, "Ver dataframes", self.vista_ver_dataframes, 1, 4
        )

        # Botón "Ver planificación"
        self.boton_ver_planificacion = Boton(
            self.__f_menu,
            "Ver planificación",
            self.vista_ver_planificacion,
            2,
            4,
        )

        self.__f_menu.pack(padx=10, pady=20)

        # Botones pie de App
        self.__f_pie = Frame(self.app)
        self.__f_pie.config(bg="#333333")

        # Botón "Ayuda"
        self.boton_ayuda = Boton(self.__f_pie, "Ayuda", self.ayuda, 0, 0)

        # Botón "Ver planificaciones"
        self.boton_ver_planificaciones = Boton(
            self.__f_pie, "Ver planificaciones", self.ver_planificaciones, 0, 2
        )

        # Botón "Resetear"
        self.boton_resetear = Boton(
            self.__f_pie, "Resetear", self.resetear, 0, 4
        )

        self.boton_ver_parametros.desactivar_boton()
        self.boton_etl.desactivar_boton()
        self.boton_ver_dataframes.desactivar_boton()
        self.boton_planificar.desactivar_boton()
        self.boton_ver_planificacion.desactivar_boton()
        self.boton_resetear.desactivar_boton()

        self.__f_pie.pack(padx=10, pady=20)

    def vista_parametros(self):
        vista_parametros = VistaParametros(self.app)
        self.controlador_parametros = ControladorParametros(
            self, vista_parametros
        )
        vista_parametros.set_controlador(self.controlador_parametros)

    def vista_etl(self):
        vista_etl = VistaEtl(self.app)
        controlador_etl = ControladorEtl(
            self, vista_etl, self.controlador_parametros
        )
        vista_etl.set_controlador(controlador_etl)

    def vista_planificar(self):
        # Ejecutar modelo
        pass

    def vista_ver_parametros(self):
        pass

    def vista_ver_dataframes(self):
        pass

    def vista_ver_planificacion(self):
        pass

    def ayuda(self):
        pass

    def ver_planificaciones(self):
        pass

    def resetear(self):
        pass

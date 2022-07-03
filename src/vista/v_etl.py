from src.librerias import *
from src.modelo.operaciones.lectura_fichero import FicheroCsv
from src.vista.v_parametros import *
from src.vista.componentes_vistas.check_list import ChecklistBox


class VistaEtl(Toplevel):
    def __init__(self, app):
        super().__init__(app)

        self.app = app

        self.__controlador = None

        # Aspecto de la ventana "Etl"
        self.title("Menú ETL")
        self.geometry("1200x500")
        self["bg"] = "#333333"
        self.minsize(1100, 500)
        self.attributes("-topmost", True)

        # Etiqueta cabecera
        cabecera = Frame(self)
        cabecera.config(bg="#333333")

        titulo = Label(cabecera, text="Menú de ETL")

        titulo.config(
            font=("Adobe Caslon Pro", 20, "bold"), fg="#FFFFFF", bg="#333333"
        )

        titulo.pack(padx=5, pady=15)

        cabecera.pack(padx=10, pady=20)

        # Etiqueta cabecera
        self.__f_seleccion = Frame(self)
        self.__f_seleccion.config(bg="#333333")

        # Introducir fichero GESLOT
        self.__e_fichero_vue = Etiqueta(self.__f_seleccion, "Fichero:", 2, 2)

        # Introducir fichero aviones
        self.__e_fichero_avi = Etiqueta(self.__f_seleccion, "Fichero:", 3, 2)

        self.__f_seleccion.pack(padx=10, pady=20)

    def set_controlador(self, controlador):
        self.__controlador = controlador

    def set_botones(self):
        self.__b_fichero_vue = Boton(
            self.__f_seleccion,
            "Introducir fichero GESLOT",
            partial(
                self.__controlador.set_fichero_vuelos, self.__e_fichero_vue
            ),
            2,
            0,
            15,
        )

        self.__b_fichero_avi = Boton(
            self.__f_seleccion,
            "Introducir fichero aviones",
            partial(
                self.__controlador.set_fichero_aviones, self.__e_fichero_avi
            ),
            3,
            0,
            15,
        )

        self.boton_etl = Boton(
            self.__f_seleccion,
            "Aplicar ETL",
            self.__controlador.comprobar_etl,
            4,
            0,
            15,
            2,
        )

    def set_etiqueta_fichero(self, nombre_fichero, etiqueta):
        etiqueta.set_texto("Fichero: " + nombre_fichero)
